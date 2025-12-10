import json
from typing import Dict, Optional
from media_item import MediaItem, Category


class State:
    STATE_FILE = 'state.json'

    def __init__(self):
        self.media: Dict[str, MediaItem] = {}
        self.load_from_file()

    def add_media(self, name: str, author: str, publication_date: str, category: Category, available_for_borrowing: bool) -> MediaItem:
        media = MediaItem(name, author, publication_date, category, available_for_borrowing)
        self.media[media.id] = media
        self.save_to_file()
        return media

    def get_media(self, media_id: str) -> Optional[MediaItem]:
        return self.media.get(media_id)

    def delete_media(self, media_id: str) -> bool:
        if media_id in self.media:
            del self.media[media_id]
            self.save_to_file()
            return True
        return False

    def get_all_media(self) -> list:
        return [media.to_dict() for media in self.media.values()]

    def get_media_by_category(self, category: Category) -> list:
        return [media.to_dict() for media in self.media.values() if media.category == category]

    def search_media(self, name: str) -> list:
        return [media.to_dict() for media in self.media.values() if name.lower() in media.name.lower()]

    def save_to_file(self):
        data = {media_id: media.to_dict() for media_id, media in self.media.items()}
        with open(self.STATE_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self):
        try:
            with open(self.STATE_FILE, 'r') as f:
                data = json.load(f)
                for media_id, media_data in data.items():
                    media = MediaItem.from_dict(media_data)
                    self.media[media.id] = media
        except FileNotFoundError:
            self.save_to_file()

# Global state instance
state = State()
