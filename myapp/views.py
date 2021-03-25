from django.http import Http404
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import UserRegForm
from .models import *

# Create your views here.
class MyappIndexView(View):
	def get(self,request):
		return render(request,'dashboard.html')

	#def post(self,request):
	#	if request.method == 'POST'
	#		print('post')
	#		return render(request, 'myapp/')
class RegistrationIndexView(View):
	def get(self,request):
		return render(request,"signup.html")
	def post(self,request):
		form = UserRegForm(request.POST)

		if form.is_valid():

			fname = request.POST.get("firstname")
			mname = request.POST.get("middlename")
			lname = request.POST.get("lastname")
			Sex = request.POST.get("sex")
			Age = request.POST.get("age")
			Email = request.POST.get("emailaddress")
			bdate = request.POST.get("birthdate")
			bplace = request.POST.get("bplace")
			pnumber = request.POST.get("phone")

			form = UserReg(first_name = fname, middle_name = mname, last_name = lname, sex = Sex, age = Age, email_address = Email,
			birth_date = bdate, birth_place = bplace, phone_number = pnumber)

			form.save()

			#return HttpResponse('Welcome User!')
			return render(request,'landing.html')

		else:
			print(form.errors)
			return HttpResponse('not valid')






class LoginIndexView(View):
	def get(self,request):

		return render(request,'login.html')
	def post(self,request):
		return render(request, 'signup.html')



class HomeIndexView(View):
	def get(self,request):
		return render(request, 'landing.html')
	def post(self,request):
		return render(request, 'signup.html')
class AdminLoginIndexView(View):
	def get(self,request):
		return render(request,'adminlogin.html')
