from datetime import datetime, timedelta
import io
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .models import *
from rest_framework import viewsets, permissions, generics
from .serializers import *
from authentication.models import User
from django.db.models import Q
from rest_framework import permissions
from django.utils import timezone
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
import django_filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser


# Pagination for REST FRAMEWORK TAKEN
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.


class FoodAPI(generics.GenericAPIView,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin
              ):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = FoodDetailsSerializer
    queryset = FoodDetails.objects.all()
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    # filter_class =
    ordering_fields = [
        'food_name',
    ]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class PostedFoodAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, *args, **kwargs):
        if not request.user.groups.all():
            return Response(None)

        if request.GET.get('type') == "requested_food":

            fooddetails = FoodDetails.objects.filter(
                status="requested", requested_by=request.user)

            foodDetails_serializer = FoodDetailsSerializer(
                fooddetails, many=True)
            return Response(foodDetails_serializer.data)

        if (request.user.groups.all()[0].id == 1):
            fooddetails = FoodDetails.objects.filter(
                posted_by=request.user)
        else:
            date_from = datetime.now() - timedelta(days=1)
            # print(date_from, 'date_fromdate_from')
            fooddetails = FoodDetails.objects.filter(
                status="available", posted_date__gte=date_from)

        foodDetails_serializer = FoodDetailsSerializer(
            fooddetails, many=True)
        return Response(foodDetails_serializer.data)
