from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='image/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50,null=True )


    def __str__(self):
        return self.name

class Cart(models.Model):

        name = models.CharField(max_length=50)
        Quantity = models.CharField(max_length=50)
        Price = models.CharField(max_length=50)
        Status = models.CharField(max_length=50)
        Customer_id = models.CharField(max_length=50)

        def __str__(self):
            return self.name


class Customer_Order(models.Model):
    name = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Status = models.CharField(max_length=50, default=" ")

    Customer_id = models.CharField(max_length=50, default=" ")
    CustomerName = models.CharField(max_length=50)
    CustomerAddress = models.CharField(max_length=50)
    CustomerContact = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Customer_feedback(models.Model):

    name = models.CharField(max_length=50, null=True )
    email = models.CharField(max_length=50, null=True )
    feedback = models.CharField(max_length=50)




    def __str__(self):
        return self.name





