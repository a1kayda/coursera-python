import os
import csv

class CarBase:

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)



class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        params = body_whl.split('x')
        try:
            if not len(params) == 3:
                raise ValueError
            self.body_length = float(params[0])
            self.body_width = float(params[1])
            self.body_height = float(params[2])
        except (ValueError, IndexError):
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra

#осталось написать функцию которая парсит цсв и обработать еще всякие исключения
def get_car_list(csv_filename):
    car_list = []
    formats  = ['.jpeg', '.jpg', '.png', '.gif']
    c_boo = [1, 1, 1, 1, 0, 1, 0]
    t_boo = [1, 1, 0, 1, 1, 1, 0]
    sm_boo = [1, 1, 0, 1, 0, 1, 1]
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            if not reader:
                raise IOError
            next(reader)  # пропускаем заголовок
            for row in reader:
                r_boo = [bool(x) for x in row]
                #print(row)
                try:
                    if not len(row) == 7:
                        raise IndexError
                    if (row[0] == 'car') and r_boo == c_boo :
                        car = Car(row[1],row[3], row[5], row[2])
                    elif row[0] == 'truck':
                        r_boo[4] = 1
                        if r_boo == t_boo :
                            car = Truck(row[1],row[3], row[5], row[4])
                        else:
                            continue
                    elif row[0] == 'spec_machine' and r_boo == sm_boo :
                        car = SpecMachine(row[1],row[3], row[5], row[6])
                    else:
                        continue
                    if car.get_photo_file_ext() not in formats :
                        raise ValueError
                    car_list.append(car)
                except (ValueError, IndexError):
                    continue
    except IOError:
        return []
    return car_list
