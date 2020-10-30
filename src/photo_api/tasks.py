from . import CELERY, CONFIG, app
from .interview_api import InterviewAPI
from .models import Photo, PhotoMetadata


@CELERY.task()
def fetch_photos():
    app.logger.info("Fetching photos...")
    api = InterviewAPI(CONFIG.get("api.interview_api_key"))
    # Retrieves photos from API
    photos = api.fetch_photos_with_metadata()

    # Removes objects that doesn't present in the API
    Photo.objects(photo_id__not__in=[photo["id"] for photo in photos]).delete()

    # Creates or updates photos
    for photo in photos:
        Photo.objects(photo_id=photo["id"]).update_one(
            photo_id=photo.pop("id"),
            cropped_picture=photo.pop("cropped_picture"),
            full_picture=photo.pop("full_picture"),
            metadata=PhotoMetadata(**photo),
            upsert=True,
        )
