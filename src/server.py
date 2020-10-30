import logging

from photo_api import CONFIG, app, routes
from photo_api.tasks import fetch_photos

if __name__ == "__main__":
    fetch_photos.delay()
    app.run("127.0.0.1", port=9999, debug=True)
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
