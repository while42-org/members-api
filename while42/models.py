from django.db import models
from faker import Factory


class Chapter(models.Model):
    city = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.city

    class Meta:
        ordering = ["city"]


class Member(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    work = models.CharField(max_length=200, blank=False)
    school = models.CharField(max_length=200, blank=True)
    graduation_year = models.IntegerField(max_length=4, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    chapter = models.ManyToManyField(Chapter)

    def __unicode__(self):
        return u"%s %s " % (self.last_name, self.first_name)

    def get_photos(self):
        return Photo.objects.filter(user=self.id)

    def get_fullname(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_random_photo(self):
        return Photo.objects.filter(user=self.id).order_by('?').first()

    @staticmethod
    def get_fakename():
        fake = Factory.create('fr_FR')
        return (fake.name() for _ in xrange(3))


class Photo(models.Model):
    photo = models.URLField(blank=False)
    user = models.ForeignKey(Member)

    def __unicode__(self):
        return u"%s" % self.photo
