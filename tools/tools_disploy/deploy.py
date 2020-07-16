#!/usr/bin/python3
import glob

import deploy_config
import os
import git
import subprocess
import paramiko


class NoKeyPathException(Exception): pass


class PackageFailedException(Exception): pass


class NoJarException(Exception): pass


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


def send_file(ip, machine_user, machine_password, sour_file_path, target_file_dir):
    transport = paramiko.Transport(ip)
    transport.connect(username=machine_user, password=machine_password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(sour_file_path, target_file_dir)


def send_jar_to_target(service_name, source_root, target_path, target_ip, machine_user, machine_password):
    source_path = os.path.join(source_root, service_name)
    jar_path = os.path.join(source_path, target_path)

    os.chdir(jar_path)
    jars = glob.glob('*.jar')
    if len(jars) == 0:
        raise NoJarException('no jar in target path.')

    jar_file_path = jars[0]
    send_file(target_ip, machine_user, machine_password, jar_file_path, "/home/mmpprd/tmp/temp.jar")


if __name__ == '__main__':
    service_name = 'online-bb-member'
    source_root = "/home/mmpprd/source"
    service = deploy_config.services[service_name]

    git_update(service_name, source_root,
               service.git_config.git_url,
               service.git_config.git_branch)
    maven_package(service_name, source_root)

    send_jar_to_target(service_name, source_root,
                       service.git_config.jar_path,
                       service.targets_config[0].ip,
                       service.targets_config[0].machine_user,
                       service.targets_config[0].machine_password)
