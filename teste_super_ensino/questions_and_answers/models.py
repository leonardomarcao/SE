import uuid
from django.db import models
from django.utils import timezone


class Student(models.Model):
    """A class model for Student from Super Ensino"""

    student_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.TextField(null=False, max_length=150)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "student"
        ordering = ["student_id"]


class Question(models.Model):
    """A class model for the question"""

    question_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=150)
    text = models.TextField(null=False, default="")
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "question"
        ordering = ["question_id"]


class Alternative(models.Model):
    """A class model for the alternative"""

    alternative_id = models.AutoField(primary_key=True, auto_created=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(null=False, default="")
    is_correct = models.BooleanField(null=False)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "alternative"
        ordering = ["alternative_id"]


class QuestionAndAnswer(models.Model):
    """A class models for the question and answer for the student"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    alternative_id = models.ForeignKey(Alternative, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    answered_time = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = "question_and_answer"
        ordering = ["answered_time"]

