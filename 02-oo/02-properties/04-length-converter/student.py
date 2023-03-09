
#*3.28 to go from meter to feet
#*39.37 to go from meter to inch

class LengthConverter:
    
    def __init__(self):
        self.__distanceInMeter = 0

    @property
    def meter(self):
        return self.__distanceInMeter
    
    @meter.setter
    def meter(self,value):
        self.__distanceInMeter = value

    @property
    def feet(self):
        return self.__distanceInMeter * 3.28084
    
    @feet.setter
    def feet(self,value):
        self.__distanceInMeter = value / 3.28084
    
    @property
    def inch(self):
        return self.__distanceInMeter * 39.3701
    
    @inch.setter
    def inch(self,value):
        self.__distanceInMeter = value / 39.3701


converter = LengthConverter()    
converter.meter = 100
print(converter.feet)
print(converter.inch)
print(converter.meter)
converter.feet = 5
print(converter.inch)