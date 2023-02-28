class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if value <0 or value > 23:
            raise ValueError("must be between 0 and 23")
        self.__hours = value
    
    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if value < 0 or value > 59:
            raise ValueError("must be between 0 and 59")
        self.__minutes = value
    
    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if value < 0 or value > 59:
            raise ValueError("must be between 0 and 59")
        self.__seconds = value
