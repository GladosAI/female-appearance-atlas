"""Check the last successful Pages deployment, including during a newer release build."""
import argparse
import json
import os
import re
import time
import urllib.request
from check_online import check


def active_deployment(repository):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repository) or any(part in {'.','..'} for part in repository.split('/')):
        raise ValueError('Expected owner/repository')
    base='https://api.github.com/repos/'+repository
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,*args,**kwargs):return None
    opener=urllib.request.build_opener(NoRedirect())
    def read(path):
        headers={'Accept':'application/vnd.github+json','User-Agent':'female-appearance-atlas-monitor',
                 'X-GitHub-Api-Version':'2022-11-28'}
        token=os.environ.get('GH_TOKEN')
        if token:headers['Authorization']='Bearer '+token
        # Credentials only go to this repository's API; website and asset checks use no token.
        with opener.open(urllib.request.Request(base+path,headers=headers),timeout=20) as response:
            return json.load(response)
    deployments=read('/deployments?environment=github-pages&per_page=20')
    for deployment in deployments:
        statuses=read('/deployments/'+str(int(deployment['id']))+'/statuses?per_page=1')
        if statuses and statuses[0]['state']=='success':
            commit=deployment['sha']
            if not re.fullmatch('[0-9a-f]{40}',commit):raise ValueError('Invalid deployed commit')
            return commit
    raise ValueError('No successful Pages deployment found')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository',required=True);parser.add_argument('--base',required=True)
    parser.add_argument('--attempts',type=int,default=4);args=parser.parse_args()
    if not args.base.startswith('https://') or not args.base.endswith('/'):
        parser.error('Expected an HTTPS site base ending in /')
    for attempt in range(args.attempts):
        try:
            result=check(args.base,active_deployment(args.repository))
            print(json.dumps(result,ensure_ascii=False));return
        except (OSError,ValueError,KeyError,StopIteration) as error:
            if attempt+1==args.attempts:raise
            print('Retrying public-site check: '+str(error),flush=True);time.sleep(10)


if __name__=='__main__':main()
