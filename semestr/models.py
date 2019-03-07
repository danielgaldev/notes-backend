from django.db import models


class Semester(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return ''.join([str(self.number), '. semester'])
    

class Class(models.Model):
    name = models.TextField(max_length=50)
    credit = models.IntegerField()
    parent_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Requirement(models.Model):
    name = models.TextField()
    due = models.DateField(auto_now_add=False)
    parent_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
