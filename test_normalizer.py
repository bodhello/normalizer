# ================
#      Tests
# ================
from normalizer import *


def test_timestamp_normalizer():
    assert timestamp_normalizer("3/12/14 12:00:00 AM") == "2014-03-12T03:00:00-0500"
    assert timestamp_normalizer("3/12/16 11:01:00 PM") == "2016-03-13T02:01:00-0500"


def test_zip_normalizer():
    assert zip_normalizer("3") == "00003"
    assert zip_normalizer("99999") == "99999"
    assert zip_normalizer("1000000000") == "10000"


def test_name_normalizer():
    assert name_normalizer("Superman übertan") == "SUPERMAN ÜBERTAN"
    assert name_normalizer("株式会社スタジオジブリ") == "株式会社スタジオジブリ"


def test_duration_to_seconds():
    assert duration_to_seconds("1:32:33.123") == 5553.123
    assert duration_to_seconds("31:23:32.123") == 113012.123
