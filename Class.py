class Car():
    def __init__(self, name, year, mile):
        self.name = name
        self.year = year
        self.mile = mile

    def info(self):
        print('Car name is: ', self.name, 'Car year is: ', self.year, 'Car mile is: ', self.mile)


ford = Car('Ford Mustang', 1967, 66000)
ford.info()