import os

cmd = "uname -a"

returnedValue = os.system(cmd)
print('return: ', returnedValue)