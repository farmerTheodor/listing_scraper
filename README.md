# WIP 
# listing_scraper
## Sites supported
Scrapes from your favorite buy/sell sites. Currently only supports:
* Craigslist

Future buy/sell sites:
* FB marketplace(somewhat working just have to figure out how queries will work)
* Kijiji

## Standardized Data
The current standard information taken from a listing is:
* name
* date(UTC)
* price
* coordinates(lat,lon)
* type(Item, Rental)
* description
* link(to original listing)

## The plan is to:
* Scrape multiple sites using the same queries.
* Throw the results of the queries in a postgres database.
* Write some SQL to make use of the results

## Setup:
### src
* install the file /src/requirements.txt using pip 
* Set Environment variable NOMINATIM_EMAIL_ID to be whatever email you can be reached at

### test
* install src
* install the file /test/requirements.txt using pip 
* run using pytest

## TODO:
* Throw results from craigslist into database
* Add FB marketplace support
* Add multiple queries support
