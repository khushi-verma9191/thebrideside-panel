from django.shortcuts import render
from .models import Lead
from django.utils.timezone import now, timedelta
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead, SalesRep
from django.db.models import Q
from .models import CallSchedule
from django.utils import timezone
from .forms import LeadForm

def admin_dashboard(request):
    today = now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)

    context = {
        'daily_count': Lead.objects.filter(event_date=today).count(),
        'weekly_count': Lead.objects.filter(event_date__gte=week_ago).count(),
        'monthly_count': Lead.objects.filter(event_date__gte=month_ago).count(),
        'service_counts': Lead.objects.values('service_type').annotate(count=Count('id')),
        'status_summary': Lead.objects.values('status').annotate(count=Count('id'))
    }

    return render(request, 'dashboard/dashboard.html', context)

def lead_list(request):
    service_filter = request.GET.get('service_type', '')
    leads = Lead.objects.all()
    
    for lead in leads:
        lead.suggested_time = suggest_call_time(lead.city)

    if service_filter:
        leads = leads.filter(service_type=service_filter)

    sales_reps = SalesRep.objects.all()

    # Assign rep logic
    if request.method == 'POST':
        lead_id = request.POST.get('lead_id')
        rep_id = request.POST.get('rep_id')
        scheduled_time = request.POST.get('scheduled_time')
        lead = get_object_or_404(Lead, id=lead_id)
        rep = get_object_or_404(SalesRep, id=rep_id)
        lead.assigned_to = rep

        if scheduled_time:
            lead.scheduled_time = scheduled_time
            
        lead.save()
        return redirect('lead_list')


    context = {
        'leads': leads,
        'sales_reps': sales_reps,
        'selected_service': service_filter,
    }
    return render(request, 'dashboard/leads.html', context)


def schedule_call(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    sales_reps = SalesRep.objects.all()

    if request.method == 'POST':
        datetime_str = request.POST.get('scheduled_time')
        rep_id = request.POST.get('rep')
        rep = get_object_or_404(SalesRep, id=rep_id)

        schedule = CallSchedule.objects.create(
            lead=lead,
            scheduled_time=datetime_str,
            rep=rep,
            status='Scheduled'
        )
        return redirect('lead_list')

    return render(request, 'dashboard/schedule_call.html', {'lead': lead, 'sales_reps': sales_reps})


def suggest_call_time(city):
    india_cities = ['Delhi', 'Mumbai', 'Bangalore']
    if city in india_cities:
        return "10AM–1PM or 5PM–7PM IST"
    else:
        return "7PM–10PM IST"

def lead_create(request):
    suggested_time = None

    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()
            city = lead.city
            suggested_time = suggest_call_time(city)
            return render(request, 'dashboard/lead_success.html', {'lead': lead, 'suggested_time': suggested_time})
    else:
        form = LeadForm()

    return render(request, 'dashboard/lead_form.html', {'form': form, 'suggested_time': suggested_time})