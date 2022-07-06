class Astronaut:
    """Astronaut Class"""

    def __init__(self,name, status, flightHr):
        print("initializing name, status, and flight hours")
        self.__name = name
        self.__status = status
        self.__flightHr = flightHr

    def __str__(self):
        return '%s %s' % (self.__name, self.__status)

    @property
    def name(self):
        print("Getting name")
        return self.__name
    
    # def __init__(self,flightHr):
    #     print("initializing flight hours")
    #     self.__flightHr = flightHr

    def __gt__(self, other):
        print("__gt__ called - self: %s, other: %s" % (self, other))
        return self.flightHr > other.flightHr

    def __eq__(self,other):
        print("__eq__ called - self: %s, other: %s" % (self, other))
        return self.flightHr == other.flightHr

    def __ge__(self,other):
        print("__ge__ called - self: %s, other: %s" % (self, other))
        return self.flightHr >= other.flightHr

    @property
    def flightHr(self):
        print("Getting flight hours")
        return self.__flightHr

    # def __init__(self,status):
    #     print("initializing status")
    #     self.__status = status

    @property
    def status(self):
        print("Getting status")
        return self.__status


import csv

aF = open('astronauts.csv', 'r')
astronautsDict = csv.DictReader(aF)

astronautList = []

for i in astronautsDict:
    astronautList.append(Astronaut(i['Name'], i['Status'], i['Space Flight (hr)']))

for i in astronautList:
    print(i)

print(astronautList[0] > astronautList[1])
print(astronautList[0] >= astronautList[1])
print(astronautList[0] == astronautList[1])