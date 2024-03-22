from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User # to access the data entered by the user
from django.contrib import messages # to display warning and error messages
from django.contrib.auth import authenticate, login, logout # authenticate is to verify the password and login is to enable the user to login if all details are correct
from django.contrib.auth.decorators import login_required # this will make sure of the usr has not logged in then receipes page will not be visible


# Create your views here.


@login_required(login_url="/login")
def receipes(request):

  if request.method == "POST":

    data = request.POST
    
    receipe_image = request.FILES.get('receipe_image')
    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')

    '''
    print(receipe_name)
    print(receipe_description)
    print(receipe_image) '''
    
    Receipe.objects.create(
      receipe_name = receipe_name,
      receipe_description = receipe_description,
      receipe_image = receipe_image,
    )

    return redirect('/receipes/')
  
  queryset = Receipe.objects.all()

  if request.GET.get('search'):
    queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))


  context = {'receipes':queryset}
  return render(request,'receipes.html',context)


@login_required(login_url="/login")
def delete_receipe(request,id):
  queryset = Receipe.objects.get(id = id)
  queryset.delete()
  return redirect("/receipes/")


def update_receipe(request,id):
  queryset = Receipe.objects.get(id = id)

  if request.method == "POST":
    data = request.POST
    
    receipe_image = request.FILES.get('receipe_image')
    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')

    queryset.receipe_name = receipe_name
    queryset.receipe_description = receipe_description

    if receipe_image:
      queryset.receipe_image = receipe_image

    queryset.save()
    return redirect('/receipes/')

  context = {'receipe':queryset}
  return render(request, 'update_receipes.html',context)


def login_page(request):

  if request.method == 'POST':
    # first_name = request.POST.get('first_name')
    # last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username=username).exists():
      messages.error(request,'Invaild Username!')
      return redirect('/login')
    

    # WE CANNOT DIRECTLY COMPARE THE PASSWORDS bcz its encrypted
    # if password == user.password

    # to check whether password is correct
    user = authenticate(username=username, password=password)

    if user is None:
      messages.error(request,'Invalid Password!')
      return redirect('/login')
    else:
      login(request,user) # user can successfully login if all details are correctly entered
      return redirect('/receipes')

        

  return render(request, 'login.html')


def logout_page(request):
  logout(request)
  return redirect('/login')


def register_page(request):

  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    # check for duplicate usrname
    user = User.objects.filter(username=username)
    if user.exists():
      messages.error(request, 'This username is already taken!')
      return redirect('/register')

    user = User.objects.create(
      first_name = first_name,
      last_name = last_name,
      username=username, 
      # password=password , this wont be encrypted
      )

    user.set_password(password)
    user.save()

    messages.info(request, 'Account created successfully!')

    return redirect('/register')

  return render(request, 'register.html')