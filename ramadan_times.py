#! python3
"""
Determines today's fajr and maghrib times, along tomorrow's fajr time.

METHOD 1: Auto-detect location
The script will automatically detect your location. You will need an ipstack
API KEY to enable it do so. You can get one from ipstack.com and then assign
it to KEY (line 49).

METHOD 2: Manual input
You can manually give the script your location. This can be a ZIP code, a city
name, or coordinates. Make sure to use quotes if a space is necessary.

EXAMPLES:
> python3 ramadanTimes 'Poughkeepsie, NY'
> python3 ramadanTimes 12604
> python3 ramadanTimes 41.7599,-73.7437
"""
import calendar
import json
import sys
import time
import requests

MONTH = int(time.strftime('%m'))
YEAR = int(time.strftime('%Y'))
DAY = int(time.strftime('%d'))
BASE = 'http://api.aladhan.com/v1/calendarByAddress?address='

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
METHOD = 2

#### GETS YOUR LOCATION
if len(sys.argv) == 1:
    KEY = '' # enter ipstack API key
    if not KEY:
        exit('No valid ipstack API key.')
    LOCATION_URL = f'http://api.ipstack.com/check?access_key={KEY}'
    LOCATION_REQUEST = requests.get(LOCATION_URL)
    LOCATION_DATA = json.loads(LOCATION_REQUEST.text)
    LOCATION = f'{LOCATION_DATA["latitude"]},{LOCATION_DATA["longitude"]}'

elif len(sys.argv) == 2:
    LOCATION = sys.argv[1]

else:
    exit('Usage: python3 ramadanTimes.py or python3 ramadanTimes.py [location]')

#### finds fajr [today], fajr [tomorrow], and maghrib based on your location
if DAY == calendar.monthrange(YEAR, MONTH)[1]:
    FAJR_DAY = 1
    FAJR_MONTH = (MONTH + 1) % 12
    FAJR_YEAR = YEAR
    if FAJR_MONTH == 0:
        FAJR_MONTH = 12
    if MONTH == 12:
        FAJR_YEAR += 1

    URL = f'{BASE}{LOCATION}&method={METHOD}&month={MONTH}&year={YEAR}'
    FAJR_URL = f'{BASE}{LOCATION}&method={METHOD}&month={FAJR_MONTH}&year={FAJR_YEAR}'

    IMPORTED = requests.get(URL)
    PRAYER_DATA = json.loads(IMPORTED.text)['data']
    FAJR_IMPORTED = requests.get(FAJR_URL)
    FAJR_PRAYER_DATA = json.loads(FAJR_IMPORTED.text)['data']
    print(f'Fajr [today]: {PRAYER_DATA[DAY]["timings"]["Fajr"]}')
    print(f'Maghrib: {PRAYER_DATA[DAY]["timings"]["Maghrib"]}')
    print(f'Fajr [tomorrow]: {FAJR_PRAYER_DATA[FAJR_DAY]["timings"]["Fajr"]}')
else:
    FAJR_DAY = DAY+1
    URL = f'{BASE}{LOCATION}&method={METHOD}&month={MONTH}&year={YEAR}'
    IMPORTED = requests.get(URL)
    PRAYER_DATA = json.loads(IMPORTED.text)['data']
    print(f'Fajr [today]: {PRAYER_DATA[DAY]["timings"]["Fajr"]}')
    print(f'Maghrib: {PRAYER_DATA[DAY]["timings"]["Maghrib"]}')
    print(f'Fajr [tomorrow]: {PRAYER_DATA[FAJR_DAY]["timings"]["Fajr"]}')
