import os
import subprocess


hostnames = [
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3',
    '192.168.1.1'
]

# for hostname in hostnames:
#     response = os.system('ping -c 1 ' + hostname)
#     # Note that os.system will only return the exit code but will not give output of ping
#     print(f'response value is {response}')
#     if response == 0:
#         print(f'{hostname} is up')
#     else:
#         print(f'{hostname} is down')

for hostname in hostnames:
    try:
        cmd = "ls"
        # cmd = "date"
        print(cmd)
        # returns output as byte string
        returned_output = subprocess.check_output(["ping", "-c", "1", hostname])
        print(f"returned_output is {returned_output}")
    except subprocess.CalledProcessError:
        print(f'Ping failed on {hostname}')

