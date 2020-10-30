from photo_api import CONFIG
from photo_api.tasks import fetch_photos


def on_starting(server):
    fetch_photos.delay()


bind = "127.0.0.1:8080"

workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 30

loglevel = CONFIG.get("api.log_lvl")
