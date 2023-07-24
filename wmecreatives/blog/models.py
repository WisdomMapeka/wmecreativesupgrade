from distutils.command.upload import upload
from statistics import mode
from django.db import models
from tinymce.models import HTMLField 

draft_publish = (
    ('publish','publish'),
    ('draft','draft'),
)

class AnalyticsCode(models.Model):
    name = models.CharField(default="google code", max_length=200, null=True, blank=True)
    code_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300, unique=True)
    is_series = models.BooleanField(default=False)
    summary = models.TextField(null=True, blank=True, help_text="31 letters max will give a better out look")
    lead_img = models.ImageField(upload_to='media_files/blog', null=True, blank=True)
    lead_img_alt = models.CharField(max_length=1000, null=True, blank=True, help_text="alt text of an image")
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    author = models.CharField(max_length=200, default="wmecreatives", null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)
    icon = models.ImageField(upload_to="media_files/Categories/icon", null=True, blank=True)
    icon_class = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "No Category"


class Articles(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    article_status = models.CharField(max_length=100, null=True, blank=True, choices=draft_publish)
    slug = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    category = models.ManyToManyField(Categories, blank=True)
    lead_img = models.ImageField(upload_to='media_files/blog', null=True, blank=True)
    lead_img_alt = models.CharField(max_length=1000, null=True, blank=True, help_text="alt text of an image")
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)
    content = HTMLField()
    summary = models.TextField(null=True, blank=True, help_text="31 letters max will give a better out look")
    author = models.CharField(max_length=200, default="wmecreatives", null=True, blank=True)
    author_image = models.ImageField(upload_to='media_files/authorImg', null=True, blank=True)
    author_image_atlt_text = models.CharField(max_length=1000, null=True, blank=True, help_text="alt text of an image")
    youtube_video_link = models.TextField(null=True, blank=True)
    num_views = models.IntegerField(null=True, blank=True)
    read_time = models.CharField(max_length=30, null=True, blank=True)
    # styleshit = models.CharField(max_length=100, null=True, blank=True, choices=choices, default="shades-of-purple.min.css")
    


    def __str__(self):
        return self.title

class Images(models.Model):
    name = models.CharField(default='article image', null=True, blank=True, max_length=300, unique=True)
    image = models.ImageField(upload_to="uploads", null=True, blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    name  = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    dislikes = models.IntegerField(default=0, null=True, blank=True)
    blog = models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name and self.email and self.phone:
            return "Name: {}   email: {}   phone: {}".format(self.name, self.email, self.phone)
        elif self.name and self.email:
            return "Name: {}   email: {}".format(self.name, self.email)
        elif self.name:
            return self.name
        else:
            return "NO NAME"

#THis model was created for an article about creating an image ap
class Photos_collections(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default="api image")
    uploded = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    photographer = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to = "api_photos", null=True, blank=True)

    def __str__(self):
        return self.name

    
