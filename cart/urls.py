from . import views
from django.urls import path

urlpatterns = [
                  path('cartdetails', views.cart_details, name='cartdetails'),
                  path('add/<int:product_id>/',views.add_cart,name='addcart'),
                  path('min/<int:product_id>/', views.min_cart, name='minus'),
                  path('del/<int:product_id>/', views.delete_cart, name='delete'),
                  path('delivery_details', views.delivery_details, name='delivery_details'),
                  path('payment', views.payment, name='payment'),
                  path('order_successful', views.order_successful, name='order_successful'),
              ]
