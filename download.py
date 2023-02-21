
import os
import sys
import time
 
path = os.getcwd()
remoteFilePath = sys.argv[1]
localPath = sys.argv[2]
command = ""
opt = input()
if opt == '.':
    command = "scp pravesh@172.30.2.243:{0} {1}".format(remoteFilePath, localPath)
else:
    command = "scp pravesh@172.26.1.208:{0} {1}".format(remoteFilePath, localPath) #original
 
print (remoteFilePath, command)
 
os.system(command)
