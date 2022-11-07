from . import views
from django.urls import path

urlpatterns = [
                  path('cartdetails', views.cart_details, name='cartdetails'),
                  path('add/<int:product_id>/',views.add_cart,name='addcart')
              ]
