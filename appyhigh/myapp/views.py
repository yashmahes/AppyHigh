from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, FoodSerializer, RegisterSerializer, LoginSerializer
from .models import User, Food
from django.shortcuts import render, get_list_or_404, get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def index(request):
    # movies = Movie.objects.all()
    # movies = Movie.objects.filter(release_year=1984)
    # movies = Movie.objects.get(id=1)

    data = Food.objects.all()

    return render(request, 'movies/index.html', {'data': data})


def detail(request, food_id):
    data = get_object_or_404(Food, id=food_id)
    return render(request, 'movies/detail.html', {'data': data})


def add_food(request):
    return render(request, 'home.html')


def save_food(request):
    return render(request, 'home.html')


def edit_food(request, food_id):
    return render(request, 'home.html')


def update_food(request, food_id):
    return render(request, 'home.html')


def delete_food(request, food_id):
    return render(request, 'home.html')
