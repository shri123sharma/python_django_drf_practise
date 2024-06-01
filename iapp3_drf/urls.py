from django.urls import path, include
from .views import *
from django.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewset, basename='article'),
router.register(r'album', AlbumViewset, basename='album'),

urlpatterns = [
    path('', include(router.urls)),
    path("my-view-api/", MyApiView.as_view(), name="my_view"),
    path("my-query-api/", MyQueryApi.as_view(), name="my_query"),
    path("my-parser-api/", MyParserApiView.as_view(), name="my_parser"),
    path("user-profile-api/", UserProfileView.as_view(), name="user_profile"),
    path("book-api/", BookApiView.as_view(), name="book"),
    path("book-api/<int:id>/", BookApiView.as_view(), name="book_update"),
    path("my-render-api/", MyRenderView.as_view(), name="render_name"),
    path("film-api/", FilmListCreateView.as_view(), name="film_api"),
    path("film-api/<int:pk>/", FilmDetailView.as_view(), name="film_detail_api"),
    # path("company-detail-api/<int:pk>/",CompanyDetailView.as_view(),name="company_detail_api"),
    path("company-create-api/", CompanyCreateView.as_view(),
         name="company_create_api"),
    path("company-list-api/", CompanyListView.as_view(), name="company_list_api"),
    path('my-view/', my_view, name='my_view')



]
