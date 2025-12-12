
# Defines the MediaItem class and Category enum for library items
import uuid
import json
from enum import Enum



# Enum for media categories
class Category(Enum):
    BOOK = "book"
    FILM = "film"
    MAGAZINE = "magazine"



# Represents a single media item (book, film, magazine, etc.)
class MediaItem:
    def __init__(self, name: str, author: str, publication_date: str, category: Category, available_for_borrowing: bool, id: str = None):
        """
        Initialize a MediaItem. If id is not provided, generate a new UUID.
        """
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.author = author
        self.publication_date = publication_date
        self.category = category
        self.available_for_borrowing = available_for_borrowing


    def to_dict(self):
        """
        Convert the MediaItem to a dictionary for serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'publication_date': self.publication_date,
            'category': self.category.value,
            'available_for_borrowing': self.available_for_borrowing
        }


    def to_json(self):
        """
        Convert the MediaItem to a JSON string.
        """
        return json.dumps(self.to_dict())


    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a MediaItem from a dictionary (typically loaded from JSON).
        """
        return cls(
            name=data['name'],
            author=data['author'],
            publication_date=data['publication_date'],
            category=Category(data['category']),
            available_for_borrowing=data['available_for_borrowing'],
            id=data.get('id')
        )


    @classmethod
    def from_json(cls, json_str: str):
        """
        Create a MediaItem from a JSON string.
        """
        data = json.loads(json_str)
        return cls.from_dict(data)
