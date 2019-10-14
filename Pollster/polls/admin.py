from django.contrib import admin
from .models import Questions, Choice
# Register your models here.


#admin.site.register(Questions) # show Question class and Choices on home page
#admin.site.register(Choice)

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin area"
admin.site.index_title = "Welcome to Pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
      (None, {'fields': ['question_text']}),
      ('Date published', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionsAdmin)