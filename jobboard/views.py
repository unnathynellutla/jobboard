from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponseServerError, JsonResponse
from django.template import loader
from .models import Stage, Posting
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditPostForm, UserRegisterForm, EditStageForm
import logging


@login_required
def index(request):
    if request.method == "POST":
        try:
          logger = logging.getLogger("mylogger")
          body_unicode = request.body.decode('utf-8')
          body_unicode = body_unicode.replace('id=', '')
          body_unicode = body_unicode.replace('"', '')
          body_unicode = body_unicode.replace('[', '')
          body_unicode = body_unicode.replace(']', '')
          arr = body_unicode.split(',')
          idx = 0
          for curr_stage in Stage.objects.filter(author = request.user):
            q1 = arr[idx]
            arr1 = q1.split('&')
            idx += 1
            if len(arr1) == 1 and arr1[0] == '':
               continue
            for curr in arr1:
              posting = Posting.objects.get(id=curr)
              if posting not in Posting.objects.filter(stage = curr_stage):
                posting.stage = curr_stage
                posting.save()

        except KeyError:
            HttpResponseServerError("Malformed data!")

        return JsonResponse({"success": True}, status=200)
    else:
      latest_stage_list = Stage.objects.filter(author = request.user)
      context = {
          'latest_stage_list': latest_stage_list,
      }
      return render(request, 'jobboard/index.html', context)

@login_required
def detail_view(request, posting_id):
    posting = get_object_or_404(Posting, pk=posting_id)
    return render(request, 'jobboard/detail_view.html', {'posting': posting})

@login_required
def edit_post(request, posting_id):
  context = {}
  posting = get_object_or_404(Posting, pk=posting_id)
  form = EditPostForm(request.POST or None, request = request)
  form.fields["job_title"].text = posting.job_title
  if form.is_valid():
    cd = form.cleaned_data
    pc = Posting(
        stage = cd['stage'].first(),
        job_title = cd['job_title'],
        deadline = cd['deadline'],
        job_description = cd['job_description'],
        job_url = cd['job_url'],
        job_email = cd['job_email']
    ) 
    pc.save()
    return HttpResponseRedirect("detail_view")
  context["form"] = form
  return render(request, 'jobboard/edit_post.html', context)

@login_required
def create_post(request):
  context = {}
  form = EditPostForm(request.POST or None, request = request)
  if form.is_valid():
    cd = form.cleaned_data
    pc = Posting(
        stage = cd['stage'].first(),
        job_title = cd['job_title'],
        deadline = cd['deadline'],
        job_description = cd['job_description'],
        job_url = cd['job_url'],
        job_email = cd['job_email']
    ) 
    pc.save()
  context["form"] = form
  return render(request, 'jobboard/create_post.html', context)

@login_required
def create_stage(request):
  context = {}
  form = EditStageForm(request.POST or None)
  if form.is_valid():
    form.save()
  context["form"] = form
  return render(request, 'jobboard/create_stage.html', context)

@login_required
def edit_stage(request, stage_id):
  context = {}
  stage = get_object_or_404(Stage, pk=stage_id)
  form = EditStageForm(request.POST or None, instance = stage)
  if form.is_valid():
    form.save()
  context["form"] = form
  return render(request, 'jobboard/edit_stage.html', context)

@login_required
def delete_post(request, posting_id):
    context ={}
    posting = get_object_or_404(Posting, pk=posting_id)
 
    if request.method =="POST":
        posting.delete()
        latest_stage_list = Stage.objects.filter(author = request.user)
        context = {
            'latest_stage_list': latest_stage_list,
        }
        return render(request, 'jobboard/index.html', context)
    return render(request, "jobboard/delete_post.html", context)

@login_required
def delete_stage(request, stage_id):
    context ={}
    stage = get_object_or_404(Stage, pk=stage_id)
 
    if request.method =="POST":
        stage.delete()
        latest_stage_list = Stage.objects.filter(author = request.user)
        context = {
            'latest_stage_list': latest_stage_list,
        }
        return render(request, 'jobboard/index.html', context)
    return render(request, "jobboard/delete_stage.html", context)

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