from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")
        # fields = ("name", "kind") -> name 과 kind 를 보여줌
        # exclude = ("created_at") -> created_at 을 제외하고 보여줌