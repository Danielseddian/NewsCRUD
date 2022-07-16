from django.urls import include, path
from rest_framework.routers import DefaultRouter

from application import views as v

app_name = "news"

router = DefaultRouter()
router.register("tags", v.TagViewSet, basename="tags")
router.register("category", v.CategoryViewSet, basename="categories")
router.register("news", v.NewsViewSet, basename="news")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
