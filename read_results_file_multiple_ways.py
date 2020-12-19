import os

# read file located in the run path directory
results_file = open("results.txt", "r")

# text1 = results_file.read()
# print(results_file.read())  # Note that you can only read the file once since read() leaves the cursor \
# at end of the line

# try this code you will see what i mean where it read first 5 characters then the cursor stops there
# and it will continue there for reading the next two lines
# print('this is a separator')
#
# print(results_file.read(5))  # this is to read first 5 characters
#
# print(results_file.readline())
# print(results_file.readline())

# This is trick to bring back read cursor to 0 so you can re-read the file again
# print(results_file.read())
# results_file.seek(0)
# print('this is a separator again')
# print(results_file.read(5))
# #####

# readline(4) is same as read(4) where it only reads 4 characters
# print(results_file.readline(4))
#results_file.seek(0)
# print(results_file.readline(4))

# This is to read the file and save each line in the lists
# print(results_file.readlines())
# #####

# This is read each character of the file
# text1 = results_file.read()
# for x in text1:
#     print(x)

# This is read each line of the file as per list elements
# text1 = results_file.readlines()
# for x in text1:
#     print(x)

# This is read each line of the file as per list elements and then check if 'UP' is in the element then starts counting
text1 = results_file.readlines()
UP_counter = 0
for x in text1:
    # print(x)
    if 'UP' in x:
        UP_counter += 1
        print(f'UP_counter value is {UP_counter}')

results_file.close()

'''
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
    response = os.popen(f"ping {ip} -c 1").read()
    if "1 packets transmitted, 1 packets received, 0.0% packet loss" in response:
        print(f"UP {ip} Ping Successful")
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        print(f"Down {ip} Ping Unsuccessful")
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
results_file.close()

'''