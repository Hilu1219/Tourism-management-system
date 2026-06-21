from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path('book/<int:package_id>/', views.book_package, name='book_package'),
]