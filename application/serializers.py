from rest_framework import serializers as s
from typing import Tuple

from application import models as m


class NewSerializer(s.ModelSerializer):
    category = s.SlugRelatedField(slug_field="name", read_only=True)
    author = s.SlugRelatedField(slug_field="username", read_only=True)
    tags = s.SlugRelatedField(slug_field="tag", read_only=True, many=True)

    class Meta:
        fields = "__all__"
        model = m.New

    def save(self, **data):
        author = data["author"] if data["author"].is_authenticated else None
        m.Tag.objects.bulk_update_or_create((m.Tag(tag=tag) for tag in data["tags"]), ("tag",), "tag")
        category = m.Category.objects.get_or_create(name=data["category"])[0] if data["category"] else None
        return super().save(author=author, tags=m.Tag.objects.filter(tag__in=data["tags"]), category=category)


class TagSerializer(s.ModelSerializer):
    news = NewSerializer(instance=m.New.objects.all(), many=True)

    class Meta:
        fields = "__all__"
        model = m.Tag


class CategorySerializer(s.ModelSerializer):
    news = NewSerializer(instance=m.New.objects.all(), many=True)

    class Meta:
        fields = "__all__"
        model = m.Category
