from django.shortcuts import render
from django.views.generic import (View,ListView,
                                  CreateView,DetailView,
                                  UpdateView,TemplateView,DeleteView)

from .models import Desk,Column,Card
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .forms import *
from django.shortcuts import render,redirect

class index(TemplateView):
    template_name = 'index.html'


class DesksList(ListView):
    model = Desk
    context_object_name = 'desk'
    template_name = 'taskmanager/task_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DesksList, self).get_context_data()
        context['card'] = Card.objects.all()
        context['column'] = Column.objects.all()
        return context


class DeskDetail(DetailView):
    model = Desk
    template_name = 'taskmanager/desk_detail.html'
    context_object_name = 'desk_detail'


class CreateDesk(CreateView):
    model = Desk
    fields = ('user','title','type',)


class CreateColumn(CreateView):
    model = Column
    fields = ('title','position',)


class CreateCard(FormMixin,ListView):
    template_name = 'taskmanager/card_form.html'
    form_class = CardCreationForm
    model = Card

    def post(self,request,*args,**kwargs):
        form = CardCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'taskmanager/card_form.html', context={'form':form})

class CardDetail(DetailView):
    model = Card
    template_name = 'taskmanager/card_detail.html'
    context_object_name = 'card_detail'


class CardUpdate(UpdateView):
    fields = ('title','description',)
    model = Card

    def get_form(self, form_class=None):
        form = super(CardUpdate,self).get_form()
        return form

    def get_context_data(self, **kwargs):
        context = super(CardUpdate, self).get_context_data(**kwargs)
        context['update_form'] = self.get_form()
        return context


class CardDelete(DeleteView):
    model = Card
    success_url = reverse_lazy('taskmanager:desk-list')