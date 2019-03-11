"""
    Determines today's fajr and maghrib times, along tomorrow's fajr time.

    METHOD 1: Auto-detect location
    The script will automatically detect your location. This will be done using
    the am.i.mullvad.net API. If you're using a VPN/proxy, this could cause 
    location inaccuracies.

    METHOD 2: Manual input
    You can manually give the script your location. This can be a ZIP code, a city
    name, or coordinates. Make sure to use quotes if a space is necessary.

    EXAMPLES:
    > python3 ramadanTimes 'Poughkeepsie, NY'
    > python3 ramadanTimes 12604
    > python3 ramadanTimes 41.7599,-73.7437
"""
import calendar
import sys
import time
import requests

BASE = 'http://api.aladhan.com/v1/calendarByAddress?address='
IP_URL = 'https://am.i.mullvad.net/json'

'''
    METHODS:
    0 - Shia Ithna-Ansari
    1 - University of Islamic Sciences, Karachi
    2 - Islamic Society of North America
    3 - Muslim World League
    4 - Umm Al-Qura University, Makkah
    5 - Egyptian General Authority of Survey
    7 - Institute of Geophysics, University of Tehran
    8 - Gulf Region
    9 - Kuwait
    10 - Qatar
    11 - Majlis Ugama Islam Singapura, Singapore
    12 - Union Organization islamic de France
    13 - Diyanet İşleri Başkanlığı, Turkey
    99 - Custom. See https://aladhan.com/calculation-methods
'''
METHOD = 2

def get_times(location):
    '''
        finds fajr [today], fajr [tomorrow], and maghrib based on your location
    '''
    month = int(time.strftime('%m'))
    year = int(time.strftime('%Y'))
    day = int(time.strftime('%d'))

    url = f'{BASE}{location}&method={METHOD}&month={month}&year={year}'
    prayer_data = requests.get(url).json()['data']
    fajr_today = prayer_data[day]["timings"]["Fajr"]
    maghrib = prayer_data[day]["timings"]["Maghrib"]

    if day == calendar.monthrange(year, month)[1]:
        fajr_month = ((month == 11) * 12) + ((month + 1) % 12)
        fajr_year = year + (month == 12)
        fajr_url = f'{BASE}{location}&method={METHOD}&month={fajr_month}&year={fajr_year}'
        fajr_tomorrow = requests.get(fajr_url).json()['data'][1]["timings"]["Fajr"]

    else:
        fajr_tomorrow = prayer_data[day+1]["timings"]["Fajr"]

    return f"Fajr [today]: {fajr_today}\nMaghrib: {maghrib}\nFajr [tomorrow]: {fajr_tomorrow}"

def get_location():
    '''
        Gets your location using mullvad's API
    '''
    response = requests.get(IP_URL).json()
    return f'{response["latitude"]}, {response["longitude"]}'

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print(get_times(get_location()))

    elif len(sys.argv) == 2:
        print(get_times(sys.argv[1]))

    else:
        exit('Usage: python3 ramadanTimes.py or python3 ramadanTimes.py [location]')
