from django.db import models

class Register(models.Model):
    rid=models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    blogurl = models.URLField(max_length=200)
    contact=models.IntegerField()
    country=models.CharField(max_length=120)
    city=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    collegename=models.CharField(max_length=120)
    branch=models.CharField(max_length=120)
    stream=models.CharField(max_length=120)
    role=models.CharField(max_length=120)
    proof=models.FileField(upload_to='proof/')
    discribe=models.CharField(max_length=200)
  

   
    def __str__(self):
        return self.name
class BookItem(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default="hari@gmail.com.com")
    price = models.IntegerField()
    description = models.CharField(max_length=5000)
    dkey=models.CharField(max_length=220,default="book")
    image = models.FileField(upload_to='proof/',default='proof/default_image.jpeg')

    def __str__(self):
        return self.name

class blogs(models.Model):
    title=models.CharField(max_length=50)
    email = models.EmailField(default="hari@gmail.com")
    author=models.CharField(max_length=50,default="Raghuram")
    content=models.CharField(max_length=1000)
    date=models.DateField()
    image=models.FileField(upload_to='images/', default='images/default_image.jpg')

    def __str__(self):
        return self.title  
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    email = models.EmailField(default="hari@gmail.com.com")
    seller_name = models.CharField(max_length=100)
    num_books = models.IntegerField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    describe=models.CharField(max_length=200)
    stream = models.CharField(max_length=100)
    is_series = models.CharField(max_length=20)
    image = models.ImageField(upload_to='proof/')
    
    def __str__(self):
        return self.book_name    
class mainblog(models.Model):
    Author=models.CharField(max_length=50)
    Title=models.CharField(max_length=120)
    ukey=models.CharField(max_length=200,default="blog")
    link = models.URLField(max_length=200, blank=True)
    description = models.CharField(max_length=5000)
    dkey=models.CharField(max_length=220,default="blog")
    date=models.DateField()

    def __str__(self):
        return self.Author

class uploadblog(models.Model):
    email = models.EmailField(default="demo@gmail.com")
    title=models.CharField(max_length=120)    
    authorname=models.CharField(max_length=50)
    ukey=models.CharField(max_length=200,default="blog")
    link=models.URLField(max_length=200, blank=True)
    description = models.CharField(max_length=5000)
    dkey=models.CharField(max_length=220,default="blog")
    stream=models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Customer(models.Model):
    book_name = models.CharField(max_length=100)
    email = models.EmailField(default="demo@gmail.com")
    phone=models.IntegerField(default=9867534210)
    full_name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name