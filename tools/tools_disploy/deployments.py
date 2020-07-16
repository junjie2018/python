import glob
import os
import subprocess

import git
import paramiko


class NoKeyPathException(Exception): pass


class PackageFailedException(Exception): pass


class NoJarException(Exception): pass


class TooManyJarsException(Exception): pass


class SSHUtils:
    def __init__(self, ip, machine_user, machine_password):
        print(ip)
        print(machine_user)
        print(machine_password)
        self.transport = paramiko.Transport(ip)
        self.transport.connect(username=machine_user, password=machine_password)

    def send_file(self, source_file, target_file):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        print(source_file)
        print(target_file)
        sftp.put(source_file, target_file)

        # todo 这个地方需要关闭么


class Deployment:
    def __init__(self, source_root, service, target_config):
        self.service_name = service.service_name
        self.source_root = source_root
        self.source_path = os.path.join(source_root, service.service_name)

        print(os.path.join(self.source_path, service.git_config.jar_path, '*.jar'))

        jars = glob.glob(os.path.join(self.source_path, service.git_config.jar_path, '*.jar'))
        if len(jars) == 0:
            raise NoJarException('jar file missing.')
        if len(jars) > 1:
            raise TooManyJarsException('too many jars')

        self.jar_path = jars[0]
        print(self.jar_path)

        # jar 包将会被发送到这个目录下
        self.target_dir = 'deploy/%s_%s' % (self.service_name, target_config.port)

        self.transportUtil = SSHUtils(target_config.ip,
                                      target_config.machine_user,
                                      target_config.machine_password)
        pass

    def send_jar(self):
        print(self.jar_path)
        print(self.target_dir)

        if not os.path.isfile(self.jar_path):
            raise NoJarException('Jar Not Exist.')
        self.transportUtil.send_file(self.jar_path, self.target_dir)
        pass

    def deploy(self):
        pass

    def kill(self):
        pass


class Deployments:
    def __init__(self, source_root, service):
        self.service_name = service.service_name
        self.source_root = source_root
        self.source_path = os.path.join(source_root, service.service_name)

        self.git_url = service.git_config.git_url
        self.git_branch = service.git_config.git_branch

        self.deployments = []

        for target_config in service.targets_config:
            self.deployments.append(Deployment(source_root, service, target_config))

    def package(self):
        if not os.path.isdir(self.source_path):
            raise NoKeyPathException("source_path not exist.")
        os.chdir(self.source_path)
        pipe = subprocess.Popen('mvn package -D maven.test.skip=True', shell=True, stdout=subprocess.PIPE)

        for line in pipe.stdout.readlines():
            print(line)

        pipe.wait()
        if pipe.returncode != 0:
            raise PackageFailedException

    def pull(self):
        if os.path.isdir(self.source_path):
            # git pull
            repo = git.Repo(self.source_path)
            repo.remote().pull()
            pass
        else:
            repo = git.Repo.clone_from(self.git_url, self.source_path)
            repo.git.checkout(self.git_branch)
            # git clone
            pass
