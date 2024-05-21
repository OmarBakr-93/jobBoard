from django.db import models

# Create your models here.

job_tybe = (
    ('full time','full time'),
    ('part time','part time'),
)
class Job(models.Model):
    
    title = models.CharField(max_length=100)
    job_type= models.CharField(max_length=15,choices=job_tybe)
    description = models.CharField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    