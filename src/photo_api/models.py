from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, FileField, StringField


class PhotoMetadata(EmbeddedDocument):
    author = StringField()
    camera = StringField()
    tags = StringField()


class Photo(Document):
    photo_id = StringField()
    cropped_picture = StringField()
    full_picture = StringField()
    metadata = EmbeddedDocumentField(PhotoMetadata)

    meta = {
        "indexes": [
            {
                "fields": ["$metadata.author", "$metadata.camera", "$metadata.tags"],
                "default_language": "english",
            }
        ]
    }
