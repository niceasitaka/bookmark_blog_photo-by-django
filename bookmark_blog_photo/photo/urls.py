from django.urls import path
from photo.views import *




app_name = 'photo'
urlpatterns = [
	path('', AlbumLV.as_view(), name='index'), # /photo/
	path('album/', AlbumLV.as_view(), name='album_list'), # /photo/album/
	path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'), # /photo/album/1/
	path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'), # /photo/photo/1/
	
	path('album/add/', AlbumPhotoCV.as_view(), name='album_add'), # /photo/album/add/
	path('album/change/', AlbumChangeLV.as_view(), name='album_change'), # /photo/album/change/
	path('album/<int:pk>/update/', AlbumPhotoUV.as_view(), name='album_update'), # /photo/album/1/update/
	path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'), # /photo/album/1/delete/
	path('photo/add/', PhotoCreateView.as_view(), name='photo_add'), # /photo/add/
	path('photo/change/', PhotoChangeLV.as_view(), name='photo_change'), # /photo/change/
	path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'), # /photo/photo/1/update/
	path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'), # /photo/photo/1/delete/
]