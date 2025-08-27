from django.contrib import admin
from enroll.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('age',)
    ordering = ('-created_at',)

admin.site.register(Student, StudentAdmin)
