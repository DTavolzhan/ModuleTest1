import csv
import os


def read_population_data(file_path):
    """Читання даних з файлу і повернення списку країн з їх площею та населенням"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл за вказаним шляхом {file_path} не знайдено.")

    data = []
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    raise ValueError(f"Невірний формат рядка: {row}")
                country, area, population = row
                try:
                    data.append({
                        "country": country,
                        "area": float(area),
                        "population": int(population)
                    })
                except ValueError:
                    raise ValueError(f"Невірний формат чисел у рядку: {row}")
    except Exception as e:
        raise e

    return data


def sort_by_area(data):
    """Сортування за площею країни"""
    return sorted(data, key=lambda x: x['area'])


def sort_by_population(data):
    """Сортування за населенням країни"""
    return sorted(data, key=lambda x: x['population'])


if __name__ == "__main__":
    # Запитуємо шлях до файлу з даними
    file_path = input("Введіть шлях до файлу з даними: ")

    # Читаємо дані з файлу
    population_data = read_population_data(file_path)

    # Сортуємо за площею
    sorted_by_area = sort_by_area(population_data)
    print("Сортування за площею:")
    for country in sorted_by_area:
        print(f"{country['country']}: {country['area']} км²")

    print("\n")  # Розділяємо виведення

    # Сортуємо за населенням
    sorted_by_population = sort_by_population(population_data)
    print("Сортування за населенням:")
    for country in sorted_by_population:
        print(f"{country['country']}: {country['population']} осіб")
