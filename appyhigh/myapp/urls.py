from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('foods', views.FoodViewSet)

app_name = "movies"
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('detail/<int:food_id>', views.detail, name='detail'),
    path('add_food/', views.add_food, name='add_food'),
    path('save_food', views.save_food, name='save_food'),
    path('delete/<int:food_id>', views.delete_food, name='delete_food'),
    path('edit/<int:food_id>', views.edit_food, name='edit_food'),
    path('update/<int:food_id>', views.update_food, name='update_food'),
]
