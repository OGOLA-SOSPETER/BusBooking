from BusesData.Buses import Buses
from Fares.FareRates import Fare
from Routes.BusData import DataBase

pick = DataBase()
bus = Buses()

class Customer(Fare,Buses):
    fares = Fare()
    destination = pick.DropPoints()
    name = []
    age = []
    gender = ['male', 'female']
    start = pick.PickPoints()


    def __init__(self):
        super().__init__()
        self.fares = Fare.getFare()
        self.bus_number = bus.busDetails()
        self.driver_name = bus.driver_Details()

        pass

    def busDetails(self):
        pass
    def driver_Details(self):
        self.licence = license

        pass
    def show_register(self):
        pass
    def Display(self):
        print('\n', '-'*30)
        print('Your driver\'s name is :  ', self.driver_name,
              ' of vehicle Registration Number: ', self.bus_number)
        print(self.name, 'You are ',self.age, 'Years Old  and are a ',self.gender)
        print('Departure Station: ',self.start)
        print('Drop Off Point: ',self.destination)
        print('Your fare is Kshs. ', self.fares)
        print('\n', '-'*30)


    def CustDetails(self):
        print('Enter details here:')
        self.name = input('Name: ')
        self.age = input('Age: ')
        self.gender = input('Gender: ')
        self.start = input('StartPoint: ')
        self.destination = input('Destination: ')


Customer1 = Customer()
Customer1.busDetails()
Customer1.driver_Details()
Customer1.show_register()
Customer1.CustDetails()
Customer1.Display()
