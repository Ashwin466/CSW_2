from django.db import models

# Create your models here.s
class Employee(models.Model):
    # Emp_id = models.AutoField()
    Emp_name = models.CharField(max_length=100)
    Emp_Email = models.EmailField()
    Emp_Mobile = models.IntegerField()


    def __str__(self) -> str:
        return self.Emp_name

class User1(models.Model):
    u_name = models.CharField()
    U_pass = models.CharField()
    u_mail = models.EmailField()
    u_mob = models.IntegerField()
    u_address = models.CharField(max_length=200, null=True, blank=True)

class Blog(models.Model):
    btext = models.CharField(max_length=100, null=True, blank=True)
    bdate = models.CharField(max_length=11)
    btime = models.CharField(max_length=11)
    bimage = models.ImageField(upload_to="image")

    def __str__(self) -> str:
        return self.btext
