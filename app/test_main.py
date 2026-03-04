import pytest
from app import main


class TestConvertToHumanAges:

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
    )
    def test_converts_ages_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected: list[int]
    ) -> None:
        assert main.get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            (-1, 28),
            (28, -1),
            (-5, -7),
        ],
    )
    def test_raises_value_error_for_negative_ages(
        self,
        cat_age: int,
        dog_age: int
    ) -> None:
        with pytest.raises(ValueError):
            main.get_human_age(cat_age, dog_age)
