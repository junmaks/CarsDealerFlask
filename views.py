from app import app
import funcs


@app.errorhandler(404)
def not_found(error):
    return funcs.not_found(error)


@app.route('/')
@app.route('/api/')
def index():
    return funcs.get_index()


@app.route('/api/dealers/', methods=['GET', 'POST'])
def get_data_dealers():
    return funcs.get_data_dealers()


@app.route('/api/dealers/<int:id_dealer>', methods=['GET', 'PUT', 'DELETE'])
def get_dealer(id_dealer):
    return funcs.get_dealer(id_dealer)


@app.route('/api/cars/', methods=['GET', 'POST'])
def get_data_cars():
    return funcs.get_data_cars()


@app.route('/api/cars/<int:id_car>', methods=['GET', 'PUT', 'DELETE'])
def get_car(id_car):
    return funcs.get_car(id_car)
