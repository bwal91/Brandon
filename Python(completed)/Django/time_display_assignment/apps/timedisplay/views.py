from django.shortcuts import render
import datetime
def index(request):
	context = {
	"Date": datetime.datetime.now()
	}
	return render(request, 'timedisplay/index.html', context)
