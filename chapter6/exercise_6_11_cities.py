"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in,
its approximate population, and one fact about that city. The keys for each city’s dictionary should be
something like country, population, and fact. Print the name of each city and all of the information
you have stored about it.
"""

cities={'new york':{'country':'USA','population':'23461111','fact':'popular'},
        'chicago':{'country':'USA','population':'432178','fact':'freezing'},
        'texas':{'country':'USA','population':'235555','fact':'stormy'}}

for key,value in cities.items():
    print("------------------")
    print(f"City Name is {key}.It is located in {value['country']} and has a population of {value['population']} and a fact about it is {value['fact']}")