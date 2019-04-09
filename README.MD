# Deamon for keep alive services


## instalação step by step

* Donwload repository 
* move `mydeamon.service` to `/etc/systemd/system`
* move  `deamon.py` to `/root`
* start service 
  
### Moving archives
``` shell
$mv mydeamon.service /etc/systemd/system
$mv deamon.py /root
```

Starting service 

``` shell
$systemctl start mydeamon
`

