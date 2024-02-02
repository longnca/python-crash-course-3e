# I'm gonna use **kwargs as the additional keyword arguments 

def build_profile(first, last, **kwargs):
    user_info = {}
    user_info['first name'] = first
    user_info['last name'] = last
    for key, value in kwargs.items():
        user_info[key] = value
    return user_info

user_profile = build_profile('Aaron', 'Carter',
                             age = '28',
                             location = 'US')

print(user_profile)