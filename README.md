# Fastapi based web application

Updated: 06-07-2023


## Overview

A Light weight simple web app


## Requirement

See requirements.txt for updates.

```sh
aiofiles==0.8.0
fastapi==0.89.1
Jinja2==3.1.2
python-dotenv==0.21.1
python-multipart==0.0.5
requests==2.27.1
uvicorn==0.20.0
Markdown==3.3.6
pytest==6.2.5
```

## Installation & Usage

```bash
-# Setup locally
-* git git@github.com:ashutoshnjha/container-templates.git
-* cd container-templates
-* Make sure python configured is 3.10 or use virtualenv to enable python3.10
-* e.g. I use virtualenv and enable it by executing,$ source ./pyvenv/py310/bin/activate
-* Run pip install -r requirements.txt to have dependent modules
-* Execute uvicorn to start the application on port 8000
-  * $ uvicorn app.main:app --reload --port 8000
-  * Since we have the main.py in app/main.py therefore we used uvicorn app.main:app
```
Visit [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

## Docker based
https://github.com/ashutoshnjha/container-templates.git
docker build -t fastapi-tpl .
docker run -d --name anj-tpl -p 5000:5000 fastapi-tpl

## Features

- Docker template generation
- Kuberservice template generation

## Test

All tests are under `tests` directory.

```bash
# Go to repo directory
$ cd container-templates
# Execute pytest command
$ pytest -v
```

## Author

[linkedIn](https://www.linkedin.com/in/ashutoshnarayanjha/)

## Licence


