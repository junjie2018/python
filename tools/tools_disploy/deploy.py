#!/usr/bin/python3
import deploy_config
from deployments import Deployments
import glob
import os
import git
import subprocess
import paramiko

# def send_jar_to_target(service_name, source_root, target_path, target_ip, machine_user, machine_password):
#     source_path = os.path.join(source_root, service_name)
#     jar_path = os.path.join(source_path, target_path)
#
#     os.chdir(jar_path)
#     jars = glob.glob('*.jar')
#     if len(jars) == 0:
#         raise NoJarException('no jar in target path.')
#
#     jar_file_path = os.path.join(jar_path, jars[0])
#     print(jar_file_path)
#     send_file(target_ip, machine_user, machine_password, jar_file_path, "/home/mmpprd/tmp/temp.jar")


if __name__ == '__main__':
    service_name = 'online-bb-member'
    source_root = '/home/mmpprd/source'
    service = deploy_config.services[service_name]

    deployments = Deployments(source_root, service)
    deployments.pull()
    # deployments.package()
