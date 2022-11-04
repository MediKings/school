from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model


User = get_user_model()


class Universite(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='picture/')
    logo = models.ImageField(upload_to='logo/')
    about = models.TextField()
    url = models.URLField()
    contact = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Universite, self).save(*args, **kwargs)


class Faculte(models.Model):
    univ = models.ForeignKey(Universite, on_delete=models.CASCADE, related_name='universite')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Faculte, self).save(*args, **kwargs)


class Departement(models.Model):
    fac = models.ForeignKey(Faculte, on_delete=models.CASCADE, related_name='faculte')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Departement, self).save(*args, **kwargs)


class Promotion(models.Model):
    fac = models.ForeignKey(Faculte, on_delete=models.CASCADE, related_name='fac')
    dep = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='departement', default='Empty')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Promotion, self).save(*args, **kwargs)
