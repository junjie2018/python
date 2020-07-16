#!/usr/bin/python3

import deploy_config
import os
import git
import subprocess
import shutil


class NoKeyPathException(Exception): pass


class PackageFailedException(Exception): pass


def git_update(service_name, source_root, git_url, git_branch):
    source_path = os.path.join(source_root, service_name)
    if os.path.isdir(source_path):
        # git pull
        repo = git.Repo(source_path)
        repo.remote().pull()
        pass
    else:
        repo = git.Repo.clone_from(git_url, source_path)
        repo.git.checkout(git_branch)
        # git clone
        pass


def maven_package(service_name, source_root):
    source_path = os.path.join(source_root, service_name)
    if not os.path.isdir(source_path):
        raise NoKeyPathException("source_path not exist.")
    os.chdir(source_path)
    pipe = subprocess.Popen('mvn package -D maven.test.skip=True', shell=True, stdout=subprocess.PIPE)

    for line in pipe.stdout.readlines():
        print(line)

    pipe.wait()
    if pipe.returncode != 0:
        raise PackageFailedException


if __name__ == '__main__':
    service_name = 'online-bb-member'
    source_root = "/home/mmpprd/source"
    service = deploy_config.services[service_name]

    git_update(service_name, source_root,
               service.git_config.git_url,
               service.git_config.git_branch)
    maven_package(service_name, source_root)
