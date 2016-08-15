from django.shortcuts import render
from .models import Saying
# Create your views here.
def main(request):
	cur_saying = Saying.objects.all()
	context = {'cur_saying': cur_saying}
	return render(request, 'main.html', context)