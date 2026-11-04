import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import monitor_online


class MonitorTests(unittest.TestCase):
    def test_pending_or_failed_deployment_does_not_replace_last_success(self):
        calls=[]
        responses=[
            [{'id':3,'sha':'c'*40,'statuses_url':'https://untrusted.invalid/'},
             {'id':2,'sha':'b'*40},{'id':1,'sha':'a'*40}],
            [{'state':'in_progress'}],[{'state':'failure'}],[{'state':'success'}]]
        class Opener:
            def open(self,request,**kwargs):
                calls.append(request.full_url)
                return io.BytesIO(json.dumps(responses.pop(0)).encode())
        with patch.object(monitor_online.urllib.request,'build_opener',return_value=Opener()):
            result=monitor_online.active_deployment('owner/atlas')
        self.assertEqual(result,'a'*40)
        self.assertTrue(all(url.startswith('https://api.github.com/repos/owner/atlas/') for url in calls))

    def test_repository_name_cannot_redirect_api_reads(self):
        with self.assertRaises(ValueError):monitor_online.active_deployment('owner/atlas/../../other')


if __name__=='__main__':unittest.main()
