import requests

from . import app


class InterviewAPI:
    host = "http://interview.agileengine.com"
    __token: str
    __api_key: str

    def __init__(self, api_key):
        self.__api_key = api_key
        self.__obtain_token()

    def fetch_photos_with_metadata(self):
        """Returns the photos with metadata

        Returns:
                photos ([dict]): List of dicts with information about each photo
        """
        photo_ids = self.fetch_photo_ids()
        photos = []
        for photo_id in photo_ids:
            photos.append(self.fetch_photo_metadata(photo_id))
        return photos

    def fetch_photo_metadata(self, photo_id):
        """Returns the photo metada

        Parameters:
                photo_id (str): The photo id

        Returns:
                photo_data (dict): Dict with information about photo
        """
        url = self.host + f"/images/{photo_id}"
        return self.__call_api("get", url)

    def fetch_photo_ids(self):
        """Returns the list of photo ids

        Returns:
                photo_ids ([str]): The list of photo ids
        """
        photo_ids = []

        has_more = True
        page_id = 1
        url = self.host + "/images"

        while has_more:
            data = self.__call_api("get", url, params={"page": page_id})
            photo_ids.extend([picture["id"] for picture in data["pictures"]])
            page_id += 1
            has_more = data["hasMore"]
        return photo_ids

    def __obtain_token(self):
        """Obtains token for API

        raises:
            Exception: When can't obtain token
        """
        url = self.host + "/auth"
        response = requests.post(url, json={"apiKey": self.__api_key})
        data = response.json()
        if response.status_code == 401 or not data["auth"]:
            raise Exception("I can't get a token!")
        self.__token = data["token"]

    def __call_api(self, method, url, params=None, json=None):
        """Makes a request to the API with specified parameters

        Parameters:
                method (str): A request method
                url (str): An url
                params (dict): GET parameters
                json (dict): POST json parameters

        Returns:
                data (dict): Response from API

        raises:
            Exception: When can't obtain token (from __obtain_token)
        """
        headers = {"Authorization": "Bearer " + self.__token}
        response = getattr(requests, method)(url, params=params, json=json, headers=headers)
        if response.status_code == 401:
            self.__obtain_token()
            return self.__call_api(method, url, params, json)
        return response.json()
