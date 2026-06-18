# from normalizer import normalize_year
# from normalizer import normalize_ticker

# print(normalize_year("2023-24"))
# print(normalize_year("2024"))

# print(normalize_ticker(" abb "))
# print(normalize_ticker("adanient"))









from src.etl.normalizer import normalize_year
from src.etl.normalizer import normalize_ticker


def test_year_1():
    assert normalize_year("2023-24") == "2023"


def test_year_2():
    assert normalize_year("2024") == "2024"


def test_year_3():
    assert normalize_year(None) is None


def test_ticker_1():
    assert normalize_ticker("abb") == "ABB"


def test_ticker_2():
    assert normalize_ticker(" adanient ") == "ADANIENT"


def test_ticker_3():
    assert normalize_ticker(None) is None