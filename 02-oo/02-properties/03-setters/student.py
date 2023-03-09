class Time:

    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self,value):
        if value < 24 and value >= 0:
            self.__hours = value
        else:
            raise ValueError('hours must be between 0 and 24')
        
    @property
    def minutes(self):
        return self.__minutes
        
    @minutes.setter
    def minutes(self,value):
        if value < 60 and value >= 0:
            self.__minutes = value
        else:
            raise ValueError('minutes must be between 0 and 60')
        
    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self,value):
        if value < 60 and value >= 0:
            self.__seconds = value
        else:
            raise ValueError('seconds must be between 0 and 60')
