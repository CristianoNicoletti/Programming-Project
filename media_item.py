import uuid
import json
from enum import Enum


class Category(Enum):
    BOOK = "book"
    FILM = "film"
    MAGAZINE = "magazine"


class MediaItem:
    def __init__(self, name: str, author: str, publication_date: str, category: Category, available_for_borrowing: bool, id: str = None):
        self.id = id if id else str(uuid.uuid4())
        self.name = name
        self.author = author
        self.publication_date = publication_date
        self.category = category
        self.available_for_borrowing = available_for_borrowing

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'publication_date': self.publication_date,
            'category': self.category.value,
            'available_for_borrowing': self.available_for_borrowing
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict):
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
        data = json.loads(json_str)
        return cls.from_dict(data)
