#!/usr/bin/python3

import deploy_config
import os
import git
import shutil

service_name = 'online-bb-member'
# source_path = r"C:\Users\Junjie\Desktop\source"
source_path = "/home/mmpprd/source"
project_source_path = os.path.join(source_path, service_name)

services = deploy_config.services
service = services[service_name]
# os.removedirs(project_source_path)
shutil.rmtree(project_source_path, ignore_errors=True)
repo = git.Repo.clone_from(service.git_config.git_url, project_source_path)
repo.git.checkout('develop')
# print(repo.git.branch('-r'))

# service = services['online-bb-member']

#
# print("")
