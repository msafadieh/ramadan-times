#! python3
import requests, json, time, calendar, sys
month = int(time.strftime('%m'))
year = int(time.strftime('%Y'))
day = int(time.strftime('%d'))
base = 'http://api.aladhan.com/v1/calendarByAddress?address='

# METHODS:
# 0 - Shia Ithna-Ansari
# 1 - University of Islamic Sciences, Karachi
# 2 - Islamic Society of North America
# 3 - Muslim World League
# 4 - Umm Al-Qura University, Makkah
# 5 - Egyptian General Authority of Survey
# 7 - Institute of Geophysics, University of Tehran
# 8 - Gulf Region
# 9 - Kuwait
# 10 - Qatar
# 11 - Majlis Ugama Islam Singapura, Singapore
# 12 - Union Organization islamic de France
# 13 - Diyanet İşleri Başkanlığı, Turkey
# 99 - Custom. See https://aladhan.com/calculation-methods
method = 2

#### GETS YOUR LOCATION
if len(sys.argv) == 1:
    key = '' # enter IPStack API key
    location_url = 'http://api.ipstack.com/check?access_key={key}'
    location_request = requests.get(location_url)
    locataion_data = json.loads(location_request.text)
    location = str(locataion_data['latitude']) + ',' + str(locataion_data['longitude'])

elif len(sys.argv) == 2:
    location = sys.argv[1]

else:
    print('Usage: python3 ramadanTimes.py or python3 ramadanTimes.py [location]')
    exit()

#### finds fajr [today], fajr [tomorrow], and maghrib based on your location
if day == calendar.monthrange(year,month)[1]:
    fajr_day = 1
    fajr_month = (month + 1) % 12
    fajr_year = year
    if fajr_month == 0:
        fajr_month = 12
    if month == 12:
        fajr_year += 1

    url = f'{base}{location}&method={method}&month={month}&year={year}'
    fajrUrl = f'{base}{location}&method={method}&month={fajr_month}&year={fajr_year}'

    imported = requests.get(url)
    prayer_data = json.loads(imported.text)['data']
    fajr_imported = requests.get(fajrUrl)
    fajr_prayer_data = json.loads(fajr_imported.text)['data']
    print('Fajr [today]: ' + prayer_data[day]['timings']['Fajr'])
    print('Maghrib: ' + prayer_data[day]['timings']['Maghrib'])
    print('Fajr [tomorrow]: ' + fajr_prayer_data[fajr_day]['timings']['Fajr'])
else:
    fajr_day = day+1
    url = f'{base}{location}&method={method}&month={month}&year={year}'
    imported = requests.get(url)
    prayer_data = json.loads(imported.text)['data']
    print('Fajr [today]: ' + prayer_data[day]['timings']['Fajr'])
    print('Maghrib: ' + prayer_data[day]['timings']['Maghrib'])
    print('Fajr [tomorrow]: ' + prayer_data[fajr_day]['timings']['Fajr'])
