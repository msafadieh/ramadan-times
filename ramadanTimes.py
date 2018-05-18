#! python3
import requests, json, time, calendar, sys
month = int(time.strftime('%m'))
year = int(time.strftime('%Y'))
day = int(time.strftime('%d'))
monthDays = []
for i in range(1,13):
    monthDays.append(calendar.monthrange(int(time.strftime('%Y')),i)[1])

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

### finds fajr [today], fajr [tomorrow], and maghrib based on your location
if day == monthDays[month]:
    fajrDay = 1
    fajrMonth = (month + 1) % 12
    if month == 12:
        fajrYear = year + 1

    url = 'http://api.aladhan.com/v1/calendarByAddress?address=%s&method=6&month=%s&year=%s' % (location, month, year)
    fajrUrl = 'http://api.aladhan.com/v1/calendarByAddress?address=%s&method=2&month=%s&year=%s' % (location, fajrMonth, fajrYear)

    imported = requests.get(url)
    prayerData = json.loads(imported.text)['data']
    fajrImported = requests.get(fajrUrl)
    fajrPrayerData = json.loads(fajrImported.text)['data']
    print('Fajr [today]: ' + prayerData[day]['timings']['Fajr'])
    print('Maghrib: ' + prayerData[day]['timings']['Maghrib'])
    print('Fajr [tomorrow]: ' + fajrPrayerData[fajrDay]['timings']['Fajr'])
else:
    fajrDay = day+1
    url = 'http://api.aladhan.com/v1/calendarByAddress?address=%s&method=2&month=%s&year=%s' % (location, month, year)
    imported = requests.get(url)
    prayerData = json.loads(imported.text)['data']
    print('Fajr [today]: ' + prayerData[day]['timings']['Fajr'])
    print('Maghrib: ' + prayerData[day]['timings']['Maghrib'])
    print('Fajr [tomorrow]: ' + prayerData[fajrDay]['timings']['Fajr'])
