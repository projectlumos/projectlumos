from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class RowInfo(models.Model):
    """
    Abstract class used to common columns across the models file
    """
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Technology(RowInfo):
    """
    Store the different technologies
    """
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(null=True, blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Technology, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'technology'
        verbose_name_plural = 'technologies'
        ordering = ['name']

class Domain(RowInfo):
    """
    Stores the different domains across several technologies
    """
    technology = models.ManyToManyField(Technology)
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(null=True, blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Domain, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'domain'
        ordering = ['name']


class Resources(RowInfo):
    """
    Used to save the resources (the most atomic component)
    """
    technology = models.ManyToManyField(Technology)
    domain = models.ManyToManyField(Domain)
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(null=True, blank=True)
    link = models.TextField()
    diff_levels = (
                (0, 'Beginner'),
                (1, 'Intermediate'),
                (2, 'Advanced'),
    )
    diff_level = models.IntegerField(choices=diff_levels)
    diff_sort = models.IntegerField(default=999)
    data_type = (
                (0, 'Video'),
                (1, 'Article'),
                (2, 'Interactive Site'),
                (3, 'Other')
                )
    media_type = models.IntegerField(choices=data_type, default=3)
    is_youtube = models.BooleanField(default=False)
    slug = models.SlugField()
    # quality parameters
    quality_helpfulness = models.IntegerField(default=0)
    quality_simplicity = models.IntegerField(default=0)
    quality_recommendation = models.IntegerField(default=0)
    quality_placement = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if ("youtube" in self.link) or ("youtu.be" in self.link):
            self.is_youtube = True
        super(Resources, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'resources'
        verbose_name_plural='resources'


class QualityFeedback(RowInfo):
    """
    Stores the different domains across several technologies
    """
    resource = models.ForeignKey(Resources)
    helpfulness = models.FloatField(default=0)
    simplicity = models.FloatField(default=0)
    placement = models.FloatField(default=0)
    recommendation = models.FloatField(default=0)
    aggr_calculation = models.BooleanField(default=False)
    
    def __str__(self):
        return self.resource.name
    
    class Meta:
        db_table = 'quality_feedback'


# TO DO
# career to domain linking
# indexing based on explain plan