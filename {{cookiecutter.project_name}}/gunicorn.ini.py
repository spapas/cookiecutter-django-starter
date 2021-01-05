"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():
    return 2 * cpu_count() + 1


# bind = '0.0.0.0:' + environ.get('PORT', '8000')
bind = ["unix:/home/serafeim/{{cookiecutter.project_name}}/gunicorn.sock"]
chdir = "/home/serafeim/{{cookiecutter.project_name}}/{{cookiecutter.project_name}}/"
pidfile = "/home/serafeim/{{cookiecutter.project_name}}/gunicorn.pid"

proc_name = "{{cookiecutter.project_name}}"
# threads = 2
# worker_class = "gthread"
workers = max_workers()

errorlog = "/home/serafeim/{{cookiecutter.project_name}}/logs/gunicorn_error.log"
loglevel = "info"
accesslog = "/home/serafeim/{{cookiecutter.project_name}}/logs/gunicorn_access.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
timeout = 60
capture_output = True

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

def worker_abort(worker):
    worker.log.info("Worker received SIGABRT signal (pid: %s)", worker.pid)
