import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('git'),'Git is not installed')
class GitCheckoutByteTests(unittest.TestCase):
    def test_manifest_and_provenance_files_survive_both_checkout_settings(self):
        with tempfile.TemporaryDirectory() as folder:
            base=Path(folder);repo=base/'source';repo.mkdir()
            env=dict(os.environ,GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=str(base/'no-global-config'))
            for key in ['GIT_DIR','GIT_WORK_TREE','GIT_INDEX_FILE','GIT_COMMON_DIR']:
                env.pop(key,None)
            def git(*args):
                return subprocess.run(['git',*map(str,args)],env=env,check=True,capture_output=True)
            fixtures={'data/catalog.json':b'{"sample":1}\r\n',
                      'data/navigation.json':b'{"sample":2}\n',
                      'data/agent-index.jsonl':b'{"id":"fixture"}\r\n',
                      'CONTENT-LICENSE':b'Content license fixture\n',
                      'LICENSE':b'Code license fixture\r\n',
                      'assets/brand/logo-mark.svg':b'<svg/>\n',
                      'assets/brand/beauty-profile/logo.svg':b'<svg/>\r\n'}
            shutil.copyfile(ROOT/'.gitattributes',repo/'.gitattributes')
            for relative,content in fixtures.items():
                target=repo/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(content)
            git('init','-q',repo)
            git('-C',repo,'config','core.autocrlf','true')
            git('-C',repo,'add','--all')
            git('-C',repo,'-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fixture')
            for setting in ['false','true']:
                checkout=base/('checkout-'+setting)
                git('-c','core.autocrlf='+setting,'clone','-q',repo,checkout)
                for relative,content in fixtures.items():
                    self.assertEqual(hashlib.sha256((checkout/relative).read_bytes()).digest(),
                                     hashlib.sha256(content).digest(),(setting,relative))


if __name__=='__main__':unittest.main()
