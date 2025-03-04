from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
   def create_user(self, email,passwod=None, **kwargs):
      if not email:
         raise ValueError('Users must have an email address')
      email = self.normalize_email(email)
      user = self.model(email=email, **kwargs)
      user.set_password(passwod)
      user.save(using=self._db)
      return user
   def create_superuser(self,email,password=None,**kwargs):
      kwargs.setdefault("is_staff",True)
      kwargs.setdefault("is_superuser",True)
      if kwargs.get("is_staff") is not True:
         raise ValueError('Superuser must be True is_staff') 
      if kwargs.get("is_superuser") is not True:
         raise ValueError('Superuser must be True is_superuser')
      return self.create_user(email=email, passwod=password, **kwargs)
   
      


class CustomUser(AbstractUser):
   COUNTRY_CHOICES = [
      ("UZB", "UZBEKISTAN"),
      ("KAZ", "KAZAKHSTAN"),
      ("KYR", "KIRGIZISTAN")
   ]
   username = None
   first_name = models.CharField(max_length=50, blank=True, null=True)
   last_name = models.CharField(max_length=50, blank=True, null=True)
   email = models.EmailField(unique=True)
   phone_number = models.CharField(max_length=15, blank=True, null=True)
   address1 = models.CharField(max_length=250, blank=True, null=True)
   address2 = models.CharField(max_length=50, blank=True, null=True)
   country = models.CharField(max_length=3, choices=COUNTRY_CHOICES, default="UZB")
   city = models.CharField(max_length=50, blank=True, null=True)
   state = models.CharField(max_length=50, blank=True, null=True)
   zipcode = models.CharField(max_length=50, blank=True, null=True)
   objects = CustomUserManager()
   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = []
   
class Category(models.Model):
   title = models.CharField(max_length=50)
   image = models.ImageField(upload_to="image/", blank=True, null=True)
   
   def __str__(self):
      return self.title
   class Meta:
      verbose_name = "Category" 
      verbose_name_plural = 'Categories'  
      
class SubCategory(models.Model):
   title = models.CharField(max_length=50)
   image = models.ImageField(upload_to="image/", blank=True, null=True)
   description = models.TextField(blank=True, null=True)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
   
   def __str__(self):
      return self.title
      
   class Meta:
      verbose_name = "SubCategory" 
      verbose_name_plural = 'SubCategories'
      
class Offer(models.Model):
      title = models.CharField(max_length=100)
      persent = models.IntegerField(default=10)
      image = models.ImageField(upload_to="image/", blank=True, null=True)
      
      def __str__(self):
         return self.title
      
      class Meta:
         verbose_name = "Offer" 
         verbose_name_plural = 'Offers'