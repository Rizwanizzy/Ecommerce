from . import views
from django.urls import path

urlpatterns = [
                  path('cartdetails', views.cart_details, name='cartdetails'),
                  path('add/<int:product_id>/',views.add_cart,name='addcart'),
                  path('min/<int:product_id>/', views.min_cart, name='minus'),
                  path('del/<int:product_id>/', views.delete_cart, name='delete'),
                  path('place_order', views.delivery_details, name='place_order'),
                  path('payment', views.payment, name='payment'),
              ]
