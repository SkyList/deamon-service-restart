import os
import time
import subprocess

def checkServiceALive(serviceName):
        cmd = "netstat -putan | grep "+serviceName+" | wc -l"
        while(True):
                os.system("echo fetching for "+serviceName+"... >> "+serviceName+".log")
                output = subprocess.check_output(cmd, shell=True)

                if(int(output) == 6):
                        os.system("echo "+serviceName +", OK! >>"+serviceName+".log")
                else:
                        os.system("echo "+serviceName +", service has problems! >> "+serviceName+".log")
                        os.system("echo restarting, "+ serviceName+">> "+serviceName+".log")
                        os.system("systemctl restart "+serviceName)

                time.sleep(10)


checkServiceALive('nginx')