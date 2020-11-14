#!/usr/bin/env python3

import argparse, json
from noaa_sdk import noaa

n = noaa.NOAA()

parser = argparse.ArgumentParser()
parser.add_argument("-z", "--zip", help="ZIP code to search for", default="20500", type=int)
parser.add_argument("-c", "--country", help="Country code to use. Default is US.", default="US")

args = parser.parse_args()
zipc = args.zip
country = args.country

def zip_sanity_check(zipc):
    """Sanity check to ensure a 0-starting ZIP isn't invalid"""
    if len(str(zipc)) < 4:
        zipc = str(zipc).zfill(5)
        return str(zipc)
    elif len(str(zipc)) < 5:
        zipc = str(zipc).zfill(5)
        return str(zipc)
    elif len(str(zipc)) == 5:
        return str(zipc)
    else:
        raise Exception("Invalid ZIP code")


if __name__ == "__main__":
    args.zip = zip_sanity_check(args.zip)
    print("Current conditions for " + args.zip + ", " + args.country + ":")
    res = n.get_forecasts(args.zip, args.country, False)
    current_forecast = res[0]
    current_formatted = list(current_forecast.values())
    print("The conditions for " + current_formatted[1].lower() + " are...\n")
    print("Description: " + current_formatted[11])
    print("Temperature: " + str(current_formatted[5]) + "° " + current_formatted[6])
    print("Winds: " + current_formatted[9] + " at " + current_formatted[8] + "\n")
