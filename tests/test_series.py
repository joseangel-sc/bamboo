import pytest

from bamboo.series import Series


def test_valid_option():
    valid = [1, 2, 3]
    series = Series(valid)
    assert series.values == valid

    valid.append(None)
    series = Series(valid)
    assert series.values == valid


def test_not_valid():
    non_valid = [1, 2, 'A']
    with pytest.raises(Exception, match="Only one type .* in a Series got"):
        Series(non_valid)


def test_print_format():
    valid = [1, 2, 3, None]
    series = Series(valid)
    print_string = series.__str__()
    expected = "0    1\n1    2\n2    3\n3    None\ndtype: <class 'int'>"
    assert expected == print_string
