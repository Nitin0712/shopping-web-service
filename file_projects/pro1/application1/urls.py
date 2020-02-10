from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index),
    path('', views.view_product, name='home'),
    path('edit/<int:id>', views.edit_product, name='edit_pro'),
    path('update/<int:id>', views.update_product, name='update_pro'),
    path('addtocart', views.add_to_cart, name='addtocart'),
    path('register', views.regview, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('search', views.get_search_data, name='search'),
    path('view_cart/<int:id>', views.view_cart),
]