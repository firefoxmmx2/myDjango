from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=['name']
        
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    class Meta:
        ordering=['email']

class BookMananger(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()

class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(author="Roald Dahl")

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True)
    num_pages = models.IntegerField(blank=True,null=True)
    #objects = BookMananger()
    objects = models.Manager()
    dahl_objects = DahlBookManager()

    def __unicode__(self):
        return self.title
    class Meta:
        ordering=['title']
