from django.db import models

# Create your models here.

class Pizza(models.Model):
    """Names of the pizzas."""
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.name 
    
class Topping(models.Model):
    """Names of the toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name