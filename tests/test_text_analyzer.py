import pytest
from text_analyzer import read_population_data, sort_by_area, sort_by_population

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


# Тестування функції сортування за населенням
@pytest.mark.parametrize("data, expected", [
    (
        [
            {"country": "A", "population": 1000},
            {"country": "B", "population": 5000},
            {"country": "C", "population": 3000}
        ],
        [
            {"country": "A", "population": 1000},
            {"country": "C", "population": 3000},
            {"country": "B", "population": 5000}
        ]
    )
])
def test_sort_by_population(data, expected):
    assert sort_by_population(data) == expected


# Тестування функції читання файлу для правильного формату даних
def test_read_population_data_valid():
    # Створюємо тимчасовий файл для тестування
    test_file = "test_population_data.txt"
    with open(test_file, "w", encoding="utf-16") as file:
        file.write("Україна, 603628, 41300000\n")
        file.write("Канада, 9984670, 38005238\n")

    result = read_population_data(test_file)

    assert len(result) == 2  # Перевірка, що дані зчитані правильно
    assert result[0]["country"] == "Україна"  # Перевірка країни
    assert result[1]["area"] == 9984670  # Перевірка площі

    # Видалити тимчасовий файл після тесту
    import os
    os.remove(test_file)