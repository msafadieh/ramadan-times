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
    locationURL = 'http://api.ipstack.com/check?access_key=684b90ffe5e846163a1b244e3a1bab9c'
    locationRequest = requests.get(locationURL)
    locationData = json.loads(locationRequest.text)
    location = str(locationData['latitude']) + ',' + str(locationData['longitude'])

elif len(sys.argv) == 2:
    location = sys.argv[1]

else:
    print('Usage: python3 ramadanTimes.py or python3 ramadanTimes.py [location]')
    exit()

#### finds fajr [today], fajr [tomorrow], and maghrib based on your location
if day == calendar.monthrange(year,month)[1]:
    fajrDay = 1
    fajrMonth = (month + 1) % 12
    fajrYear = year
    if fajrMonth == 0:
        fajrMonth = 12
    if month == 12:
        fajrYear += 1

    url = f'{base}{location}&method={method}&month={month}&year={year}'
    fajrUrl = f'{base}{location}&method={method}&month={fajrMonth}&year={fajrYear}'

    imported = requests.get(url)
    prayerData = json.loads(imported.text)['data']
    fajrImported = requests.get(fajrUrl)
    fajrPrayerData = json.loads(fajrImported.text)['data']
    print('Fajr [today]: ' + prayerData[day]['timings']['Fajr'])
    print('Maghrib: ' + prayerData[day]['timings']['Maghrib'])
    print('Fajr [tomorrow]: ' + fajrPrayerData[fajrDay]['timings']['Fajr'])
else:
    fajrDay = day+1
    url = f'{base}{location}&method={method}&month={month}&year={year}'
    imported = requests.get(url)
    prayerData = json.loads(imported.text)['data']
    print('Fajr [today]: ' + prayerData[day]['timings']['Fajr'])
    print('Maghrib: ' + prayerData[day]['timings']['Maghrib'])
    print('Fajr [tomorrow]: ' + prayerData[fajrDay]['timings']['Fajr'])
