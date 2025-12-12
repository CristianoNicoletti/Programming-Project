
# Handles persistent state management for media items in the library system
import json
from typing import Dict, Optional
from media_item import MediaItem, Category



class State:
    # File where the state is persisted
    STATE_FILE = 'state.json'

    def __init__(self):
        # Dictionary mapping media IDs to MediaItem objects
        self.media: Dict[str, MediaItem] = {}
        self.load_from_file()

    def add_media(self, name: str, author: str, publication_date: str, category: Category, available_for_borrowing: bool) -> MediaItem:
        """
        Add a new media item to the state and persist the change.
        Returns the created MediaItem.
        """
        media = MediaItem(name, author, publication_date, category, available_for_borrowing)
        self.media[media.id] = media
        self.save_to_file()
        return media

    def get_media(self, media_id: str) -> Optional[MediaItem]:
        """
        Retrieve a media item by its ID.
        Returns the MediaItem or None if not found.
        """
        return self.media.get(media_id)

    def delete_media(self, media_id: str) -> bool:
        """
        Delete a media item by its ID.
        Returns True if deleted, False if not found.
        """
        if media_id in self.media:
            del self.media[media_id]
            self.save_to_file()
            return True
        return False

    def get_all_media(self) -> list:
        """
        Get a list of all media items as dictionaries.
        """
        return [media.to_dict() for media in self.media.values()]

    def get_media_by_category(self, category: Category) -> list:
        """
        Get all media items in a specific category as dictionaries.
        """
        return [media.to_dict() for media in self.media.values() if media.category == category]

    def search_media(self, name: str) -> list:
        """
        Search for media items by name (case-insensitive substring match).
        Returns a list of matching media as dictionaries.
        """
        return [media.to_dict() for media in self.media.values() if name.lower() in media.name.lower()]

    def save_to_file(self):
        """
        Save the current state to the state file in JSON format.
        """
        data = {media_id: media.to_dict() for media_id, media in self.media.items()}
        with open(self.STATE_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self):
        """
        Load the state from the state file, or create it if it doesn't exist.
        """
        try:
            with open(self.STATE_FILE, 'r') as f:
                data = json.load(f)
                for media_id, media_data in data.items():
                    media = MediaItem.from_dict(media_data)
                    self.media[media.id] = media
        except FileNotFoundError:
            # If the file doesn't exist, create it with the current (empty) state
            self.save_to_file()


# Global state instance for use throughout the application
state = State()
