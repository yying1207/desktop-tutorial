import paramiko
import os

password = os.environ.get('PASS') # 'export PASS=abc123' in terminal before running the script
key = paramiko.RSAKey.from_private_key_file("~/.ssh/id_rsa") # Load the private key from the specified file path

# Create an ssh client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add the host key
ssh.connect(hostname='34.222.179.99', username='centos', password=password) # Connect to the server using the password
ssh.connect(hostname='34.222.179.99', username='centos', pkey=key) # Connect to the server using the private key
ssh.connect(hostname='34.222.179.99', username='ec2-user ', key_filename='/home/yy/key.em') # Cloud server with key pair authentication
stdin, stdout, stderr = ssh.exec_command("free -m")

# stdin: standard input
# stdout: standard output
# stderr: standard error

print(stdout.readlines())


ftp_client = ssh.open_sftp()
ftp_client.put("tempfile", "tempfile") #upload tempfile
ftp_client.get("tempfile", "/tmp/tempfile") #download tempfile
ftp_client.close()

ssh.close()
