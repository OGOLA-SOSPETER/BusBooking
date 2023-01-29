from Routes.BusData import DataBase
from Buses.Buses import Buses
import datetime

class Fare(Buses,DataBase):
    def __init__(self):
        super().__init__()
        self.fare = []

    @staticmethod
    def morning_fare():

        if datetime.datetime.now().replace(hour=23, minute=0,second=0) > datetime.datetime.now() < datetime.datetime.now().replace(hour=4,minute=29,second=0):
            print('CLOSED!!\\nWe open at 4:30am')

        elif datetime.datetime.now() < datetime.datetime.now().replace(hour=10,minute=0,second=0):
            fare = 'Khs.', 50
            return fare

        elif datetime.datetime.now() < datetime.datetime.now().replace(hour=12,minute=0,second=0):
            fare = 'Kshs. ', 70
            print(fare)
            return fare

    @staticmethod
    def evening_fare():
        if datetime.datetime.now() > datetime.datetime.now().replace(hour=12,minute=0,second=0):
            fare = 'Khs.', 80
            print(fare)
            return fare

        elif datetime.datetime.now().replace(hour=12, minute=0, second=0) < datetime.datetime.now() < datetime.datetime.now().replace(hour=20, minute=0, second=0):
            fare = 'Kshs. ', 90
            print(fare)
            return fare
