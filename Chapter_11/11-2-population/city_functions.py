def city_country(city, country, population=None):
    """A function to return a single string of city and country."""
    citycountry = f"{city}, {country} - population {population}"
    return citycountry.title()