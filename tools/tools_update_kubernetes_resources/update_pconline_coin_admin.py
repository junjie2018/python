#!/usr/bin/python3

import subprocess

# 得到版本
get_admin_destination_rule_version_command = \
    "kubectl get dr pconline-coin-admin -n kube-pconline -o=jsonpath='{.spec.subsets[0].labels.version}'"

update_admin_virtual_servicon_subset_command = \
    """kubectl patch vs pconline-coin --type='json' -n kube-pconline -p '[{{"op":"replace","path":"/spec/http/0/route/0/destination/subset","value":"{version}"}}]'"""

delete_admin_destination_rule_version_command = \
    "kubectl delete dr pconline-admin-admin -n kube-pconline"

print('####################### 执行的指令 #######################')
print(get_admin_destination_rule_version_command)
print(update_admin_virtual_servicon_subset_command.format(version="version1"))
print(delete_admin_destination_rule_version_command)

print('####################### 执行结果及异常 #######################')
cur_version = subprocess.check_output(get_admin_destination_rule_version_command, shell=True)
subprocess.check_call(update_admin_virtual_servicon_subset_command.format(cur_version))
subprocess.check_call(delete_admin_destination_rule_version_command)
