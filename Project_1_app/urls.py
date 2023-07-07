from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index , name='index'),
    path('blog', views.blog ,name ='blog'),
    path('add-blog/', views.addBlogPage ,name ='add-blog'),
    path('add-blog/add_blog', views.addBlogHandler ,name ='addBlogHandler'),
    path('add-blog/delete_blog', views.delBlogPage ,name ='delete-blog'),
    path('form', views.create_form, name = 'testform'),
    path('models_form', views.ModelsForm, name = 'modelsform'),
    path('delete/<id>', views.deleteblog, name='delete'),
    path('update/<id>', views.updateblog, name='update'),
    path('update_data/<id>', views.updatedata, name='update')
]
