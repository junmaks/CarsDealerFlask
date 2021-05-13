# CarsDealerFlask
1) Установка и активация venv
2) Выполнить make install (pip install -r requirements.txt)
3) Запуск make start (по дефолту http://localhost:5000/) (или запуск runserver.py, или gunicorn --workers=4 --bind=127.0.0.1:5000 app:app)


Json схемы находятся в папке JsonSchem
dealers - http://localhost:5000/api/dealers/
cars - http://localhost:5000/api/cars/

Примеры запросов:

Add new car
curl -i -H "Content-Type: application/json" -X POST -d '{"brand": "Audi", "car_model": "A6", "year_release": 2015, "price": 135000, "dealer": 3}' http://localhost:5000/api/cars

Delete car
curl -i -X DELETE http://localhost:5000/api/cars/2

Put car
curl -i -H "Content-Type: application/json" -X PUT -d '{"brand": "Audi", "car_model": "A5", "year_release": 2015, "price": 135000, "dealer": 3}' http://localhost:5000/api/cars/1




Add new dealer
curl -i -H "Content-Type: application/json" -X POST -d '{"title": "Dealer 4", "locations": "Rostov", "year": 1926}' http://localhost:5000/api/dealers


Delete new dealer
curl -i -X DELETE http://localhost:5000/api/dealers/2

Put dealer
curl -i -H "Content-Type: application/json" -X PUT -d '{"title": "Dealer 10", "locations": "Spb", "year": 2015}' http://localhost:5000/api/dealers/1
