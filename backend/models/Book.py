import os
import requests
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

# Book resource
class Book:

    # Constructor
    def __init__(self, ISBN, title, edition, publisher) -> None:
        self.ISBN = ISBN
        self.title = title
        self.edition = edition
        self.publisher = publisher
        self.topics = self.get_topics()

    # Construct topics list
    def get_topics(self):
        try:
            # Google Books API url
            request_url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{int(self.ISBN)}&key={API_KEY}'

            # Make a request to the API
            response = requests.get(request_url)
            response_json = response.json()

            # Check if the request was successful
            if response.status_code == 200:
                # Append categories to topics list
                volume_list = response_json.get('items', [])
                if volume_list:
                    volume = volume_list[0].get('volumeInfo', {})
                    categories = volume.get('categories', [])
                    return categories
                else:
                    return []
            else:
                raise Exception('Unsuccessful category retrieval')

        except Exception as e:
            return []

    # Custom print function
    def __str__(self):
        return "ISBN: " + str(int(self.ISBN)) + " Title: " + self.title + " Edition: " + self.edition + " Publisher: " + self.publisher + " Categories: " + str(self.topics)