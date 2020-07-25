# Simple IoT Monitor
A simple webserver for receiving data from sensors in a local network and displaying them in a website. 
It is meant to be used by hobbyists and students in a local network. 
It is not meant to be deployed on the Internet, due to security concerns.

## How to use
*NOTICE: it is not recommended to deploy this system to the Internet. Use it only on a
 local network*
 
You need to have [python 3](https://www.python.org/) installed.

- To use the system just on your computer, run:
    - python manage.py runserver
- To register things and sensors, access http://localhost:8000/iotmonitor on a browser
and click on the Admin button
  - the default login is
     - login: admin
     - password: ukJX^jhFo:re%?ZG.De#
   - remember to change your password after login
 - To make the system accessible to other devices, you need to 
   - edit the settings file in 
 iotproject/iotproject
     - search for ALLOWED_HOSTS and add your ip address
       - example: ALLOWED_HOSTS = ['localhost', '192.168.1.4']
   - run the system:
     - python manage.py runserver YOUR_IP:8000
       - example: manage.py runserver 192.168.1.4:8000
   - then you can access the system through
     - YOUR_IP:8000/iotmonitor
       - example:  http://192.168.1.4:8000/iotmonitor
 - *NOTICE: it is not recommended to deploy this system to the Internet. Use it only on a
 local network*

## User requirements



## Contributors
We would love to receive your pull request! All contributors will be listed here, chronologically:
- [João Pimentel](https://github.com/jhcp)
- [José Otávio](https://github.com/otavio-maciel)
- [Davi Melo](https://github.com/DaviMelo558)
