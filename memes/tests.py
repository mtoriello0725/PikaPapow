from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Meme
from .serializers import MemeSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_meme(name="", created_date="", img_url="", description="", upvote_peak = "'"):
        if name != "":
            Meme.objects.create(
                name=name, 
                created_date=created_date, 
                img_url=img_url,
                description=description,
                upvote_peak=upvote_peak 
            )

    def setUp(self):
        # add test data
        self.create_meme("pika1", "2010-03-10", img_url='https://google.com', description='test1', upvote_peak="100")
        self.create_meme("pika2", "2010-03-10", img_url='https://google.com', description='test2', upvote_peak="1000")
        self.create_meme("pika3", "2010-03-10", img_url='https://google.com', description='test3', upvote_peak="10000")
        self.create_meme("pika4", "2010-03-10", img_url='https://google.com', description='test4', upvote_peak="100000")
        self.create_meme("pika5", "2010-03-10", img_url='https://google.com', description='test5', upvote_peak="1")




class GetAllMemesTest(BaseViewTest):

    def test_get_all_memes(self):
        """
        This test ensures that all memes added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("memes-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Meme.objects.all()
        serialized = MemeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)