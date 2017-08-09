from django.db import models


class startups(models.Model):
    company_name = models.CharField(max_length=100)
    #enrollment = models.CharField(max_length=25)
    #date_of_birth = models.DateTimeField()
    co_founders = models.TextField()
    details = models.TextField()
    logo = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title
