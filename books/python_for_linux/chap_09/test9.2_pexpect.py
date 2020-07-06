import pexpect

child = pexpect.spawn('scp your_file user@host')
child.expect('Password:')
child.sendline('your_password')
