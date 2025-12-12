import requests

def test_add_and_get_media():
    # Add a new media item
    data = {
        "name": "Test Book",
        "author": "Tester",
        "publication_date": "Mon Jan 1 2024",
        "category": "book",
        "available_for_borrowing": True
    }
    add_resp = requests.post("http://localhost:5000/add_media", json=data)
    assert add_resp.status_code == 201
    # Now check if it appears in available_media
    get_resp = requests.get("http://localhost:5000/available_media")
    assert get_resp.status_code == 200
    media_list = get_resp.json()["media"]
    assert any(m["name"] == "Test Book" for m in media_list)