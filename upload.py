import os
import sys
 
path = os.getcwd()
fileName = sys.argv[1]
filePath = os.path.join(path,fileName)
remotePath = sys.argv[2]
command = "scp {0} pravesh@172.26.1.208:{1}".format(filePath, remotePath)
print (command)
os.system(command)
 