class TravelSchedule:
    def __init__(self):
        super().__init__()

    @staticmethod
    def work_days():
        days = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for p in range(len(days)):
            print(p+1,'.', days[p])

    @staticmethod
    def get_day():
        day = input('Enter day of the week: ')
        if day.lower() == 'saturday' or day.lower() == 'sunday':
            print('It\'s a Weekend.\nWe remain CLOSED.\nKindly travel with us from Monday.')

        else:
            print("Continue to login")

#Travel = TravelSchedule
#Travel.work_days()
#Travel.get_day()

