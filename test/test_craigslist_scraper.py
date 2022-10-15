import pytest
from src import CraigslistScraper
from test.helpers.ad_definition import assert_ad_coord_is_properly_defined, assert_ad_date_is_properly_defined, assert_ad_description_is_properly_defined, assert_ad_is_properly_defined, assert_ad_link_is_properly_defined, assert_ad_name_is_properly_defined, assert_ad_price_is_properly_defined, assert_ad_type_is_properly_defined

@pytest.fixture(scope="module")
def list_of_ads():
    scraper = CraigslistScraper((49.2796, -123.1219))
    list_of_ads = scraper.get_all_ads("monitor")
    yield list_of_ads

@pytest.fixture(scope="module")
def single_ad(list_of_ads):
    yield list_of_ads[0]

def test_environment():
    assert True

def test_can_grab_ads(list_of_ads):
    for ad in list_of_ads:
        assert_ad_is_properly_defined(ad)
    assert len(list_of_ads) > 0

def test_ad_type_is_defined(single_ad):
    assert_ad_type_is_properly_defined(single_ad)


def test_ad_name_is_defined(single_ad):
    assert_ad_name_is_properly_defined(single_ad)


def test_ad_price_is_defined(single_ad):
    assert_ad_price_is_properly_defined(single_ad)


def test_ad_coord_is_defined(single_ad):
    assert_ad_coord_is_properly_defined(single_ad)

def test_ad_description_is_defined(single_ad):
    assert_ad_description_is_properly_defined(single_ad)

def test_ad_link_is_defined(single_ad):
    assert_ad_link_is_properly_defined(single_ad)

def test_ad_date_is_defined(single_ad):
    assert_ad_date_is_properly_defined(single_ad)