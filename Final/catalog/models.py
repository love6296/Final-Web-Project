from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances




# Create your models here.

#class Genre(models.Model):
#    """Model representing a book genre."""
#    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
#    
#    def __str__(self):
#        """String for representing the Model object."""
#        return self.name
        
        
        
        
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
        
        
        
        
        


#class Book(models.Model):
#    """Model representing a book (but not a specific copy of a book)."""
#    title = models.CharField(max_length=200)
#
#    # Foreign Key used because book can only have one author, but authors can have multiple books
#    # Author as a string rather than object because it hasn't been declared yet in the file
#    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
#    
#    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
#    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
#    
#    # ManyToManyField used because genre can contain many books. Books can cover many genres.
#    # Genre class has already been defined so we can specify the object above.
#    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
#    
#    def __str__(self):
#        """String for representing the Model object."""
#        return self.title
#    
#    def get_absolute_url(self):
#        """Returns the url to access a detail record for this book."""
#        return reverse('book-detail', args=[str(self.id)])
        



        


#class BookInstance(models.Model):
#    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
#    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
#    imprint = models.CharField(max_length=200)
#    due_back = models.DateField(null=True, blank=True)
#
#    LOAN_STATUS = (
#        ('m', 'Maintenance'),
#        ('o', 'On loan'),
#        ('a', 'Available'),
#        ('r', 'Reserved'),
#    )
#
#    status = models.CharField(
#        max_length=1,
#        choices=LOAN_STATUS,
#        blank=True,
#        default='m',
#        help_text='Book availability',
#    )
#
#    class Meta:
#        ordering = ['due_back']
#
#    def __str__(self):
#        """String for representing the Model object."""
#        return f'{self.id} ({self.book.title})'



        
        
#class Author(models.Model):
#    """Model representing an author."""
#    first_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)
#    date_of_birth = models.DateField(null=True, blank=True)
#    date_of_death = models.DateField('Died', null=True, blank=True)
#
#    class Meta:
#        ordering = ['last_name', 'first_name']
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular author instance."""
#        return reverse('author-detail', args=[str(self.id)])
#
#    def __str__(self):
#        """String for representing the Model object."""
#        return f'{self.last_name}, {self.first_name}'
        
        
        
        
        
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
        
        
        
        
        
#class Student(models.Model):
#    """Model representing an student."""
#    first_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)
#    # ManyToManyField used because genre can contain many books. Books can cover many genres.
#    # Genre class has already been defined so we can specify the object above.
#    school = models.ManyToManyField(School, help_text='Select a school')
#    #school = models.CharField(max_length=100)
#    grade = models.IntegerField('Grade', null=False)
#    
#
#    class Meta:
#        ordering = ['last_name', 'first_name']
#
#    def get_absolute_url(self):
#        """Returns the url to access a particular student instance."""
#        return reverse('student-detail', args=[str(self.id)])
#
#    def __str__(self):
#        """String for representing the Model object."""
#        return f'{self.last_name}, {self.first_name}'
        
        
        
        
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
    def exam1(self):
        return ', '.join(Time_1.test_name for Time_1 in self.Time_1.all()[:100])
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

    Time_1 = models.ManyToManyField(Exam, help_text='Select an exam.')
    #Time_Slot_1030 = models.ForeignKey(Exam, on_delete=models.CASCADE)
    #Time_Slot_1130 = models.ManyToManyField(Exam, help_text='Select a genre for this book')
    

    class Meta:
        ordering = ['student_last', 'student_first']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.school})'
