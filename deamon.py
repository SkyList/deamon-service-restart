import os
import time
import subprocess
import datetime

def checkServiceALive(serviceName):
        cmd = "netstat -putan | grep "+serviceName+" | wc -l"
        while(True):
                os.system("echo "+datetime.datetime.now()+"fetching for "+serviceName+"... >> /root/"+serviceName+".log")
                output = subprocess.check_output(cmd, shell=True)

                if(int(output) == 6):
                        os.system("echo "+datetime.datetime.now()+" "+serviceName +", OK! >> /root/"+serviceName+".log")
                else:
                        os.system("echo "+datetime.datetime.now()+" "+serviceName +", service has problems! >> /root/"+serviceName+".log")
                        os.system("echo "+datetime.datetime.now()+" restarting, "+ serviceName+">> /root/"+serviceName+".log")
                        os.system("systemctl restart "+serviceName)

                time.sleep(10)

checkServiceALive('nginx')