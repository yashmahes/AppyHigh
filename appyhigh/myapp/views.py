from rest_framework import viewsets
from .serializers import UserSerializer, FoodSerializer, RegisterSerializer, LoginSerializer
from .models import User, Food
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .forms import FoodForm, SearchFoodForm, LoginForm, RegisterForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def login(request):
    form = LoginForm()
    return render(request, 'movies/login.html', {'form': form})


def register(request):
    form = RegisterForm()
    return render(request, 'movies/register.html', {'form': form})


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
    if request.session.get('loggedin_user_id'):
        data = Food.objects.all()
        user_id = request.session.get('loggedin_user_id')
        user = User.objects.get(id=user_id)
        return render(request, 'movies/index.html', {'data': data, 'user': user})
    else:
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})


def detail(request, food_id):
    if request.session.get('loggedin_user_id'):
        data = get_object_or_404(Food, id=food_id)
        return render(request, 'movies/detail.html', {'data': data})
    else:
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})


def add_food(request):
    if request.session.get('loggedin_user_id'):
        form = FoodForm()
        return render(request, 'movies/add.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})


def save_food(request):
    if request.session.get('loggedin_user_id'):
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
                a.user_id = request.session.get('loggedin_user_id')
                a.save()
                data = Food.objects.all()
                user_id = request.session.get('loggedin_user_id')
                user = User.objects.get(id=user_id)
                return render(request, 'movies/index.html', {'data': data, 'user': user})
        else:
            form = FoodForm()
        return render(request, 'movies/add.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})


def edit_food(request, food_id):
    if request.session.get('loggedin_user_id'):
        data = Food.objects.get(id=food_id)
        return render(request, 'movies/edit.html', {'data': data})
    else:
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})


def update_food(request, food_id):
    a = Food.objects.get(id=food_id)
    print(request.POST)
    form = FoodForm(request.POST)
    data = Food.objects.all()
    if form.is_valid():
        print(form.cleaned_data)
        a.name = form.cleaned_data['name']
        a.carbohydrates_amount = form.cleaned_data['carbohydrates_amount']
        a.fats_amount = form.cleaned_data['fats_amount']
        a.proteins_amount = form.cleaned_data['proteins_amount']
        a.user_id = request.session.get('loggedin_user_id')
        a.save()
        data = Food.objects.all()
        user_id = request.session.get('loggedin_user_id')
        user = User.objects.get(id=user_id)
        return render(request, 'movies/index.html', {'data': data, 'user': user})

    return render(request, 'movies/edit.html', {'data': data})


def delete_food(request, food_id):
    if request.session.get('loggedin_user_id'):
        m = get_object_or_404(Food, id=food_id)

        m.delete()
        data = Food.objects.all()
        user_id = request.session.get('loggedin_user_id')
        user = User.objects.get(id=user_id)
        return render(request, 'movies/index.html', {'data': data, 'user': user})
    else:
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})


def logout(request):
    request.session['loggedin_user_id'] = None
    form = LoginForm()
    return render(request, 'movies/login.html', {'form': form})


def search_food(request):
    food_name = request.GET.get("fname")
    data = get_object_or_404(Food, name=food_name)
    return render(request, 'movies/detail.html', {'data': data})


@api_view(['GET'])
def search_food_api(request):
    food_name = request.GET.get("fname")
    food_data = get_object_or_404(Food, name=food_name)
    serializer = FoodSerializer(data=food_data)
    response_object = {}
    response_object['name'] = food_data.name
    response_object['carbohydrates_amount'] = food_data.carbohydrates_amount
    response_object['fats_amount'] = food_data.fats_amount
    response_object['proteins_amount'] = food_data.proteins_amount
    return Response({'data': response_object}, status=status.HTTP_200_OK)


def validate_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = User.objects.filter(username=username, password=password)
        if user:
            request.session['loggedin_user_id'] = user[0].id
            data = Food.objects.all()
            user_id = request.session.get('loggedin_user_id')
            user = User.objects.get(id=user_id)
            return render(request, 'movies/index.html', {'data': data, 'user': user})
        else:
            return render(request, 'movies/login.html', {'form': form})
    return render(request, 'movies/login.html', {'form': form})


def register(request):
    form = RegisterForm()
    return render(request, 'movies/register.html', {'form': form})


def save_user(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        user = User()
        user.fullname = form.cleaned_data['fullname']
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.username = user.email
        user.save()
        form = LoginForm()
        return render(request, 'movies/login.html', {'form': form})
    form = RegisterForm()
    return render(request, 'movies/register.html', {'form': form})
