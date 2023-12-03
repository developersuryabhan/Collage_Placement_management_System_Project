# placement_app/forms.py
from django import forms
from .models import Companies, Interviews, Placements, Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'branch', 'gpa']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50
    # interview_date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
            

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['co_name', 'industry', 'location']
    
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interviews
        fields = ["student","company","interview_date"]

    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50
    interview_date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))


class InterviewEditForm(forms.ModelForm):
    class Meta:
        model = Interviews
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(InterviewEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50
    interview_date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))

class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placements
        fields = ["interview","placement_date","offered_salary"]


    def __init__(self, *args, **kwargs):
        super(PlacementForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50
    placement_date = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
