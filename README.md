# WhoIsHere


## Installation

### Install dependencies
```bash
pipenv install
pipenv shell
```

### Configure database
```bash
python3 manage.py migrate
```

### Create superuser
```bash
python3 manage.py createsuperuser
```

### Create cronjob
In order to track the people that are logged to the network we need to run a cron job that by default is executed every 10 minutes. To create this cron job, you have to type the following command:
```bash
sudo crontab ./home/cron/cron_command.txt
```

**Import Note:** The cronjob must be added as sudo user in order to send raw ARP packets and sniff for results.

### Launch the server
```shell
python3 manage.py runserver 0.0.0.0:8000
```

### Fill the database
Before being effective, you must first add peoples to track. First off, go to the admin section of the website and connect with the credentials created earlier.

Adding peoples / MAC Addresses is relatively straightforward even if you don't know Django. But if you want to know more, just look around on the internet, there are plenty of easy tutorials.


## How does it work ?
The application is relatively easy to understand. The idea is just to scan the LAN network to see who is connected, this gives us an idea of how is currently at the kot. In order to scan the network, we use arp-scan utility to send raw ARP packets and sniff for results. We are using ARP packets as we are not guaranteed that all host responds to ICMP packets.
