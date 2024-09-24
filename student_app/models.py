from django.db import models

# Create your models here.
class Student_Details(models.Model):
    student_id=models.IntegerField(primary_key='true')
    student_name=models.CharField(max_length=200)
    student_class=models.CharField(max_length=50)
    student_contact=models.IntegerField()
    student_image=models.ImageField(upload_to='images')


    class Meta:
        db_table="student_table"





