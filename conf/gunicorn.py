proc_name = "gunicorn"
bind = "127.0.0.1:5000"
backlog = 128
worker_class = 'meinheld.gmeinheld.MeinheldWorker'
worker_connections = 5

daemon = True
pidfile = "/var/run/gunicorn.pid"
umask = 0
user = None
group = None
tmp_upload_dir = None

errorlog = '/var/log/gunicorn/error.log'
loglevel = 'info'
accesslog = '/var/log/gunicorn/access.log'

workers = 4
worker_class = 'sync'
worker_connections = 1000
max_requests = 0
timeout = 60
keepalive = 2
debug = False
spew = False
