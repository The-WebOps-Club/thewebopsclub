from django.db import models

# Create your models here.
class Update(models.Model):
    title     = models.CharField(max_length = 50, blank = False)
    message   = models.TextField()
    timestamp = models.TimeField(auto_now = True, editable = False)
    
    def __unicode__(self):
        return self.title
