from django.db import models
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView

class User(models.Model):
    name = models.CharField(max_length=200)

class RegisterView(TemplateView):
    template_name = 'register.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url