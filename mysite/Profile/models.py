from django.db import models
#from django.core.urlresolvers import reverse

class entries(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=25)
    date_of_birth = models.DateTimeField()
    skills = models.TextField()
    more_about_you = models.TextField()
    image = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
     #   return reverse('profile:detail',kwargs={'pk': self.pk})


    #def __str__(self):
     #   return self.title

