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
        self.transport = paramiko.Transport(ip)
        self.transport.connect(username=machine_user, password=machine_password)

    def mkdir_p(self, relative_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        if relative_path == '/':
            sftp.chdir('.')
        if relative_path == '':
            return
        try:
            sftp.chdir(relative_path)
        except IOError:
            dirname, basename = os.path.split(relative_path.rstrip('/'))
            mkdir_p(sftp)

    def send_file(self, source_file, target_file):
        sftp.mkdir()
        print(source_file)
        print(target_file)
        sftp.put(source_file, target_file)

        # todo 这个地方需要关闭么


class Deployment:
    def __init__(self, source_root, service, target_config):
        self.service_name = service.service_name
        self.source_root = source_root
        self.source_dir = os.path.join(source_root, service.service_name)

        # jar包放在该目录下
        self.jar_path = os.path.join(self.source_dir, target_config.jar_path)

        self.target_port = target_config.port  # 8000
        self.target_home = os.path.join('/home', target_config.machine_user)  # /home/mmpprd
        self.deploy_dir = os.path.join(self.target_home, 'deploy')  # /home/deploy
        self.target_dir_name = '%s_%s' % (self.service_name, self.target_port)  # online-bb-member_8000
        self.target_dir = os.path.join(self.deploy_dir, self.target_dir_name)  # /home/deploy/online-bb-member_8000


        self.target_deploy_path = os.path.join(self.target_home, 'deploy')  # /home/mmpprd/deploy
        self.target_deploy_path = os.path.join(self.target_home, 'deploy')  # /home/mmpprd/deploy
        self.target_deploy_dir = os.path.join(
            self.target_home,
            'deploy',
            '%s_%s' % (self.service_name, self.target_port))

        jars = glob.glob(os.path.join(self.source_dir, service.git_config.jar_path, '*.jar'))
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
        print(self.target_deploy_dir)

        if not os.path.isfile(self.jar_path):
            raise NoJarException('Jar Not Exist.')
        self.transportUtil.send_file(self.jar_path, self.target_deploy_dir)
        pass

    def deploy(self):
        pass

    def kill(self):
        pass


class Deployments:
    def __init__(self, source_root, service):
        self.service_name = service.service_name
        self.source_root = source_root
        self.source_dir = os.path.join(source_root, service.service_name)

        self.git_url = service.git_config.git_url
        self.git_branch = service.git_config.git_branch

        self.deployments = []

        for target_config in service.targets_config:
            self.deployments.append(Deployment(source_root, service, target_config))

    def package(self):
        if not os.path.isdir(self.source_dir):
            raise NoKeyPathException("source_dir not exist.")
        os.chdir(self.source_dir)
        pipe = subprocess.Popen('mvn package -D maven.test.skip=True', shell=True, stdout=subprocess.PIPE)

        for line in pipe.stdout.readlines():
            print(line)

        pipe.wait()
        if pipe.returncode != 0:
            raise PackageFailedException

    def pull(self):
        if os.path.isdir(self.source_dir):
            # git pull
            repo = git.Repo(self.source_dir)
            repo.remote().pull()
            pass
        else:
            repo = git.Repo.clone_from(self.git_url, self.source_dir)
            repo.git.checkout(self.git_branch)
            # git clone
            pass
