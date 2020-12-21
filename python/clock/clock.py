class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour if hour >= 0 else 24 - (abs(hour) % 24) + int(minute // 60)) % 24
        self.minute = (minute % 60) if minute >= 0 else 60 - (abs(minute) % 60)
        # minute 가 60 아래일때 음수일 경우 hour을 빼주는 부분에 대해서 생각을 해야함.

    def __repr__(self):
        hour = str(self.hour) if self.hour >= 10 else "0" + str(self.hour)
        minute = str(self.minute) if self.minute >= 10 else "0" + str(self.minute)
        return hour + ":" + minute

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        hour = self.hour + int((self.minute + minutes) / 60)
        minute = (self.minute + minutes) % 60
        # this can be make another object
        return Clock(hour, minute)

    def __sub__(self, minutes):
        hour = self.hour - int(abs(minutes) / 60)
        minute = self.minute - (minutes % 60) if self.minute >= (abs(minutes) % 60) \
                    else 60 - (self.minute - (abs(minutes) % 60))
        return Clock(hour, minute)


if __name__ == '__main__':
    print(Clock(2, 40), Clock(3, -20))