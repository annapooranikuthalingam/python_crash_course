"""
Write a function called city_country() that takes in the name of a city and its country. The function
 should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_names(city,country):
    city=city.title()
    country=country.title()
    print(f'"{city}, {country}"')

city_names('sfo','usa')
city_names('mumbai','india')
city_names('chicago','USA')