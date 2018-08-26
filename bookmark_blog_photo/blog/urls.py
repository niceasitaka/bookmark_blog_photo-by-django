from django.urls import path, include

from blog.views import *

app_name = 'blog'
urlpatterns = [
	path('', PostLV.as_view(), name='index'), # /blog/
	path('post/', PostLV.as_view(), name='post_list'), # /blog/post/
	path('post/<slug:slug>/', PostDV.as_view(), name='post_detail'), #/blog/post/django-example/
	path('archive/', PostAV.as_view(), name='post_archive'), # /blog/archive/
	path('<int:year>/', PostYAV.as_view(), name='post_year_archive'), # /blog/2012/
	path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'), # /blog/2012/nov/
	path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'), # /blog/2012/nov/10/
	path('today/', PostTAV.as_view(), name='post_today_archive'), # /blog/today/
	# name은 템플릿의 href 등의 변수에 사용됨
	path('tag/', TagTV.as_view(), name='tag_cloud'), # /blog/tag/
	path('tag/<str:tag>/', PostTOL.as_view(), name='tagged_object_list'), # /blog/tag/tagname/
	path('search/', SearchFormView.as_view(), name='search'),
	
	path('add/', PostCreateView.as_view(), name='add'), # /blog/add/
	path('change/', PostChangeLV.as_view(), name='change'), # /blog/change/
	path('<int:pk>/update/', PostUpdateView.as_view(), name='update'), # /blog/99/update/
	path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'), # /blog/99/delete/
]