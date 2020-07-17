import git

repo = git.Repo('.')
if repo.is_dirty():
    git = repo.git
    git.add('.')
    git.commit('-m', "auto commit")
else:
    print('noting to commit.')
input()
