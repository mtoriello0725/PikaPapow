from rest_framework import generics
from .models import Meme
from .serializers import MemeSerializer


class GetMemes(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer