from datetime import datetime
from src import AdType
import validators

def assert_ad_is_properly_defined(ad_dictionary):
    assert isinstance(ad_dictionary, dict) 
    assert grab_ad_type(ad_dictionary) is not None
    assert grab_ad_name(ad_dictionary) is not None 
    assert grab_ad_coordinates(ad_dictionary) is not None
    assert grab_ad_price(ad_dictionary) is not None
    assert grab_ad_description(ad_dictionary) is not None
    assert grab_ad_link(ad_dictionary) is not None

def grab_ad_link(ad_dictionary):
    return ad_dictionary["link"]

def grab_ad_description(ad_dictionary):
    return ad_dictionary["description"]

def grab_ad_price(ad_dictionary):
    return ad_dictionary["price"]

def grab_ad_coordinates(ad_dictionary):
    return ad_dictionary["coord"]

def grab_ad_name(ad_dictionary):
    return ad_dictionary["name"]

def grab_ad_type(ad_dictionary):
    return ad_dictionary["type"]

def grab_ad_date(ad_dictionary):
    return ad_dictionary["date"]

def assert_ad_type_is_properly_defined(ad_dictionary):
    ad_type = grab_ad_type(ad_dictionary)
    set_of_all_ad_types = set(item for item in AdType) 
    assert ad_type in set_of_all_ad_types

def assert_ad_name_is_properly_defined(ad_dictionary):
    ad_name = grab_ad_name(ad_dictionary)
    assert isinstance(ad_name, str)
    assert len(ad_name) > 0

def assert_ad_coord_is_properly_defined(ad_dictionary):
    ad_coord = grab_ad_coordinates(ad_dictionary)
    lat, long = ad_coord
    assert lat >= -90 and lat <= 90
    assert long >= -180 and long <= 180

def assert_ad_price_is_properly_defined(ad_dictionary):
    ad_price = grab_ad_price(ad_dictionary)
    assert isinstance(ad_price, float)
    assert ad_price >= 0

def assert_ad_description_is_properly_defined(ad_dictionary):
    ad_description = grab_ad_description(ad_dictionary)
    assert isinstance(ad_description, str)

def assert_ad_link_is_properly_defined(ad_dictionary):
    ad_link = grab_ad_link(ad_dictionary)
    assert validators.url(ad_link)

def assert_ad_date_is_properly_defined(ad_dictionary):
    ad_date = grab_ad_date(ad_dictionary)
    assert isinstance(ad_date, datetime)
    assert ad_date.tzname() == "UTC"