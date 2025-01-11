# if you want to run gunicorn with this config file, you can use the following command:
# gunicorn -c gunicorn_cf.py app:app

bind = "0.0.0.0:5000"
workers = 4
worker_connections = 2000
backlog = 2048
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
timeout = 600
debug=False
capture_output = True
worker_class = 'gevent'

