from git import Repo

def clone(url):
    folder = url.split("/")[-1].removesuffix(".git")
    Repo.clone_from(url, folder)

    return folder