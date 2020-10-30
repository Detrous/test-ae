from flask import Response, jsonify

from . import CACHE, CONFIG, app
from .models import Photo


@app.route("/search/<search_term>")
@CACHE.memoize(CONFIG.get("api.search_cache_time"))
def index(search_term):
    photos = Photo.objects.search_text(search_term)
    if photos.count() != 0:
        return Response(photos.to_json(), content_type="application/json")
    return Response(status=404)
