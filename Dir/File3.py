import time
class People():
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self.friends = ["Axvan", "Karen", "Margo"]

    def info(self):
        print(f"Name is: {self.__name}")

    def read(self):
        for i in range(9):
            print("Reading...")
            time.sleep(1)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    person1 = People("John", 44)
    person1.info()