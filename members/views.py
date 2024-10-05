from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MembersForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_list_or_404


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request,slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render(request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def create_member_profile(request):
  if request.method == 'POST':
    form = MembersForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("success")
  else:
    form = MembersForm()
  return render(request,'create_member_profile.html',{'form':form})

def success_view(request):
  return render(request,'success.html')

# def delete_member_profile(request, member_id):
#   member = get_list_or_404(Member, id = member_id)

#   if request.method == 'POST':
#     member.delete()
#     return redirect('success')
  
#   return render(request,'confirm_delete.html',{'member':member})
