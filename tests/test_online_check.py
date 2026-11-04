import hashlib
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import check_online


class OnlineCheckTests(unittest.TestCase):
    def responses(self):
        build={'app_version':'1.0.0','content_version':'70.0','source_commit':'a'*40,
               'source_dirty':False,'runtime_index':'assets/runtime-test.js',
               'detail_chunks':{'hair':'assets/details-test.js'}}
        files={'assets/runtime-test.js':b'index fixture','assets/details-test.js':b'details fixture',
               'images/test.webp':b'image fixture'}
        manifest={'build':build,'files':[{'path':key,'bytes':len(value),'sha256':hashlib.sha256(value).hexdigest()}
                                       for key,value in files.items()]}
        files.update({'build-info.json':json.dumps(build).encode(),
                      'release-manifest.json':json.dumps(manifest).encode(),
                      'index.html':'女性之美 assets/runtime-test.js'.encode()})
        return files

    def read_from(self,files):
        return lambda request,**kwargs:io.BytesIO(files[urlsplit(request.full_url).path.removeprefix('/site/')])

    def test_published_version_and_asset_integrity(self):
        files=self.responses()
        with patch.object(check_online.urllib.request,'urlopen',side_effect=self.read_from(files)):
            result=check_online.check('https://example.invalid/site/','a'*40)
        self.assertTrue(result['passed'])
        self.assertEqual(len(result['checked_assets']),3)

    def test_stale_version_and_changed_asset_fail(self):
        files=self.responses()
        with patch.object(check_online.urllib.request,'urlopen',side_effect=self.read_from(files)):
            with self.assertRaisesRegex(ValueError,'not live yet'):
                check_online.check('https://example.invalid/site/','b'*40)
            files['images/test.webp']=b'changed content'
            with self.assertRaisesRegex(ValueError,'digest mismatch'):
                check_online.check('https://example.invalid/site/','a'*40)


if __name__=='__main__':unittest.main()
