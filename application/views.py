from rest_framework.viewsets import ModelViewSet
from typing import Dict

from application import serializers as s, models as m, permissions as p


class TagViewSet(ModelViewSet):
    queryset = m.Tag.objects.all()
    serializer_class = s.TagSerializer
    permission_classes = (p.GetCreateOrAuthorize,)


class CategoryViewSet(ModelViewSet):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer
    permission_classes = (p.GetCreateOrAuthorize,)


class NewsViewSet(ModelViewSet):
    queryset = m.New.objects.all()
    serializer_class = s.NewSerializer
    permission_classes = (p.GetCreateOrAuthorize,)

    def get_queryset(self):
        print(self.request.method)
        return super().get_queryset()

    def perform_create(self, serializer):
        data: Dict = self.request.data
        serializer.save(author=self.request.user, category=data.get("category", ""), tags=data.get("tags", ()))

    def perform_update(self, serializer):
        data: Dict = self.request.data
        serializer.save(author=self.request.user, category=data.get("category", ""), tags=data.get("tags", ()))
