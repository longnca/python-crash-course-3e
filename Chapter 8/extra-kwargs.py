# Some examples of **kwargs

# 1
def personal_info(**kwargs):
    """Define a function to record personal information"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
personal_info(name = 'John', age=30, city='London')

personal_info(name='Mandy', location='Calgary', occupation='doctor')


# 2 Combining *args and **kwargs
def register(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

register('Alice', 'Bob', 'Charlie', age=30, occupation = 'doctor')


# 3 Using **kwargs with Function Calls
def create_profile(name, email, city):
    print(f"Name: {name}, Email: {email}, City: {city}")

details = {"name": "Emily",
           "email": "emily@email.com",
           "city": "Toronto"}

create_profile(**details)