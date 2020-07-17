import git

repo = git.Repo('.')
if repo.is_dirty():
    git = repo.git
    git.add('.')
    git.commit('-m', "auto commit")

    remote = repo.remote()
    remote.push()
else:
    print('noting to commit.')
input()
