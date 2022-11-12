from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:c_slug>/', views.index, name='prod_cat'),
    path('<slug:c_slug>/<slug:p_slug>/', views.product_details, name='details'),
    path('search',views.search,name='search'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('help',views.help,name='help'),
    path('faqs',views.faqs,name='faqs'),
    path('terms',views.terms,name='terms'),
    path('privacy',views.privacy,name='privacy'),
    path('profile',views.profile,name='profile'),
]
