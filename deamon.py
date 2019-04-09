import os

cmd = "netstat -putan | grep nginx | wc -l"

returnedValue = os.system(cmd)
print('return: ', returnedValue)