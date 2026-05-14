import requests


def fetch_repo_metadata(repo_url):

    response = requests.get(repo_url)

    return {
        "status_code": response.status_code,
        "url": repo_url
    }