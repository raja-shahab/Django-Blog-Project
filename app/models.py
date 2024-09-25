from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('0', 'DRAFT'),
        ('1', 'PUBLISH')
    )
    SECTION = (
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editors Pick','Editors Pick'),
        ('Trending','Trending'),
        ('Inspiration','Inspiration'),
        ('Latest Post','Latest Post'),
    )

    featured_image = models.ImageField(upload_to='Images')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = RichTextField()
    slug = models.SlugField(max_length=300, null=True, blank=True, unique=True)
    status = models.CharField(choices=STATUS, max_length=100)
    section = models.CharField(choices=SECTION, max_length=200)
    main_post = models.BooleanField(default=False)

    def __str__(self):
        return self.title


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()

    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)

    return slug


@receiver(pre_save, sender=Post)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


