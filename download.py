
import os
import sys
import time
 
path = os.getcwd()
remoteFilePath = sys.argv[1]
localPath = sys.argv[2]
command = "scp pravesh@172.26.1.208:{0} {1}".format(remoteFilePath, localPath)
 
print (remoteFilePath, command)
 
os.system(command)
