from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(seld, postdata):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['pw']) < 8:
            errors['pw'] = "Your password must be at least 8 characters long"
        if len(postdata['fname']) < 2 or len(postdata['lname']) < 2:
            errors['name'] = "Your name must be at least 2 characters long"
        if not email_checker.match(postdata['email']):
            errors['email'] = "Invalid email"
        if postdata['pw'] != postdata['confpw']:
            errors['pw'] = "Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = UserManager()
    # user_likes(liked_posts)
    # user_messages
    # user_comments

class Wall_Message(models.Model):
    message = models.CharField(max_length=255)
    poster= models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    # post_comments

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name='post_comments', on_delete=models.CASCADE)