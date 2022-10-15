from .ad_type_enum import AdType
import os
import pycraigslist
from time import sleep

from geopy.geocoders import Nominatim

from datetime import datetime   
from tzwhere import tzwhere
import pytz


def find_address_from_coord(search_coord):
        geocoder = Nominatim(user_agent=os.getenv("NOMINATIM_EMAIL_ID"))
        lat, lon = search_coord
        location = geocoder.reverse(str(lat) + ", " + str(lon))
        return location.raw["address"]

def find_timezone_from_coord(search_coord):
    tz = tzwhere.tzwhere(forceTZ=True)
    lat, lon = search_coord
    return tz.tzNameAt(lat, lon)


class CraigslistScraper():
    def __init__(self, search_coord):
        search_address = find_address_from_coord(search_coord)
        self.city = search_address["city"].strip().lower()
        self.timezone = find_timezone_from_coord(search_coord)
        
    def get_all_ads(self, query):
        all_listings = pycraigslist.forsale(site=self.city, query=query)
        all_ads = []
        for listing in all_listings.search_detail(include_body=True, limit=10):
            ad = {}
            ad["date"] = self.parse_date_to_utc(listing)
            ad["name"] = listing["title"]
            ad["type"] = AdType.Item
            ad["coord"] = self.parse_coord(listing)
            ad["price"] = self.parse_price(listing)
            ad["description"] = listing["body"]
            ad["link"] = listing["url"]
            all_ads.append(ad)

            #sleep to avoid spamming craigslist and getting a 403
            sleep(.5)
        return all_ads

    def parse_date_to_utc(self, listing):
        #grab datetime object from listing
        date_string = listing["last_updated"]
        date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M')

        #set timezone ad is listed in
        timezone = pytz.timezone(self.timezone)
        date_object = timezone.localize(date_object, is_dst=None)
        #convert to utc
        return date_object.astimezone(pytz.utc)


    def parse_price(self, listing):
        price_string = listing["price"]
        price_string = price_string.replace("$", "")
        if(len(price_string) == 0):
            return 0.0
        return float(price_string)
        

    def parse_coord(self, listing):
        lat_str = listing["lat"]
        lon_str = listing["lon"]
        return float(lat_str), float(lon_str)


if __name__ == "__main__":
    print("hello")