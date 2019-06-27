from rest_framework import viewsets
from .serializers import UserSerializer, FoodSerializer, RegisterSerializer, LoginSerializer
from .models import User, Food
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .forms import FoodForm, SearchFoodForm, LoginForm, RegisterForm


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
    form = FoodForm()
    return render(request, 'movies/add.html', {'form': form})


def save_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            # form.save()
            a = Food()
            print(form.cleaned_data)
            a.name = form.cleaned_data['name']
            a.carbohydrates_amount = form.cleaned_data['carbohydrates_amount']
            a.fats_amount = form.cleaned_data['fats_amount']
            a.proteins_amount = form.cleaned_data['proteins_amount']
            a.user_id = 1
            a.save()
            data = Food.objects.all()
            return render(request, 'movies/index.html', {'data': data})
    else:
        form = FoodForm()
    return render(request, 'movies/add.html', {'form': form})


def edit_food(request, food_id):
    data = Food.objects.get(id=food_id)
    return render(request, 'movies/edit.html', {'data': data})


def update_food(request, food_id):
    data = Food.objects.get(id=food_id)
    print(request.POST)
    form = FoodForm(request.POST, instance=data)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        data = Food.objects.all()
        return render(request, 'movies/index.html', {'data': data})

    return render(request, 'movies/edit.html', {'data': data})


def delete_food(request, food_id):
    m = get_object_or_404(Food, id=food_id)

    m.delete()
    data = Food.objects.all()
    return render(request, 'movies/index.html', {'data': data})
