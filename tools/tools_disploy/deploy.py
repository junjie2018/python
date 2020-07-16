#!/usr/bin/python3

import deploy_config
import os
import git
import shutil


def git_update(service_name, source_root, git_url):
    source_path = os.path.join(source_root, service_name)
    if os.path.isdir(source_path):
        # git pull
        repo = git.Repo(source_path)
        repo.remote().pull()
        pass
    else:
        repo = git.Repo.clone_from(git_url, source_path)
        repo.git.checkout('develop')
        # git clone
        pass


if __name__ == '__main__':
    service_name = 'online-bb-member'
    source_root = "/home/mmpprd/source"
    service = deploy_config.services[service_name]

    git_update(service_name, source_root, service.git_config.git_url)
