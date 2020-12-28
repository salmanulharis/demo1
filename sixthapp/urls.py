from django.urls import path
from sixthapp.views import home, add_product, \
    edit_product, show_products, register, login_page, logout_fn, \
        edit_user, change_password, add_category

urlpatterns = [
    path('', home, name='home'),
    path('product/', add_product, name='add_product'),
    path('product/edit/<int:id>/', edit_product),
    path('category/<int:id>/', show_products),
    path('register/', register, name='register'),
    path('login/', login_page),
    path('logout/', logout_fn),
    path('edit/user/', edit_user),
    path('password/', change_password),
    path('add_category/', add_category, name='add_category'),


]