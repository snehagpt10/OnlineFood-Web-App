from django.urls import path, include
from . import views
from accounts import views as AccountViews


urlpatterns = [
    path('', AccountViews.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/',views.fooditems_by_category,name='fooditems_by_category'),
    # category crud
    path('menu-builder/category/add_category/',views.add_category,name='add_category'),
    path('menu-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/', views.delete_category,name='delete_category'),

    # FoodItem crud
    path('menu-builder/food/add/',views.add_food,name='add_food'),
    path('menu-builder/food/edit/<int:pk>/', views.edit_food, name='edit_food'),
    path('menu-builder/food/delete/<int:pk>/', views.delete_food, name='delete_food'),

    # opening hour 
    path('opening-hour/',views.opening_hour,name='opening_hour'),
    path('opening-hour/add/',views.add_opening_hour,name='add_opening_hour'),
    path('opening-hour/remove/<int:pk>/',views.remove_opening_hour,name='remove_opening_hour'),

    path('order_detail/<int:order_number>/', views.order_detail, name='vendor_order_detail'),
    
    ]