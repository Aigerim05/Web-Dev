from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField(max_length=255)

class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    


    

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=1)  


    

# API for creating vacancy (in some company and in some position)


