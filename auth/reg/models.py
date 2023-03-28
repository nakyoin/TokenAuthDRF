from django.contrib.gis.geoip2.resources import Country
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.fields import related


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Вы не ввели Email')
        if not username:
            raise ValueError('Вы не ввели Логин')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            *extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True)


class User(AbstractBaseUser, PermissionsMixin):
        id = models.AutoField(primary_key=True, unique=True)
        username = models.CharField(max_length=50, unique=True)
        email = models.EmailField(max_length=100, unique=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=True)
        is_superuser = models.BooleanField(default=True)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']

        objects = MyUserManager()

        def __str__(self):
            return self.email

class Product(models.Model):
    prodname = models.CharField(max_length=100)
    prodman = models.ForeignKey('ProductManager', related_name = "productsmanager", on_delete=models.CASCADE)
    country = models.ForeignKey('CountryProd', related_name = "cpuntryy", on_delete=models.CASCADE)
    new_or_not = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=1, max_digits=100)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.prodname


class ProductManager(models.Model):
    prodmanname = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.prodmanname

class CountryProd(models.Model):
    countryname = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.countryname

class Cart(models.Model):
    cartproducts = models.ManyToManyField('Product', related_name='Корзина')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return str(self.cartproducts)

class Order(models.Model):
    numoforder = models.IntegerField(default=None)
    allprice = models.DecimalField(max_digits=100, decimal_places=10)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.numoforder)