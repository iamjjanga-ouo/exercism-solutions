from datetime import datetime, timedelta


def add(moment):
    return moment + timedelta(seconds=1000000000)


## Python time 관련함수 time, datetime, timedelta 뽀개
'''
1. time 모듈로 현재 시간 구하기
: 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반횐 (UTC 기준)
>>> import time
>>> time.time()
1609371331.243673

2. 날짜와 시간 형태로 변환
: localtime() -> time반환 값을 날짜와 시간 형태로 변환 (현재 지역 시간대 사용, Korea=UTC+0900)  
>>> time.localtime(time.time())
time.struct_time(tm_year=2020, tm_mon=12, tm_mday=31, tm_hour=8, tm_min=35, tm_sec=5, tm_wday=3, tm_yday=366, tm_isdst=0)

3. 날짜/시간 포맷에 맞춰서 출력
time.strftime('format', time_object)

>>> time.strftime('%Y-%m-%d', time.localtime(time.time()))
'2020-12-31'
>>> time.strftime('%c', time.localtime(time.time()))
'Thu Dec 31 08:38:34 2020'

4. datetime 모듈로 현재 날자와 시간 구하기
: datetime 모듈의 datetime 클래스 + today 메서

>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2020, 12, 31, 8, 39, 30, 236381)
드
5. 특정 날짜와 시간으로 객체 생성
: datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)

>>> d = datetime.datetime(2020, 12, 31)
>>> d
datetime.datetime(2020, 12, 31, 0, 0)

6. 문자열로 날짜/시간 객체 만들기
: datetime.datetime.strptime('날짜문자열', 'format')
>>> d = datetime.datetime.strptime('2020-12-31', '%Y-%m-%d')
>>> d
datetime.datetime(2020, 12, 31, 0, 0)

7. 날짜/시간 객체를 문자열로 만들기
: datetime 객체.strftime('format')

>>> d.strftime('%Y-%m-%d')
'2020-12-31'
>>> d.strftime('%c')
'Thu Dec 31 00:00:00 2020'

8. 날짜와 시간 속성에 접근
: datetime.datetime 객체에서 year, month, day, hour, minute, second, microsecond 속성을 따로 가져올 수 있음

>>> today = datetime.datetime.today()
>>> today.year, today.month, today.day
(2020, 12, 31)

9. 날짜와 시간차이 계산
: datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

>>> d = datetime.datetime(2020, 12, 31)
>>> d - datetime.timedelta(days=20)
datetime.datetime(2020, 12, 11, 0, 0)
'''