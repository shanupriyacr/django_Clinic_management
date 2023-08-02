
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Department
from .forms import AppointmentForm, TimeSlotForm

# Home view
@login_required
def home_view(request):
    return render(request, 'home.html')


# Admin dashboard view
def is_superuser(user):
    return user.is_superuser


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# User registration view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


# Book appointment view
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})


# Manage time slots view
@login_required
def manage_time_slots(request):
    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_slot_list')
    else:
        form = TimeSlotForm()
    return render(request, 'manage_time_slots.html', {'form': form})


# Add doctor view
@login_required
def add_doctor(request):
    if request.method == 'POST':


    return render(request, 'add_doctor.html')


# Edit doctor view
@login_required
def edit_doctor(request, doctor_id):


    return render(request, 'edit_doctor.html')


# View for department list
@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


# View for creating department
@login_required
def create_department(request):
    if request.method=='POST':
        return redirect('department_list')
    return render(request, 'create_department.html')


# View for editing department
@login_required
def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        return redirect('department_list')
    return render(request, 'edit_department.html', {'department': department})


# View for deleting department
@login_required
def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == 'POST':
        return redirect('department_list')
    return render(request, 'delete_department.html', {'department': department})



