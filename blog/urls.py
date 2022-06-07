from django.urls import path
from .views import like, post_delete, post_detail, post_list,post_create, post_update

app_name = "blog" #birden fazla app adı olabilir.Urls.py kafası karışmaması için app_name şeklinde app adı yazılabilir.
urlpatterns = [
    path("", post_list,name="list"),
    path("create/", post_create,name="create"),
    path("<str:slug>/", post_detail,name="detail"),
    path("<str:slug>/update/", post_update,name="update"),
    path("<str:slug>/delete/", post_delete,name="delete"),
    path("<str:slug>/like/",like,name="like"),
]
