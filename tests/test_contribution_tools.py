import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'));sys.path.insert(0,str(ROOT/'tools/builders'))
from contribution_tools import next_identifier
from review_contribution import review_proposal


class ContributionToolTests(unittest.TestCase):
    def fixture(self):
        return {'schema':'female-appearance-contribution/v1',
                'entries':[{'stable_id':'HC100','category':'hair','dimension':'长度','name':'新发型','en':'new hair','description':'一个新的轮廓'}],
                'boards':[{'id':'new-hair','image':'images/new-hair.png','width':10,'height':20,'columns':1,'rows':1,'items':[{'entry_id':'HC100'}]}],
                'submission':{'status':'pending-review','author':'贡献者','creation_method':'original','license':'CC-BY-NC-4.0',
                              'image':{'bytes':5,'sha256':hashlib.sha256(b'image').hexdigest()}}}

    def check(self,payload,image=None):
        catalog={'entries':[{'id':'HC001','name':'旧发型','en':'old hair'}],'categories':[{'id':'hair'}],'boards':[]}
        return review_proposal(payload,catalog,{'HC001','HC099'},{'hair':'HC'},image)

    def test_suggestion_skips_retired_identifiers_without_reserving_them(self):
        identifiers={'HC001','HC099','HCA999'};before=set(identifiers)
        self.assertEqual(next_identifier('HC',identifiers),'HC100')
        self.assertEqual(identifiers,before)

    def test_draft_hash_is_checked_without_granting_rights(self):
        payload=self.fixture();before=copy.deepcopy(payload)
        with tempfile.TemporaryDirectory() as folder:
            image=Path(folder)/'new.png';image.write_bytes(b'image')
            result=self.check(payload,image)
            self.assertTrue(result['valid']);self.assertTrue(result['image_hash_verified'])
            image.write_bytes(b'changed')
            self.assertFalse(self.check(payload,image)['valid'])
        self.assertEqual(payload,before)
        self.assertEqual(payload['submission']['status'],'pending-review')

    def test_collisions_traversal_and_self_approval_are_rejected(self):
        payload=self.fixture();payload['entries'][0]['stable_id']='HC099'
        payload['boards'][0]['image']='images/../private.png';payload['submission']['status']='cleared'
        result=self.check(payload)
        self.assertFalse(result['valid']);self.assertGreaterEqual(len(result['errors']),3)
        payload=self.fixture();payload['entries'][0]['stable_id']=[]
        self.assertFalse(self.check(payload)['valid'])

    def test_external_material_requires_source_and_authorization_details(self):
        payload=self.fixture();payload['submission']['creation_method']='third-party'
        self.assertFalse(self.check(payload)['valid'])
        payload['submission']['source_url']='https://example.org/original'
        self.assertTrue(self.check(payload)['valid'])
        payload['submission']['license']='other'
        self.assertFalse(self.check(payload)['valid'])
        payload['submission']['rights_note']='授权内容待维护者核实'
        self.assertTrue(self.check(payload)['valid'])


if __name__=='__main__':unittest.main()
