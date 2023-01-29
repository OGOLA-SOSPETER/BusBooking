from Routes.BusData import DataBase

class Buses(DataBase):
    def __init__(self):
        super().__init__()
        self.bus_number = []
        self.driver_name = []
        self.licence = []
    def busDetails(self):
        #getting the bus details

        print('\n' + '-'*30)
        print('\t\tKindly Register Your Bus.')
        bus_number = input('Enter the bus number here: ')
        self.bus_number.append(bus_number)

    def driver_Details(self):
        #Getting driver details
        print('\t\tKindly Register Name of Driver of the Bus above: ')
        driver_name = input('Enter Driver\'s Name: ')
        self.driver_name.append(driver_name)

        print('\t\tEnter the Driver\'s licence Number')
        licence = input('Licence Number: ')
        self.licence.append(licence)
        print('-'*30)

    def show_register(self):
        for a in range(len(self.bus_number)):
            print('\n','#' * 30)
            print('Bus Number: ', self.bus_number[a])
            print('Driver Name: ', self.driver_name[a])
            print('Licence Number: ', self.licence[a])
            print('\n','#' * 30)

Details = Buses()
Details.busDetails()
Details.driver_Details()

Details.show_register()
