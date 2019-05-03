from django.shortcuts import render
from catalog.models import Exam, School, Coordinators, TestSchedule


# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tests = Exam.objects.all().count()
    num_schools = School.objects.all().count()
    
    # How many students (status = 'a')
    num_applications = TestSchedule.objects.count()
    
    # The 'all()' is implied by default.    
    num_coordinators = Coordinators.objects.count()
    
    context = {
        'num_schools': num_schools,
        'num_tests': num_tests,
        'num_coordinators': num_coordinators,
        'num_applications': num_applications,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.models import School
from catalog.models import Coordinators
from catalog.models import TestSchedule

class SchoolListView(generic.ListView):
    model = School
    paginate_by = 25
    
class SchoolDetailView(generic.DetailView):
    model = School


class SchoolCreate(CreateView):
    model = School
    fields = '__all__'


class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'

class SchoolDelete(DeleteView):
    model = School
    success_url = reverse_lazy('schools')
    
    
    
class CoordinatorsListView(generic.ListView):
    model = Coordinators
    paginate_by = 25
    
class CoordinatorsDetailView(generic.DetailView):
    model = Coordinators


class CoordinatorsCreate(CreateView):
    model = Coordinators
    fields = '__all__'


class CoordinatorsUpdate(UpdateView):
    model = Coordinators
    fields = '__all__'

class CoordinatorsDelete(DeleteView):
    model = Coordinators
    success_url = reverse_lazy('coordinators')
    
    
    
class TestScheduleListView(generic.ListView):
    model = TestSchedule
    paginate_by = 25
    
class TestScheduleDetailView(generic.DetailView):
    model = TestSchedule


class TestScheduleCreate(CreateView):
    model = TestSchedule
    fields = '__all__'


class TestScheduleUpdate(UpdateView):
    model = TestSchedule
    fields = '__all__'

class TestScheduleDelete(DeleteView):
    model = TestSchedule
    success_url = reverse_lazy('testschedules')