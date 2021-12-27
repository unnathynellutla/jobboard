from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseServerError, JsonResponse
from django.template import loader
from .models import Stage, Posting
from django.contrib.auth.decorators import login_required
from jobboard.forms import UserRegisterForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import json

@login_required
def index(request):
    if request.method == "POST" and request.is_ajax():
        try:
            # Parse the JSON payload
          data = json.loads(request.body)[0]
            # Loop over our list order. The id equals the question id. Update the order and save

        except KeyError:
            HttpResponseServerError("Malformed data!")

        return JsonResponse({"success": True}, status=200)
    else:
      latest_stage_list = Stage.objects.all()
      context = {
          'latest_stage_list': latest_stage_list,
      }
      return render(request, 'jobboard/index.html', context)

@login_required
def edit_post(request, posting_id):
        posting = get_object_or_404(Posting, pk=posting_id)
        return render(request, 'jobboard/edit_post.html', {'posting': posting})

def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid(): 
        form.save()
        username = form.cleaned_data.get('username')
        return index(request)
    else:
      form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})