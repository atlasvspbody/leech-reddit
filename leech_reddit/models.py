from django.db import models

class SubReddit(models.Model):
    name = models.CharField(max_length=50 ,verbose_name="Name")
    alias = models.CharField(max_length=50 ,verbose_name="Alias")

class Post(models.Model):
    title = models.CharField(max_length=50 ,verbose_name="Title")
    selftext = models.TextField(verbose_name="SelfText")
    permalink = models.URLField(verbose_name="Permalink")
    
class Rule(models.Model):
    regex = models.CharField(verbose_name="Regex")
    
class Alert(models.Model):
    rule = models.ForeignKey(Rule)
    subreddit = models.ForeignKey(SubReddit)
    
class BotFind(models.Model):
    subreddit = models.ForeignKey(SubReddit)
    date = models.DateTimeField(verbose_name="Date")

class QuequeAlert(Post):
    rule = models.ForeignKey(Rule)
    