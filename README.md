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
You must setup a cronjob in order to scan the network periodically to know who is actually connected. The default delay is 10 minutes but this value can be changed in the [main settings file](./WhoIsHere/settings.py).
```bash
sudo python3 manage.py crontab add
```
The cronjob should also be deleted when you no longer want to use the application with:
```bash
sudo python3 manage.py crontab remove
```
**Import Note:** The cronjob must be added as sudo user in order to enable the lookup of the MAC Addresses. If you don't want to make the script run as sudo user, the application will still works but will be limited to IP Addresses.

### Launch the server
```shell
python3 manage.py runserver 0.0.0.0:8000
```

### Fill the database
Before being effective, you must first add peoples to track. First off go to the admin section of the website and connect with the credentials created earlier.

Adding peoples / MAC Addresses / IP Addresses is relatively straightforward even if you don't know Django. But if you want to know more, just look around on the internet, there are plenty of easy tutorials.
