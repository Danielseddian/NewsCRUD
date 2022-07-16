from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.db import models as m
from localization import ru as lang
from django.contrib.auth import get_user_model


User = get_user_model()


class Tag(m.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    tag = m.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = lang.TAG_VERBOSE_NAME[0]
        verbose_name_plural = lang.TAG_VERBOSE_NAME[1]
        ordering = ("tag", "pk")

    def __str__(self):
        return self.tag


class Category(m.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    name = m.SlugField(unique=True)

    class Meta:
        verbose_name = lang.CATEGORY_VERBOSE_NAME[0]
        verbose_name_plural = lang.CATEGORY_VERBOSE_NAME[1]
        ordering = ("name", "pk")

    def __str__(self):
        return self.name


class New(m.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()

    tags = m.ManyToManyField(Tag, related_name="news")
    head = m.CharField(max_length=150, help_text=lang.NEW_HEAD_HELP_TEXT, unique=True)
    text = m.TextField(max_length=10_000, help_text=lang.NEW_POST_HELP_TEXT, unique=True)
    author = m.ForeignKey(User, related_name="news", on_delete=m.CASCADE, blank=True, null=True)
    posted = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    category = m.ForeignKey(Category, related_name="news", on_delete=m.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = lang.NEW_VERBOSE_NAME[0]
        verbose_name_plural = lang.NEW_VERBOSE_NAME[1]
        ordering = ("pk", "head")

    def __str__(self):
        return f"{self.category.name + ': ' if self.category else ''}{self.head} ({self.posted})"
