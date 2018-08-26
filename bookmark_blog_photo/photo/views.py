from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from photo.models import Album, Photo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AlbumLV(ListView):
	model = Album
	
class AlbumDV(DetailView):
	model = Album
	
class PhotoDV(DetailView):
	model = Photo
	
#--- Add/Change/Update/Delete for Photo
class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView, self).form_valid(form)


class PhotoChangeLV(LoginRequiredMixin, ListView):
	model = Photo
	template_name = 'photo/photo_change_list.html'

	def get_queryset(self):
		return Photo.objects.filter(owner=self.request.user)


class PhotoUpdateView(LoginRequiredMixin, UpdateView) :
    model = Photo
    fields = ['album', 'title', 'image', 'description']
    success_url = reverse_lazy('photo:index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView) :
    model = Photo
    success_url = reverse_lazy('photo:index')


#--- Add/Change/Update/Delete for Album
#--- Change/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumDeleteView(LoginRequiredMixin, DeleteView) :
    model = Album
    success_url = reverse_lazy('photo:index')
	
#--- InlineFormSet View
#--- Add/Update for Album
from django.shortcuts import redirect
from photo.forms import PhotoInlineFormSet

class AlbumPhotoCV(LoginRequiredMixin, CreateView):
	model = Album
	fields = ['name', 'description']
	template_name = 'photo/album_form.html'
	
	def get_context_data(self, **kwargs):
		context = super(AlbumPhotoCV, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
		else:
			context['formset'] = PhotoInlineFormSet()
		return context
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		context = self.get_context_data()
		formset = context['formset']
		for photoform in formset:
			photoform.instance.owner = self.request.user
		if formset.is_valid():
			self.object = form.save() # 앨범 레코드 생성
			formset.instance = self.object
			formset.save() # 85line에서 생성한 앨범 레코드에서 N:1의 관계인 photo들을 저장
			return redirect(self.object.get_absolute_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))
	
class AlbumPhotoUV(LoginRequiredMixin, UpdateView):
	model = Album
	fields = ['name', 'description']
	template_name = 'photo/album_form.html'

	def get_context_data(self, **kwargs):
		context = super(AlbumPhotoUV, self).get_context_data(**kwargs)
		if self.request.POST:
			context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
		else:
			context['formset'] = PhotoInlineFormSet(instance=self.object)
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']
		if formset.is_valid():
			self.object = form.save()
			formset.instance = self.object
			formset.save()
			return redirect(self.object.get_absolute_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))