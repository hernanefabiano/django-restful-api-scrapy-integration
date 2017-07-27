from rest_framework_mongoengine import serializers
from .models import News


class FeedSerializer(serializers.DocumentSerializer):
    class Meta:
        model = News
        fields = '__all__'
