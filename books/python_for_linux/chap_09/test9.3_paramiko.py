import paramiko

# 密码
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ip", "port", "username", "password")

# 秘钥
ssh = paramiko.SSHClient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ip", "port", "username", key_filename='私钥')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.readlines())
