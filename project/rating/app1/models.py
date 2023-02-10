from django.db import models
from django.contrib.auth.models import User

class NewCourse(models.Model):
	
	Course_name = models.CharField(max_length=100)
	Course_star_rating = models.IntegerField()
	Course_comments = models.IntegerField()

	def __str__(self):
		return self.Course_name


class Comment(models.Model):
    course = models.ForeignKey(NewCourse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
