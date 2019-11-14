from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView

from users.forms import UpdateUserProfileForm
from .models import UserProfile

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    model = UserProfile
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        user_detail = self.model.objects.filter(user = request.user)
        context = {'user_profile' : user_detail}
        return render(request, self.template_name, context = context)

@method_decorator(login_required, name='dispatch')
class UpdateUserProfileView(UpdateView):
    model = UserProfile
    form_class = UpdateUserProfileForm
    template_name_suffix = '_update'

    def get_object(self):
        obj = self.model.objects.get(pk = self.request.user.pk)
        return obj

    def get_success_url(self):
        return reverse('user-profile')
