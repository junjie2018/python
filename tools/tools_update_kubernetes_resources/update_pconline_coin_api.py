#!/usr/bin/python3

import subprocess

# 得到版本
get_api_destination_rule_version_command = \
    "kubectl get dr pconline-coin-api -n kube-pconline -o=jsonpath='{.spec.subsets[0].labels.version}'"

update_api_virtual_servicon_subset_command = \
    """kubectl patch vs pconline-coin --type='json' -n kube-pconline -p '[{{"op":"replace","path":"/spec/http/input/route/0/destination/subset","value":"{version}"}}]'"""

delete_api_destination_rule_version_command = \
    "kubectl delete dr pconline-admin-api -n kube-pconline"

print('####################### 执行的指令 #######################')
print(get_api_destination_rule_version_command)
print(update_api_virtual_servicon_subset_command.format(version="version1"))
print(delete_api_destination_rule_version_command)

print('####################### 执行结果及异常 #######################')
cur_version = subprocess.check_output(get_api_destination_rule_version_command, shell=True)
subprocess.check_call(update_api_virtual_servicon_subset_command.format(cur_version))
subprocess.check_call(delete_api_destination_rule_version_command)
