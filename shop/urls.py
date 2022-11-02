from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:c_slug>/', views.index, name='prod_cat'),
    path('<slug:c_slug>/<slug:p_slug>/', views.product_details, name='details'),
]
