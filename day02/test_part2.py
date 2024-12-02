import pytest

from day02.part1 import check_level_line
from day02.part1 import check_level_decrease


@pytest.mark.parametrize("values, expected",
                         [
                             ([1, 2, 3, 4, 5], True),
                             ([1, 2, 2, 4, 5], False),
                             ([10, 12, 15, 18, 21], True),
                             ([1, 2, 2, 4, 5], False),
                             ([10, 10, 12, 15, 18, 21], True),
                          ]
                         )
def test__your_method_here(values, expected):
    result = check_level_line(values)
    assert result == expected
