import sys
import pytest

sys.path.append("../")
from validate_sa_id.validate_sa_ids import (
    checksum_digit,
    citizenship,
    day,
    gender,
    month,
    year,
    validate_input,
    validate_sa_id,
)

test_cases = [
    ("978022333", False),
    ("907366182280", False),
    ("0782039844783493912345", False),
    ("279339438413794", False),
    ("2790180237618", False),
    ("0002j25090680", False),
]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert validate_input(input_num) == expected_output


test_cases = [
    ("0k02525090680", False),
    ("0782039844783493912345", True),
]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert year(input_num) == expected_output


test_cases = [("203452345583080", True), ("084K368837348449", False)]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert month(input_num) == expected_output


test_cases = [("00027KK903203484589", False), ("1279404534449489", True)]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert day(input_num) == expected_output


test_cases = [
    ("0965421234880", "Female"),
    ("2834500990808", "Female"),
    ("2019458978677", "Male"),
    ("8451129999111", "Male"),
    ("980255h586098", False),
]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert gender(input_num) == expected_output


test_cases = [
    ("0299049023823", False),
    ("0299049023023", "SA citizen"),
    ("0299049023123", "permanent resident"),
]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert citizenship(input_num) == expected_output


test_cases = [
    ("2001094800086", False),
    ("2001014800086", True),
    ("2909035800085", True),
]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert checksum_digit(input_num) == expected_output


test_cases = [
    ("2001094800086", False),
    ("2001014800086", True),
    ("2909035800085", True),
]


@pytest.mark.parametrize("input_num, expected_output", test_cases)
def test_function(input_num, expected_output):
    assert validate_sa_id(input_num) == expected_output
