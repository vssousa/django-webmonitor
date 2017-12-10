# Django Web Monitor

## Overview

This repository presents a web application using Django framework for monitoring webpage accesses in external websites. 

## Software requirements

The following softwares have to be configured / installed for running this application.

1. [Django framework](https://www.djangoproject.com/) for providing web services.
2. [Python 2.7](https://www.python.org/) as the main programming language.
3. [pip](https://pypi.python.org/pypi/pip), the PyPA recommended tool for installing Python packages.
4. [VirtualEnv](https://virtualenv.pypa.io/en/stable/) for creating a Python environment with all (library) dependencies.
5. [SQLite](https://www.sqlite.org/) as the relational database management system.
6. [Bootstrap](http://getbootstrap.com/) as the template of web pages.

## How to configure

To configure a local environment, it is necessary to install Python and VirtualEnv softwares, as aforementioned. Then, virtual environment can be configured according to a environment configuration file, named as 'requirements.txt', as follows:

``` 
virtualenv env
source env/bin/activate
pip install -r requirements.txt
``` 

## How to start our projects

We basically have two projects, one for monitoring webpage accesses, named as `web_monitor`, and another for notifying webpage accesses to the web_monitor project, named as `app`. To start these projects in a local environment, it is necessary to run a Django server for each project (using different ports), as follows:

```
cd $ROOT_DIRECTORY
cd web_monitor
python manage.py runserver 5000 &
cd ../app
python manage.py runserver &
```

## Available URLs in these projects

### Web monitor (web_monitor)

The folllowing URLs are available in this project, that access:

* Contact list as our home page

```
http://$HOSTNAME:$PORT/
```

* List of webpages accessed by a specific contact. It can be accessed by links in the contact items from the home page.

```
http://$HOSTNAME:$PORT/pages/<contact_id>
```

P.S.: $HOSTNAME should be replaced by the hostname or IP address, **e.g.**, localhost; and $PORT should be replaced by the configured port in Django project, **e.g.**, 5000.

### External application (app)

The folllowing URLs are available in this project, that access:

* Home page to the external application

```
http://$HOSTNAME:$PORT/<update>
```

* Contact form to register a contact in the app web_monitor.

```
http://$HOSTNAME:$PORT/contact/<update>
```

* About page

```
http://$HOSTNAME:$PORT/about/<update>
```

* Price page

```
http://$HOSTNAME:$PORT/price/<update>
```

P.S.: We added an update parameter in our URL to trigger our JavaScript, *i.e.*, to send HTTP requests to the app web_monitor.
