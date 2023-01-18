#import File3
import time

from File3 import People

class Student(People):
    def __init__(self, name, age, id):
        People.__init__(self, name, age)
        self.id = id

    def change_name(self, name):
        self._name = name

    def learn(self):
        print("Learning...")

    def set_class(self, className):
        self.className = className

    def get_class(self):
        return self.className

    def read(self):
        for i in range(9):
            print("Reading...")
            time.sleep(0.4)



if __name__ == "__main__":

    student1 = Student("Sona", 33, 11)
    student1.info()
    # student1.read()
    print(student1.get_name())
    student1.set_name("Sonata")
    print(student1.friends)
    # print(student1._name)