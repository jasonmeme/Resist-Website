from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from .models import NewCampaign
from .forms import NewCampaignForm, AttendingForm


# Create your views here.
 
def home(request):
	context = {}
	if request.method == 'POST':
		form = NewCampaignForm(request.POST)
		if form.is_valid():
			form.save()
			form = NewCampaignForm()
			
	else:
		form = NewCampaignForm()
	latest_campaign_list = NewCampaign.objects.order_by('-pub_date')
	context['form'] = form
	context['data'] = latest_campaign_list
	return render(request, 'home/index.html', context)

def map(request):
	context = {}
	if request.method == 'POST':
		form = NewCampaignForm(request.POST)
		if form.is_valid():
			form.save()
			form = NewCampaignForm()
			
	else:
		form = NewCampaignForm()
	latest_campaign_list = NewCampaign.objects.order_by('-pub_date')
	context['form'] = form
	context['data'] = latest_campaign_list
	return render(request, 'home/resist-home.html', context)

def detail(request, pk):
	context = {}
	try:
		campaign = NewCampaign.objects.get(pk=pk)
		
	except NewCampaign.DoesNotExist:
		raise Http404("Campaign does not exist")

	if request.method == 'POST':
		form = AttendingForm(request.POST)
		if form.is_valid():
			campaign.attendees += 1
			submitted = True
			context['submitted'] = submitted
			campaign.save()
			form = AttendingForm()		
	else:
		form = AttendingForm()
			
	context['form'] = form
	context['campaign'] = campaign


	return render(request, 'home/detail.html', context)

