# WSGI_custom
custom WSGI framework

## Installation

Use Python3.7

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
gunicorn app:app
```

Output example:
```bash
[2019-08-15 20:23:17 +0300] [24575] [INFO] Starting gunicorn 19.9.0
[2019-08-15 20:23:17 +0300] [24575] [INFO] Listening at: http://127.0.0.1:8000 (24575)
[2019-08-15 20:23:17 +0300] [24575] [INFO] Using worker: sync
[2019-08-15 20:23:17 +0300] [24578] [INFO] Booting worker with pid: 24578
```

After starting the server, you need to open a browser.

You have 3 pages available:

* http://127.0.0.1:8000/
* http://127.0.0.1:8000/home
* http://127.0.0.1:8000/about