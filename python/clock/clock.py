class Clock:
    def __init__(self, hour, minute):
        over = int(-1 if -60 <= minute < 0 else minute // 60)  # initial 'over' variable is better than nested if condition one-line
        self.hour = ((hour if hour >= 0 else 24 - (abs(hour) % 24)) + over) % 24
        self.minute = (minute % 60) if (minute % 60) >= 0else 60 - (abs(minute) % 60)

    def __repr__(self):
        hour = str(self.hour) if self.hour >= 10 else "0" + str(self.hour)
        minute = str(self.minute) if self.minute >= 10 else "0" + str(self.minute)
        return hour + ":" + minute

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        # this can be make another object
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)