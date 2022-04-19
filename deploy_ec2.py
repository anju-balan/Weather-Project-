import paramiko
import sys
import time 

hostname = 'ec2-3-14-146-73.us-east-2.compute.amazonaws.com' 
myuser   = 'ubuntu'
mySSHK   = 'Dataminds.pem'
sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error
sshcon.connect(hostname, username=myuser, key_filename=mySSHK) # no passwd needed

stdin, stdout, stderr = sshcon.exec_command('/home/ubuntu/weather/Weather_Project/deploy.sh')

#stdin, stdout, stderr = sshcon.exec_command('/home/ubuntu/Weather-Project-/deploy.sh')
time.sleep(10)
sys.exit(0)
print(stdout.readlines())
sshcon.close()


