from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseServerError, JsonResponse, QueryDict
from django.template import loader
from .models import Stage, Posting
from django.contrib.auth.decorators import login_required
from jobboard.forms import UserRegisterForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import json
import logging


@login_required
def index(request):
    if request.method == "POST":
        try:
          
          logger = logging.getLogger("mylogger")
          # Parse the JSON payload
          body_unicode = request.body.decode('utf-8')
          q = QueryDict(body_unicode)

          stage1 = Stage.objects.get(stage_title = 'Applied')
          q1 = q.__getitem__('jsonString1')
          str_q1 = q1.replace('id=', '')
          str_q1 = str_q1.replace('"', '')
          arr1 = str_q1.split('&')
          for curr in arr1:
            posting = Posting.objects.get(id=curr)
            if posting not in Posting.objects.filter(stage = stage1):
              posting.stage = stage1
              posting.save()
              logger.info(posting.stage)

          stage2 = Stage.objects.get(stage_title = 'Assessment')
          q2 = q.__getitem__('jsonString2')
          str_q2 = q2.replace('id=', '')
          str_q2 = str_q2.replace('"', '')
          arr2 = str_q2.split('&')
          for curr in arr2:
            posting = Posting.objects.get(id=curr)
            if posting not in Posting.objects.filter(stage = stage2):
              posting.stage = stage2
              posting.save()
              logger.info(posting.stage)

          stage3 = Stage.objects.get(stage_title = 'Interview')
          q3 = q.__getitem__('jsonString3')
          str_q3 = q3.replace('id=', '')
          str_q3 = str_q3.replace('"', '')
          arr3 = str_q3.split('&')
          for curr in arr3:
            posting = Posting.objects.get(id=curr)
            if posting not in Posting.objects.filter(stage = stage3):
              posting.stage = stage3
              posting.save()
              logger.info(posting.stage)

          
  
            # Loop over our list order. The id equals the question id. Update the order and save'
         # for posting in enumerate(data1):
         #   pq = Stage.objects.get(posting=posting['string'])
         #   pq.stage_title = "Hi"



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