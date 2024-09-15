from django.db import models
from django.db.models.signals import pre_save,post_save
from django.core.mail import send_mail
from django.conf import settings
# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(primary_key= True)
    pname = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=4)
    pimage = models.ImageField(upload_to='images/')

def pre_save_handler(sender,instance,*args,**kwargs):
    print('Pre save signal is raised')
    #print(sender)
    #print(instance.pid,instance.pname,instance.price)
    
    msg = '''Hello sir,
            below change has happend in product table.
            {}{}{}'''.format(instance.pid,instance.pname,instance.price)
    subject = 'Test mail'
    to_list = ['lovelynaveen113@gmail.com']
    send_mail(subject,msg,settings.EMAIL_HOST_USER,to_list)

'''def post_save_handler(sender,instance,created,*args,**kwargs):
    print('Post save signal is raised')
    print(sender)
    print(instance)
    print(created)

post_save.connect(post_save_handler,sender=Product)'''
pre_save.connect(pre_save_handler,sender=Product)