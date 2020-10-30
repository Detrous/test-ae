from photo_api.tasks import fetch_photos


def on_starting(server):
    fetch_photos()


bind = "127.0.0.1:8080"

workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
