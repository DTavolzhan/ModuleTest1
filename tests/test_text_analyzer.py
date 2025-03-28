import pytest
from text_analyzer import  sort_by_area

# Фікстура для тестових даних
@pytest.fixture
def sample_data():
    return [
        {"country": "Україна", "area": 603628, "population": 41300000},
        {"country": "Канада", "area": 9984670, "population": 38005238},
        {"country": "США", "area": 9833517, "population": 331002651},
        {"country": "Індія", "area": 3287263, "population": 1380004385},
        {"country": "Китай", "area": 9596961, "population": 1395380000}
    ]
# Тестування функції сортування за площею
@pytest.mark.parametrize("data, expected", [
    (
        [
            {"country": "A", "area": 300},
            {"country": "B", "area": 500},
            {"country": "C", "area": 100}
        ],
        [
            {"country": "C", "area": 100},
            {"country": "A", "area": 300},
            {"country": "B", "area": 500}
        ]
    )
])
def test_sort_by_area(data, expected):
    assert sort_by_area(data) == expected