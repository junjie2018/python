import paramiko

# 秘钥
ssh = paramiko.SSHClient
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ip", "port", "username", key_filename='私钥')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls -l')
print(stdout.readlines())

sftp = ssh.open_sftp()
sftp.put('monitor.py', 'monitory.py')
sftp.stat('monitor.py')
sftp.rename('monitor.py', 'monitor.txt')
sftp.remove('monitor.txt')
