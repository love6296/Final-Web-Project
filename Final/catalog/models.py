from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instance





# Create your models here.


        
        
class School(models.Model):
    """Model representing an author."""

    school_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=7)
    phone = models.CharField(max_length=10)
    
    

    class Meta:
        ordering = ['school_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('school-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.school_name}'
        
        
        
        
        
        
        
class Exam(models.Model):
    """Model representing an exam."""
    test_name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ['test_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('test-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.test_name}'
        
        
        
        
       
        
        
        
class Coordinators(models.Model):
    """Model representing an coordinator."""
    def display_school(self):
        """Create a string for the School. This is required to display school in Admin."""
        return ', '.join(school.school_name for school in self.school.all()[:100])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    school = models.ManyToManyField(School, help_text='Select a school')
    email = models.CharField(max_length=100)
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular coordinator instance."""
        return reverse('coordinator-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
        
        
        

        
class TestSchedule(models.Model):
    """Model representing a specific instance of test registration."""
    def display_schools(self):
        return ', '.join(school.school_name for school in self.school.all()[:100])

    
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    YES ='Y'
    NO = 'N'
    SUBSTITUTE_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    List1 = list(Exam.objects.all())
    PickList=[]
    for i in range(len(List1)):
        a = str(List1[i])
        b = str(List1[i])
        List2 = (a,b)
        PickList.append(List2)
        
    c = ('No','-------')   
    PickList.insert(0,c)
    PickTuple = tuple(PickList)

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular test registration')
    school = models.ManyToManyField(School, help_text='Select a school')
    student_first = models.CharField(max_length=100)
    student_last = models.CharField(max_length=100)
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    substitute = models.CharField(
        max_length=1,
        choices=SUBSTITUTE_CHOICES,
        default=NO,
    )
    
    Time_1 = models.CharField(
        max_length=30,
        choices=PickTuple,
        default='No',
    )
    Time_2 = models.CharField(
        max_length=30,
        choices=PickTuple,
        default='No',
    )
    Time_3 = models.CharField(
        max_length=30,
        choices=PickTuple,
        default='No',
    )

    

    class Meta:
        ordering = ['student_last', 'student_first']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.school})'
