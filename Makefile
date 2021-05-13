start:
	gunicorn --workers=4 --bind=127.0.0.1:5000 app:app

install:
	pip install -r requirements.txt
	pip install gunicorn


