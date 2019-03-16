# ramadan-times

A simple Python script that finds Fajr and Maghrib times using the [Prayer Times API](https://aladhan.com/prayer-times-api).

```
> python ramadanTimes.py
Fajr [today]: 03:58 (EDT)
Maghrib: 20:11 (EDT)
Fajr [tomorrow]: 03:57 (EDT)
```

## Requirements:

1. Python 3
2. [A few requirements](requirements.txt)

## Installation:
Clone this repository to your computer.

```
> git clone https://github.com/msafadieh/ramadan-times.git
> cd ramadan-times
> pip3 install -r requirements.txt
> python3 ramadanTimes [location]
```

## Usage:

There are 2 ways to use this script.

**First way: automatically determine your location**

```
> python3 ramadanTimes
```

You can let the script find your location automatically based on your IP address using the [Mullvad API](https://am.i.mullvad.net/api). This is not ideal if you're using a VPN.

**Second way: manual location input**

```
> python3 ramadanTimes [location]
```

You can manually input your location for the script to use it. This can be your actual city and country, your zip code, or your coordinates. Make sure it's in between quotes if a space is necessary.

```
> python3 ramadanTimes 'Poughkeepsie, NY'
> python3 ramadanTimes 12604
> python3 ramadanTimes 41.7599,-73.7437
```
