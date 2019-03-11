# ramadan-times

A simple Python script that finds Fajr and Maghrib times using the [Prayer Times API](https://aladhan.com/prayer-times-api).

```
> python ramadanTimes.py
Fajr [today]: 03:58 (EDT)
Maghrib: 20:11 (EDT)
Fajr [tomorrow]: 03:57 (EDT)
```

## Requirements:

1. You need to have Python 3 installed. (On macOS you'll have to use ```python3``` instead of ```python```)

2. You need to have the requirements installed from ```requirements.txt```  file. You can install it using ```pip```:

```
> pip install -r requirements.txt
```

## Installation:
Clone this repository to your computer.

```
> git clone https://github.com/msafadieh/ramadan-times.git
> cd ramadan-times
> python ramadanTimes [location]
```

## Usage:

There are 2 ways to use this script.

**First way: automatically determine your location**

```
> python ramadanTimes
```

You can let the script find your location automatically based on your IP address using the [Mullvad API](https://am.i.mullvad.net/api). This is not ideal if you're using a VPN.

**Second way: manual location input**

```
> python ramadanTimes [location]
```

You can manually input your location for the script to use it. This can be your actual city and country, your zip code, or your coordinates. Make sure it's in between quotes if a space is necessary.

```
> python ramadanTimes 'Poughkeepsie, NY'
> python ramadanTimes 12604
> python ramadanTimes 41.7599,-73.7437
```
