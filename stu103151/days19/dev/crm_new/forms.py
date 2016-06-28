from django import forms
from crm_new import models
class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        exclude = ()
class CourseModelForm(forms.ModelForm):
    class Meta:
        model = models.Course
        exclude = ()
class SchoolModelForm(forms.ModelForm):
    class Meta:
        model = models.School
        exclude = ()
class ClassListModelForm(forms.ModelForm):
    class Meta:
        model = models.ClassList
        exclude = ()
class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        exclude = ()

class CourseRecordModelForm(forms.ModelForm):
    class Meta:
        model = models.CourseRecord
        exclude = ()
class StudyRecordModelForm(forms.ModelForm):
    class Meta:
        model = models.StudyRecord
        exclude = ()