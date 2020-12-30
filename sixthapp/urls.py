from django.urls import path
from sixthapp.views import home, add_product, \
    edit_product, show_products, register, login_page, logout_fn, \
        edit_user, change_password, add_category, delete_product, \
            del_category

urlpatterns = [
    path('', home, name='home'),
    path('product/', add_product, name='add_product'),
    path('product/edit/<int:id>/', edit_product, name='edit_product'),
    path('product/delete/<int:id>/', delete_product, name='delete_product'),
    path('category/<int:id>/', show_products),
    path('register/', register, name='register'),
    path('login/', login_page),
    path('logout/', logout_fn),
    path('edit/user/', edit_user, name='edit_user'),
    path('password/', change_password, name='change_password'),
    path('add_category/', add_category, name='add_category'),
    path('category/delete/<int:id>', del_category, name='del_category'),


]