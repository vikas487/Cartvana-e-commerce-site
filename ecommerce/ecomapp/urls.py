from django.urls import path
from ecomapp import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about', views.about, name="AboutUs"),
    path('contactus',views.contactus,name='contactus'),
    path('tracker', views.tracker, name="TrackingStatus"),
    path('products/<int:myid>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),




]