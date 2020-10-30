echo "Running server..."
gunicorn -c python:photo_api.wsgi server:app