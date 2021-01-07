import calendar
from datetime import date

class MeetupDayException(Exception):
    def __init__(self):
        super().__init__("out of range in month")


weekdays = [ "Monday",
             "Tuesday",
             "Wednesday",
             "Thursday",
             "Friday",
             "Saturday",
             "Sunday"]


def meetup(year, month, week, day_of_week):
    try:
        month_list = calendar.monthcalendar(year, month)
        weekday = weekdays.index(day_of_week)
        if week == "teenth":
            for w in month_list[::-1]:
                if 10 <= w[weekday] and w[weekday] < 20:
                    return date(year, month, w[weekday])
        elif week == "1st":
            for w in month_list:
                if w[weekday] != 0:
                    return date(year, month, w[weekday])
        elif week == "2nd":
            for w in month_list:
                if w[weekday] != 0:
                    return date(year, month, w[weekday] + 7)
        elif week == "3rd":
            for w in month_list:
                if w[weekday] != 0:
                    return date(year, month, w[weekday] + 14)
        elif week == "4th":
            for w in month_list:
                if w[weekday] != 0:
                    return date(year, month, w[weekday] + 21)
        elif week == "5th":
            if month_list[5][weekday] != 0:
                return date(year, month, month_list[5][weekday])
        elif week == "last":
            for w in month_list[::-1]:
                if w[weekday] != 0:
                    return date(year, month, w[weekday])
        else:
            raise MeetupDayException
    except Exception as e:
        print("Exception : ", e)


if __name__ == '__main__':
    # print(calendar.prmonth(2015, 3))
    print(meetup(2015, 2, "5th", "Monday"))