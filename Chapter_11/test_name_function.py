from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Bradley M. Cooper' work?"""
    formatted_name = get_formatted_name('bradley', 'cooper')
    assert formatted_name == 'Bradley Cooper'

def test_first_last_middle_name():
    """Do names like 'John F. Kennedy' work?"""
    formatted_name = get_formatted_name('john', 'kennedy', 'f.')
    assert formatted_name == 'John F. Kennedy'