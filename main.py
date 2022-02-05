import os
import requests
import json
from version import (get_next_version, ReleaseTypes)

class ModeTypes:
    DEV = "dev"
    OFFICIAL = "official"


def get_tag_names(owner: str, repo: str, token: str) -> list[str]:
    query_url = f"https://api.github.com/repos/{owner}/{repo}/tags"
    headers = {'Authorization': f'token {token}'}

    tag_names = []
    for i in range(1, 100):
        params = {"per_page":100, "page": i}
        response = requests.get(query_url, headers=headers, params=params)
        if not response  or response.status_code != 200 or not response.text or response.text == '[]':
            break
        tags = json.loads(response.text)
        tag_names.extend([t["name"] for t in tags])
    
    return tag_names


def get_params():
    repo = os.getenv("GITHUB_REPOSITORY", "/")
    owner, repo = repo.split("/")

    token = os.getenv('INPUT_GITHUB_TOKEN')
    
    suffix = os.getenv('INPUT_SUFFIX', "dev")

    mode = os.getenv('INPUT_MODE')
    if mode == ModeTypes.DEV:
        return (owner, repo, token, suffix, ReleaseTypes.INCREMENT)

    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        raise ValueError("Can't find event path env var (file containing event info like commit message)")
    
    with open(event_path) as f:
        data = json.load(f)
    for commit in data["commits"]:
        for release_type in [ReleaseTypes.MAJOR, ReleaseTypes.PATCH]:
            if f'#{release_type}' in  commit["message"]:
                print(f'Detected hashtag #{release_type} in message, relase type: {release_type} selected')
                return (owner, repo, token, suffix, release_type)
        
    raise ValueError(f'Could not find hashtag #{ReleaseTypes.MAJOR} nor #{ReleaseTypes.PATCH} in commit message')


def main():
    (owner, repo, token, suffix, release_type)  = get_params()

    print(f'owner: {owner}, repo: {repo}, token: {token}, suffix: {suffix}, Release type: {release_type}')

    tags = get_tag_names(owner, repo, token)
    next_version = get_next_version(suffix, tags, release_type)
    
    print(f'Next version: {next_version}')
    print(f"::set-output name=version::{next_version}")


if __name__ == "__main__":
    main()
