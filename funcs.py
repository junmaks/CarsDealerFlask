from flask import request, render_template, jsonify, make_response, abort
from playhouse.shortcuts import model_to_dict, dict_to_model

from models import Dealers, Cars

def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def get_index():
    return render_template('index.html')


def get_data_dealers():
    if request.method == 'GET':
        dealers = Dealers.select()
        result = []
        for dealer in dealers:
            result.append(model_to_dict(dealer))
        return jsonify(result)

    if request.method == 'POST':
        if not request.json or not 'title' in request.json:
            abort(400)
        data = {
            'title': request.json.get('title'),
            'locations': request.json.get('locations', ""),
            'year': request.json.get('year', ""),
        }
        new_dealer = dict_to_model(Dealers, data)
        new_dealer.save()
        return jsonify({'result': data}), 201


def get_dealer(id_dealer):
    if request.method == 'GET':
        try:
            dealer = Dealers.get(Dealers.id == id_dealer)
            return jsonify(model_to_dict(dealer))
        except:
            return jsonify({'error': 'Not found object'})

    if request.method == 'PUT':
        try:
            dealer = Dealers.get(Dealers.id == id_dealer)
            if not request.json:
                abort(400)
            print(dealer.brand)
            data = {
                'brand': request.json.get('brand', ""),
                'car_model': request.json.get('car_model', ""),
                'year_release': request.json.get('year_release'),
                'price': request.json.get('price'),
                'dealer': request.json.get('dealer'),
            }
            dealer.brand = data['brand']
            dealer.car_model = data['car_model']
            dealer.year_release = data['year_release']
            dealer.price = data['price']
            dealer.dealer = data['dealer']
            dealer.save()
            return jsonify({'result': 'done'})
        except Exception as ex:
            return jsonify({'error': str(ex)})


    if request.method == 'DELETE':
        try:
            dealer = Dealers.get(Dealers.id == id_dealer)
            dealer.delete_instance()
            return jsonify({'result': 'done'})
        except Exception as ex:
            return {'error': str(ex)}




def get_data_cars():
    if request.method == 'GET':
        cars = Cars.select()
        result = []
        for car in cars:
            result.append(model_to_dict(car))
        return jsonify(result)
    if request.method == 'POST':
        if not request.json or not 'dealer' in request.json:
            abort(400)
        data = {
            'brand': request.json.get('brand', ""),
            'car_model': request.json.get('car_model', ""),
            'year_release': request.json.get('year_release'),
            'price': request.json.get('price'),
            'dealer': request.json.get('dealer'),
        }
        new_car = dict_to_model(Cars, data)
        new_car.save()
        return jsonify({'result': data}), 201


def get_car(id_car):

    if request.method == 'GET':
        try:
            car = Cars.get(Cars.id == id_car)
            return jsonify(model_to_dict(car))
        except:
            return jsonify({'error': 'Not found object'})

    if request.method == 'PUT':
        try:
            car = Cars.get(Cars.id == id_car)
            if not request.json:
                abort(400)
            print(car.brand)
            data = {
                'brand': request.json.get('brand', ""),
                'car_model': request.json.get('car_model', ""),
                'year_release': request.json.get('year_release'),
                'price': request.json.get('price'),
                'dealer': request.json.get('dealer'),
            }
            car.brand = data['brand']
            car.car_model = data['car_model']
            car.year_release = data['year_release']
            car.price = data['price']
            car.dealer = data['dealer']
            car.save()
            return jsonify({'result': 'done'})
        except Exception as ex:
            return jsonify({'error': str(ex)})

    if request.method == 'DELETE':
        try:
            car = Cars.get(Cars.id == id_car)
            car.delete_instance()
            return jsonify({'result': 'done'})
        except Exception as ex:
            return {'error': str(ex)}
