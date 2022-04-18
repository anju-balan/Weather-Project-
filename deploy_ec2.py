import paramiko
import sys

hostname = 'ec2-3-14-146-73.us-east-2.compute.amazonaws.com' 
myuser   = 'ubuntu'
mySSHK   = 'C:/Users/karth/My_Git/AIML_Term3/AL and ML Lab - Copy/term3-capstone-project/capstone-project/Dataminds.pem'
sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error
sshcon.connect(hostname, username=myuser, key_filename=mySSHK) # no passwd needed
stdin, stdout, stderr = sshcon.exec_command('/home/ubuntu/Weather-Project-/deploy.sh')
sys.exit()
print(stdout.readlines())
sshcon.close()