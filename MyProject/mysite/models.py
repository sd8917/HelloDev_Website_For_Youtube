from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

TYPE = (("free" ,"free"),("paid", "paid"))

class Course(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=2000)
    
    thumbnail_url = models.CharField(max_length=1000)
    typecourse = models.CharField(
        max_length=20,
        choices=TYPE,
        default='free'
    )
    course_length = models.CharField(max_length=100)
    description = models.CharField(max_length=2000 ,default="your text here ...")
  
    def __str__(self):
        return self.title
class Section(models.Model):
    title = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=500)
    video_url = models.CharField(max_length=1000)
    course =     models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


