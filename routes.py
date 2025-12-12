
# Defines all Flask API routes for the backend
from flask import jsonify, request
from state import state
from media_item import Category


def register_routes(app):
    """
    Register all API endpoints with the Flask app.
    """
    def _get_category_from_string(category_str: str) -> Category:
        """
        Convert a string to a Category enum (case-insensitive).
        """
        return Category[category_str.upper()]


    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        """
        Health check endpoint to verify backend is running.
        """
        return jsonify({'status': 'healthy'}), 200


    @app.route('/available_media', methods=['GET'])
    def available_media():
        """
        Get all available media items, optionally filtered by category.
        Only returns items available for borrowing.
        """
        category = request.args.get('category')
        if category:
            cat = _get_category_from_string(category)
            media = state.get_media_by_category(cat)
        else:
            media = state.get_all_media()
        # Only return available items
        available_media = [m for m in media if m.get('available_for_borrowing')]
        return jsonify({'media': available_media}), 200


    @app.route('/add_media', methods=['POST'])
    def add_media():
        """
        Add a new media item to the library.
        Expects JSON with name, author, publication_date, category, and available_for_borrowing.
        """
        data = request.json
        category = _get_category_from_string(data.get('category'))
        media = state.add_media(
            name=data.get('name'),
            author=data.get('author'),
            publication_date=data.get('publication_date'),
            category=category,
            available_for_borrowing=data.get('available_for_borrowing', False)
        )
        return jsonify({'message': 'Media added', 'media': media.to_dict()}), 201


    @app.route('/search', methods=['GET'])
    def search():
        """
        Search for media items by name (case-insensitive substring match).
        """
        name = request.args.get('name', '')
        results = state.search_media(name)
        return jsonify({'results': results}), 200


    @app.route('/delete_media', methods=['DELETE'])
    def delete_media():
        """
        Delete a media item by its ID. Expects JSON with 'id'.
        """
        data = request.json
        media_id = data.get('id')
        if state.delete_media(media_id):
            return jsonify({'message': 'Media deleted'}), 200
        return jsonify({'message': 'Media not found'}), 404
