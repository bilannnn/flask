from datetime import datetime, timedelta
from statistics import mean
import requests
import pickle


# build report
course_db = {}
date = datetime.now()
for i in range(0, 365):
    site = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date.strftime("%Y%m%d")}&json'
    print(f'fetching course - {date}')
    r = requests.get(site)
    if r.status_code == 200:
        course = r.json()
        for val in course:
            if val['cc'] == 'USD':
                course_db[date.strftime("%Y-%m-%d")] = val['rate']
    date -= timedelta(days=1)

year = mean(course_db.values())
print(f'Year == {year}')

"""
...
2021-07-02: 27
2021-07-03: 25
2021-07-04: 23
2021-07-05: 24
...
2021-08-05: 24
2021-08-06: 25
2021-08-07: 26
2021-08-08: 24
...

by_mouth = {}
if date (2021-07-04) in by_mouth.keys() [2021-07, 2021-06]:    -> by_mouth.keys() список всіх місяців які вже записані в by_mouth
 2021-07 : [27, 25] + 23(2021-07-04)
else: data = 2021-08-05, by_mouth.keys() [2021-07, 2021-06]
    2021-08: [24, 25]


"""

by_mouth = {}
for date, record in course_db.items():
    date = date[:7]
    if date in by_mouth.keys():
        by_mouth[date].append(record)
    else:
        by_mouth[date] = [record]

mean_by_mouth = {date: mean(value) for date, value in by_mouth.items()}
print(mean_by_mouth)

data_for_dump = {date: f'{date}: ---Дані за місяць: {value};\nВідхилення: {year - value}' for date, value in mean_by_mouth.items()}
print(data_for_dump)

with open('report.pickle', 'wb') as handle:
    pickle.dump(data_for_dump, handle, protocol=pickle.HIGHEST_PROTOCOL)



# Reading pickle file
# import pickle
# with open('report.pickle', 'rb') as handle:
#     b = pickle.load(handle)
# print(b)
