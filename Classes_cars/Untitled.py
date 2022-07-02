from solution import *
#from coursera import *
from time import time
if __name__ == "__main__":
    time_now = time()
    cars = get_car_list('coursera_week3_cars.csv')
    print(time() - time_now)
    #print(cars[0].brand)
    #print(cars[1].get_body_volume())
    #print(cars[1].body_width)
