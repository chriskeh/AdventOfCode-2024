import pytest

from day02.part2 import check_level_increase
from day02.part2 import check_level_decrease


@pytest.mark.parametrize("values, versuch, expected",
                         [
                             ([1, 1, 3, 4, 5], 0, True),
                             ([1, 1, 3, 4, 5], 1, False),
                             ([1, 2, 3, 4, 4], 0, True),
                             ([1, 2, 3, 4, 4], 1, False),
                             ([1, 2, 3, 4, 5], 0, True),
                             ([10, 10, 10, 10], 0, False),
                             ([10, 10, 10, 10], 0, False),
                             ([1, 2, 2, 4, 3], 0, False),
                             ([1, 2, 2, 4, 5], 1, False),
                             ([10, 12, 15, 18, 21], 0, True),
                             ([1, 3, 2, 4, 5], 0, True),
                             ([1, 3, 2, 4, 5], 1, False),
                             ([10, 10, 12, 15, 18, 21], 0, True),
                             ([1, 2, 2, 2, 4, 5], 0, False),
                             ([1, 2, 2, 2, 4, 5], 1, False),
                          ]
                         )
def test__your_method_here(values, versuch, expected):
    result = check_level_increase(values, versuch)
    assert result == expected
