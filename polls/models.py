import datetime

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.question_text)
            slug = base_slug
            counter = 2

            while Question.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text