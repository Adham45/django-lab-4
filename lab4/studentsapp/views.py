from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from studentsapp.forms import InsertStudent, AddTrack
from studentsapp.models import MyUser, Student, Track


def home_page(request):
    usr = MyUser.objects.filter(usr_is_logged=True)
    if len(usr) != 0 and request.session.has_key('usr_name'):
        authenticate_usr = MyUser.objects.filter(usr_name=request.session['usr_name'])
        context = {'process': '', 'message': '', 'list': Student.objects.all(),
                   'usr_name': authenticate_usr[0].usr_name,
                   'insertstudent': InsertStudent()}
        if request.method == 'GET':
            if request.GET == {}:
                context['process'] = 'insert'
            else:
                context['process'] = request.GET['process']
        else:
            context['process'] = request.POST['process']
            process = request.POST['process']
            if process == 'insert':
                context['message'] = f"{process}"
                insertstudent = InsertStudent(request.POST)
                insertstudent.save()
            elif process == 'select':
                query = request.POST['query']
                context['message'] = f"{process}"
                context['list'] = Student.objects.filter(std_fname=query)
                print(f"Search {query}")
            else:
                print("Not Valid")
        return render(request, 'studentsapp/home.html', context)
    else:
        return redirect(login_page)


def register_page(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'studentsapp/register.html')
    else:
        if request.POST['usr_password'] == request.POST['cpassword']:
            MyUser.objects.create(usr_name=request.POST['usr_name'], usr_email=request.POST['usr_email'],
                                   usr_password=request.POST['usr_password'])
            User.objects.create_user(username=request.POST['usr_name'], email=request.POST['usr_email'],
                                     password=request.POST['usr_password'], is_staff=True)
        else:
            context['error'] = 'Confirm password and password don not match'
        return render(request, 'studentsapp/register.html', context)


def login_page(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'studentsapp/login.html')
    else:
        user = MyUser.objects.filter(usr_email=request.POST['usr_email'])
        authenticate_user = authenticate(username=user[0].usr_name, password=user[0].usr_password)
        if user:
            if user[0].usr_password == request.POST['usr_password'] and authenticate_user is not None:
                user.update(usr_is_logged=True)
                request.session['usr_name'] = user[0].usr_name
                login(request, authenticate_user)
                return redirect(home_page)
            else:
                context['error'] = "Incorrect Password"
                return render(request, 'studentsapp/login.html', context)
        else:
            context['error'] = "User Not Found"
            return redirect(request, 'studentsapp/login.html', context)


class UpdateStudent(View):
    def get(self, request, idu):
        context = {'rowid': idu, 'process': 'update', 'list': Student.objects.all(),
                   'usr_name': MyUser.objects.get(usr_is_logged=True).usr_name,
                   'updatestudent': InsertStudent(instance=Student.objects.get(std_id=idu))}
        return render(request, 'studentsapp/home.html', context)

    def post(self, request, idu):
        InsertStudent(request.POST, instance=Student.objects.get(std_id=idu)).save()
        return redirect(home_page)


def is_logged():
    usr = MyUser.objects.filter(usr_is_logged=True)
    if len(usr) != 0:
        return True
    else:
        return False


def welcome_page(request):
    request.session.clear()
    logout(request)
    MyUser.objects.update(usr_is_logged=False)
    return render(request, 'studentsapp/welcome.html')


def delete_student(request, idd):
    Student.objects.filter(std_id=idd).delete()
    return home_page(request)


def delete_track(request, tr_id):
    Track.objects.filter(track_id=tr_id).delete()
    return redirect('Trackshomepage')


class UpdateTrack(View):
    def get(self, request, tid):
        context = {'rowid': tid, 'trackmode': 'update', 'tracklist': Track.objects.all(),
                   'username': MyUser.objects.get(usr_is_logged=True).usr_name,
                   'updatetrack': AddTrack(instance=Track.objects.get(track_id=tid))}
        return render(request, 'studentsapp/track_form.html', context)

    def post(self, request, tid):
        AddTrack(request.POST, instance=Track.objects.get(track_id=tid)).save()
        return redirect('Trackshomepage')


class Tracksinsertview(CreateView):
    model = Track
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        if not is_logged():
            return redirect(login_page)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addtrack'] = AddTrack()
        context['tracklist'] = Track.objects.all()
        context['usr_name'] = MyUser.objects.get(usr_is_logged=True).usr_name
        return context

    success_url = reverse_lazy('Trackshomepage')
