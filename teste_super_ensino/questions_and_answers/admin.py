from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question, Student, Alternative, QuestionAndAnswer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Alternative)
class AlternativeAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionAndAnswer)
class StudentAdmin(admin.ModelAdmin):
    pass
