#!/usr/bin/env python
# import built-in os library
# https://docs.python.org/3/library/os.html

import os

# Open file for saving ping results
results_file = open("results.txt", "w")

# Empty list to store ip addresses
ip_list = []

# Loop from 1 to 255
# Appends the concatenated ip to the ip_list
for ip in range(1, 256):
    ip_list.append("192.168.1." + str(ip))

# Print ip_list
print(f'{ip_list}')

# Print number of ip addresses in list
print(len(ip_list))

# Loop to ping ip_list and check if device up or down
# Outputs to results.txt file
for ip in ip_list:
    response = os.popen(f"ping {ip} -c 1").read()  # this is to get output of ping and save it on a variable
    if "1 packets transmitted, 1 packets received, 0.0% packet loss" in response:
        print(f"UP {ip} Ping Successful")
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        print(f"Down {ip} Ping Unsuccessful")
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
results_file.close()
