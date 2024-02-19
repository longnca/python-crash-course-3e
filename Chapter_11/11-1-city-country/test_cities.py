from city_functions import city_country

def test_city_country():
    """Check if the result is 'Santiago, Chile'."""
    citycountry = city_country('paris', 'france')
    assert citycountry == "Paris, France"