from api.models import Tags_info
from rest_framework import serializers
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags_info
        fields = ['task_id', 'info']