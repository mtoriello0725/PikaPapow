from rest_framework import serializers
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ("name", "created_date", "img_url", "description", "upvote_peak")