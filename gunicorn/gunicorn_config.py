import multiprocessing
BASE_PATH = '/opt/supervisor_demo'
bind = "127.0.0.1:8001"
workers = multiprocessing.cpu_count()

max_requests = 5000

user = 'duoduo'
group = 'duoduo'

accesslog = BASE_PATH + '/gunicorn/log/gunicorn_access.log'
errorlog = BASE_PATH + '/gunicorn/log/gunicorn_error.log'
chdir = BASE_PATH + '/supervisor_django'
