import csv

def read_population_data(file_path):
    """Читання даних з файлу і повернення списку країн з їх площею та населенням"""
    data = []
    with open(file_path, 'r', encoding='utf-16') as file:
        reader = csv.reader(file)
        for row in reader:
            country, area, population = row
            data.append({
                "country": country,
                "area": float(area),
                "population": int(population)
            })
    return data

def sort_by_area(data):
    """Сортування за площею країни"""
    return sorted(data, key=lambda x: x['area'])

def sort_by_population(data):
    """Сортування за населенням країни"""
    return sorted(data, key=lambda x: x['population'])
