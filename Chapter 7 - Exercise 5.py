def describe_city(city, country='sudan'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Khartoum')
describe_city('Makah', 'Saudi Arabia')
describe_city('omdurman')