import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from rights_audit import validate_rights
from validate_atlas import local_path


class RightsEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.folder=tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root=Path(self.folder.name)
        (self.root/'LICENSE').write_text('MIT test fixture')
        (self.root/'LICENSE-SCOPE.md').write_text('Code only')
        (self.root/'CONTENT-LICENSE').write_text('Content license fixture')
        (self.root/'images').mkdir()
        (self.root/'images/photo.bin').write_bytes(b'original image fixture')
        sha=hashlib.sha256(b'original image fixture').hexdigest()
        self.review={'assets':[{'path':'images/photo.bin','sha256':sha,'status':'cleared','license':'CC0-1.0','evidence_ids':['photo'],'provenance':{'status':'verified-upstream-derivative','observed_sha256':sha}}]}
        self.evidence={'records':[{'id':'photo','permission_basis':'Specific upstream CC0 declaration','local_sha256':sha,'license':'CC0-1.0'}]}
        self.policy={'code':{'status':'selected','spdx':'MIT','text':'LICENSE','scope':'LICENSE-SCOPE.md'},**{key:{'status':'selected','license':'fixture-content-license','text':'CONTENT-LICENSE'} for key in ['editorial_content','ai_images','brand_artwork']}}

    def check(self,**kwargs):
        return validate_rights(self.review,self.evidence,self.policy,self.root,local_path,**kwargs)

    def test_mit_file_does_not_approve_undecided_content(self):
        self.policy['ai_images']={'status':'pending-owner-decision','license':None}
        errors,_=self.check(release=True)
        self.assertTrue(any('Content license remains undecided: ai_images' in e for e in errors))

    def test_cleared_requires_specific_license_evidence(self):
        self.evidence['records'][0].pop('local_sha256')
        errors,_=self.check()
        self.assertTrue(any('asset-specific matching' in e for e in errors))

    def test_generic_tool_terms_cannot_clear_an_asset(self):
        self.evidence['records'][0]={'id':'photo','permission_basis':'Tool output allocation'}
        errors,_=self.check()
        self.assertTrue(any('asset-specific matching' in e for e in errors))

    def test_changed_asset_invalidates_review(self):
        (self.root/'images/photo.bin').write_bytes(b'replacement image')
        errors,_=self.check()
        self.assertTrue(any('checksum is stale' in e for e in errors))

    def test_selected_content_requires_distributed_license_text(self):
        (self.root/'CONTENT-LICENSE').unlink()
        errors,_=self.check(release=True)
        self.assertTrue(any('Missing content license text' in e for e in errors))

    def test_changed_content_license_invalidates_recorded_terms(self):
        self.policy['ai_images']['text_sha256']=hashlib.sha256((self.root/'CONTENT-LICENSE').read_bytes()).hexdigest()
        (self.root/'CONTENT-LICENSE').write_text('Changed commercial permission')
        errors,_=self.check()
        self.assertTrue(any('Content license text checksum is stale' in e for e in errors))

    def owner_grant_fixture(self):
        asset=self.review['assets'][0]
        asset.update(kind='ai-generated-reference',license='CC-BY-NC-4.0',evidence_ids=['decision','grant'])
        self.policy['ai_images']['license']='CC-BY-NC-4.0'
        self.evidence['records']=[{'id':'decision','kind':'owner-license-decision','license':'CC-BY-NC-4.0'},
            {'id':'grant','kind':'owner-asset-license-grant','authorization':'decision','asset':asset['path'],
             'local_sha256':asset['sha256'],'license':asset['license'],'permission_basis':'Fixture owner noncommercial grant'}]

    def test_owner_grant_requires_matching_asset_path(self):
        self.owner_grant_fixture()
        self.assertEqual(self.check(release=True),([],[]))
        self.evidence['records'][1]['asset']='images/different.bin'
        errors,_=self.check()
        self.assertTrue(any('Owner grant does not match asset' in e for e in errors))

    def test_owner_grant_cannot_relicense_third_party_material(self):
        self.owner_grant_fixture()
        self.review['assets'][0]['kind']='third-party-museum-photo'
        errors,_=self.check()
        self.assertTrue(any('cannot clear third-party material' in e for e in errors))

    def test_asset_cannot_silently_change_selected_noncommercial_policy(self):
        self.owner_grant_fixture()
        self.review['assets'][0]['license']='CC-BY-4.0'
        errors,_=self.check()
        self.assertTrue(any('Asset license differs from selected project policy' in e for e in errors))

    def test_verified_photo_and_pending_owner_assets_are_distinct(self):
        self.assertEqual(self.check(release=True),([],[]))
        self.review['assets'][0].update(status='pending-owner-license',license=None)
        errors,warnings=self.check()
        self.assertEqual(errors,[])
        self.assertTrue(any('distribution decisions remain pending' in e for e in warnings))
        errors,_=self.check(release=True)
        self.assertTrue(any('distribution decisions remain pending' in e for e in errors))


if __name__=='__main__':unittest.main()
