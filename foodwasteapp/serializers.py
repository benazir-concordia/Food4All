from asyncore import read
from urllib import request
from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import *
from rest_framework.response import Response
from rest_framework import status


class FoodDetailsSerializer(serializers.ModelSerializer):

    posted_by_obj = UserSerializer(source='posted_by', read_only=True)
    requested_by_obj = UserSerializer(source='requested_by', read_only=True)

    class Meta:
        model = FoodDetails
        fields = "__all__"
