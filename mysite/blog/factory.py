

import factory
from django.utils import timezone

from django.utils.text import slugify
from faker import Faker
from .models import Post, User

fake = Faker()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = User.objects.all().first()
    title = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=30))
    body = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=250))
    status = Post.Status.PUBLISHED

    @factory.post_generation
    def slug(self, create, extracted, **kwargs):
        if not create:
            return
        self.slug = slugify(self.title)

    @factory.lazy_attribute
    def publish(self):
        return timezone.now()
