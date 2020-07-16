#
#
#
#
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('120.78.168.136', 22, 'root', 'PC+1111222', timeout=10)
# stdin, stdout, stderr = ssh.exec_command("ls")
# print(stdout.read())