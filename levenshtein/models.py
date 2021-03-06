from django.db import models


class Levenshtein(models.Model):
    """This model holds 2 text values and their levenshtein_value"""

    text_1 = models.TextField()
    text_2 = models.TextField()
    distance = models.IntegerField(null=True, blank=True)
    ratio = models.FloatField(null=True, blank=True)

    # Timestamps
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Levenshtein Value %s" % self.levenshtein_value
