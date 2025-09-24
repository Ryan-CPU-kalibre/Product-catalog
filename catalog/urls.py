from django.urls import path
from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.home, name='home'),
    path("category/<int:category_id>/", views.category_detail, name="category_detail"),
]