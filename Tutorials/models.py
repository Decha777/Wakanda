from django.db import models
from datetime import datetime

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now)
    def __str__(self):
          return 'id: {} | Title: {}'.format(self.id ,self.tutorial_title)


class CoursePage(models.Model):
     title=models.CharField(max_length=200)
     catagory=models.CharField(max_length=200)
     series=models.CharField(max_length=200)
     date=models.DateTimeField('date published', default=datetime.now)
     developer=models.CharField(max_length=200)
     content=models.TextField()

     def __str__(self):
         return 'ID: {} | Title: {}'.format(self.id ,self.title)
     



class AccountPage(models.Model):
     fname=models.CharField(max_length=200)
     lname=models.CharField(max_length=200)
     username=models.CharField(max_length=200)
     password=models.CharField(max_length=200)
     email=models.CharField(max_length=200)
     birthdate=models.DateTimeField(default=datetime.now)
     accessible=models.BooleanField(default=False)

     def __str__(self):
        return 'ID: {} | Name: {}'.format(self.id ,self.fname)
     
    

class PaymentPage(models.Model):
     username=models.CharField(max_length=200)
     password=models.CharField(max_length=200)
     


class FreelanceJobPage(models.Model):
     username=models.CharField(max_length=200)
     jobs=models.CharField(max_length=200)
     qualification=models.CharField(max_length=200)


class ToolsPage(models.Model):
     username=models.CharField(max_length=200)


class IncentivePage(models.Model):
     username=models.CharField(max_length=200)


class AboutUsPage(models.Model):
     username=models.CharField(max_length=200)


