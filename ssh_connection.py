import paramiko

command = "ls"


host = "host"
username = "user"
password = "password"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command(command)
    print(_stdout.read().decode())
    client.close()


except paramiko.ssh_exception.NoValidConnectionsError:
    print("Unable to connect to port 22 on " + host)


except:
    print("Error")

