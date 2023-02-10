from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages



def Create(request):
	form = RatingForm()
	temp = NewCourse.objects.all()
	context = {'form':form, 'data':temp}
	if request.method =='POST':
		form = RatingForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f"Course Added")
	return render(request, 'app1/create.html',context)



def add_review(request,id):

	course = get_object_or_404(NewCourse,id=id)
	form = ReviewForm()
	context = {'form':form}
	try:
		if request.method == "POST":
			form = ReviewForm(request.POST)
			if form.is_valid():
				data = form.save(commit=False)
				data.comment = request.POST["comment"]
				data.rating = request.POST["rating"]
				data.course = course
				data.user = request.user
				data.save()
				messages.success(request,f"Comment Added")
		
	except Exception as e:
		messages.warning(request,f"e")

	return render(request,'app1/rate.html', context)
		

	