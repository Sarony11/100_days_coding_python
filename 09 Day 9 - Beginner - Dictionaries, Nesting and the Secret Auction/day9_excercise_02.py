"""
In this excercise we learn:
- How to manipulate with a list of dictionaries.
"""
travel_log = [
    {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"],
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgard"],
    },
]
# CREATE function to make work the code bellow
def add_new_country(country, visits, cities = []):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

# DO NOT change code bellow
add_new_country("Rusia", 12, ["Moscou"])
print(travel_log)