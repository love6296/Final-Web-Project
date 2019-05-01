from django.contrib import admin

# Register your models here.


from catalog.models import Exam, School, Coordinators, TestSchedule

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(Exam)
#admin.site.register(TestSchedule)
#admin.site.register(School)
#admin.site.register(Coordinators)
# Define the admin class
class ExamAdmin(admin.ModelAdmin):
    pass
    
class TestScheduleAdmin(admin.ModelAdmin):
    list_display = ('student_first', 'student_last', 'display_schools', 'year_in_school', 'Time_1','Time_2','Time_3')
    #list_filter = ('student_last','year_in_school')
    fieldsets = (
        ('Demographics', {
            'fields': [('student_first', 'student_last', 'school')]
        }),
        ('Test Schedule', {
            'fields': ('id','Time_1','Time_2','Time_3')
        }),
    )
    
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'address', 'city', 'state','zipcode','phone')
    
class CoordinatorsAdmin(admin.ModelAdmin):
    list_display = ('display_school', 'first_name', 'last_name', 'email')

# Register the admin class with the associated model
admin.site.register(Exam, ExamAdmin)
admin.site.register(TestSchedule, TestScheduleAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Coordinators, CoordinatorsAdmin)


