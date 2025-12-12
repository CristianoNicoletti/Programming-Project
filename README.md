
# Library Management System

This project is a Library Management System using a GUI built with PySide6 and a backend RESTful API built with Flask. It allows users to add, search, view, and delete media items (books, films, magazines) in a persistent dictionary stored on a JSON file.

## Features

- Add new media items (book, film, magazine) with details such as name, author, publication date, and availability
- Search for media items by name
- Filter and view available media by category
- Delete media items
- Persistent storage of library state in a JSON file
- RESTful backend API using Flask
- Automated tests for backend and frontend functionality

## Project Structure

- `main.py` — Launches the GUI and starts the backend server
- `main_window.py` — Main GUI logic (PySide6)
- `ui_main_window.py` — Auto-generated UI code from Qt Designer
- `media_item.py` — Media item and category definitions
- `state.py` — Persistent state management for media items
- `routes.py` — Flask API endpoints
- `app.py` — Flask app entry point
- `state.json` — Persistent storage for media items
- `requirements.txt` — Python dependencies
- `test_1_backend_healthcheck.py`, `test_2_backend_add_and_retrieve_media.py`, `test_3_frontend_category_cmbx_populated.py` — Automated tests

## Installation & Setup

1. **Clone the repository**
2. **Create and activate a virtual environment (optional but recommended):**
	```
	python -m venv my_venv
	my_venv\Scripts\activate  # On Windows
	```

3. **Install dependencies:**
	```
	pip install -r requirements.txt
	```

## Running the Application

1. **Start the application:**
	```
	python main.py
	```
	This will launch the GUI and automatically start the Flask backend server.


2. **Using the GUI:**
	- Add new media items using the "Add Media" tab
	- Search for items by name on the "Search" tab
	- Filter by category and view available items on the "Browse" tab
	- Select and delete items as needed
    - View any media items metadata by selecting it in either the search or browse tabs 

## Running Tests

To run the automated tests, ensure the backend is running, then execute:

```
pytest
```

## Dependencies

See `requirements.txt` for the full list. Key packages include:
- Flask
- PySide6
- requests
- pytest

## Notes

- The backend server runs on `localhost:5000` by default.
- All data is stored in `state.json` in the project directory.
- The GUI and backend communicate via HTTP requests.

