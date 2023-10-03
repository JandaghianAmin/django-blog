from django.db import models
from django.contrib.auth.models import(BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserManager(BaseUserManager):
    """ 
        custome user model for our app
    """
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The Email must be filled")
        email =self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if not extra_fields.get('is_staff'):
            raise ValueError("super user must is_staff true")
        if not extra_fields.get('is_superuser'):
            raise ValueError("super user must is_superuser true")
        return self.create_user(email,password,**extra_fields)
            
            



class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=250,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # is_verify = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =  models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    imgae = models.ImageField(blank=True,null=True)
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =  models.DateField(auto_now=True)

    def __str__(self):
        return self.user.email
    
@receiver(post_save,sender= User)
def save_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)