from django.urls import path, include

from bookmark.views import *

app_name = 'bookmark'
urlpatterns = [
	path('', BookmarkLV.as_view(), name='index'),
	path('<int:pk>/', BookmarkDV.as_view(), name='detail'), # name은 템플릿의 href 등의 변수에 사용됨
	
	path('add/', BookmarkCreateView.as_view(), name='add'), # /bookmark/add/
	path('change/', BookmarkChangeLV.as_view(), name='change'), # /bookmark/change/
	path('<int:pk>/update/', BookmarkUpdateView.as_view(), name='update'), # /bookmark/99/update/
	path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete'), # /bookmark/99/delete/
]