from city_functions import city_country

def test_city_country():
    """Check if the result is 'Santiago, Chile - population xxx'."""
    citycountry = city_country('paris', 'france', '1500000')
    assert citycountry == "Paris, France - Population 1500000"