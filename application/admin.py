from django.contrib import admin as a
from application import models as m


@a.register(m.Tag)
class TagAdmin(a.ModelAdmin):
    list_display = ("id", "tag")
    list_editable = ("tag",)
    search_fields = ("id", "tag")
    list_filter = ("id", "tag")


@a.register(m.Category)
class TagAdmin(a.ModelAdmin):
    list_display = ("id", "name")
    list_editable = ("name",)
    search_fields = ("id", "name")
    list_filter = ("id", "name")


@a.register(m.New)
class NewAdmin(a.ModelAdmin):
    editable_fields = ("head", "text", "category")
    many_fields = ("tags",)
    shown_fields = ("id", "author")
    all_fields = shown_fields + many_fields + shown_fields

    list_display = shown_fields + editable_fields
    list_editable = editable_fields
    list_display_links = shown_fields
    search_fields = all_fields
    list_filter = all_fields
