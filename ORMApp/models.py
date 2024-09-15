from django.db import models

# Create your models here.
class Deportment(models.Model):
    dptno = models.IntegerField(primary_key = True)
    dptname = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.dptname
    
class Employee(models.Model):
    empno = models.IntegerField(primary_key = True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    deportment = models.ForeignKey(Deportment,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.empname
    
class person(models.Model):
    pno = models.IntegerField(primary_key = True)
    pname=models.CharField(max_length=20)
    address=models.TextField()

class Aadhar(models.Model):
    ano=models.IntegerField(primary_key=True)
    person=models.OneToOneField(person,on_delete=models.CASCADE)

class student(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=20)
    address = models.TextField()

class course(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length = 20)
    students = models.ManyToManyField(student)

class Base1(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname=models.CharField(max_length = 20)
    
    class Meta:
        abstract = True

class child1(Base1):
    salay = models.IntegerField()
class child2(Base1):
    address = models.TextField()

class Base2(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname =models.CharField(max_length = 20)
     
class Child(Base2):
    salary = models.IntegerField()


class EmployeeProxy(Employee):
    class Mete:
        proxy = True
        ordering = ['-salary']