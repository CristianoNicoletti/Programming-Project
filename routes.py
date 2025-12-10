from flask import jsonify, request
from state import state
from media_item import Category

def register_routes(app):
    def _get_category_from_string(category_str: str) -> Category:
        return Category[category_str.upper()]

    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        return jsonify({'status': 'healthy'}), 200

    @app.route('/available_media', methods=['GET'])
    def available_media():
        category = request.args.get('category')
        if category:
            cat = _get_category_from_string(category)
            media = state.get_media_by_category(cat)
        else:
            media = state.get_all_media()
        return jsonify({'media': media}), 200

    @app.route('/add_media', methods=['POST'])
    def add_media():
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
        name = request.args.get('name', '')
        results = state.search_media(name)
        return jsonify({'results': results}), 200

    @app.route('/delete_media', methods=['DELETE'])
    def delete_media():
        data = request.json
        media_id = data.get('id')
        if state.delete_media(media_id):
            return jsonify({'message': 'Media deleted'}), 200
        return jsonify({'message': 'Media not found'}), 404
