from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from .models import UserProfile

# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserProfile(View):
    model = UserProfile
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        user_detail = self.model.objects.filter(user = request.user)
        context = {'user_profile' : user_detail}
        return render(request, self.template_name, context = context)
