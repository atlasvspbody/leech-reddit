from django.db import models
from django.contrib.auth.models import User

class SubReddit(models.Model):
    name = models.CharField(max_length=50 ,verbose_name="Name")
    
    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=50 ,verbose_name="Title")
    selftext = models.TextField(verbose_name="SelfText")
    permalink = models.URLField(verbose_name="Permalink")
    
class Rule(models.Model):
    regex = models.CharField(max_length=100 ,verbose_name="Regex")
    alias = models.CharField(max_length=50 ,verbose_name="Alias", null=True, default=None, blank=True)
    
    def __str__(self):
        return self.regex if self.alias=='' else self.alias
    
class Alert(models.Model):
    rule = models.ForeignKey(Rule)
    subreddit = models.ForeignKey(SubReddit)
    
    def __str__(self):
        return self.rule.regex 
    
class BotFind(models.Model):
    subreddit = models.ForeignKey(SubReddit)
    date = models.DateTimeField(verbose_name="Date")

class QuequeAlert(Post):
    rule = models.ForeignKey(Rule)
    
class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    
    def __str__(self):
        return self.user_auth.username
