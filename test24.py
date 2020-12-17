car_brands = ['Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda']

def convert_to_tuple(car_brands):
    static_cars = tuple(car_brands)
    return static_cars

def print_tuples():
    tuples = convert_to_tuple(car_brands)
    print(tuples)
    return