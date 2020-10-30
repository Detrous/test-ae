from . import CELERY, app


@CELERY.task()
def fetch_photos():
    app.logger.info("Fetching photos...")
