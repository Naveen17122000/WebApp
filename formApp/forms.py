from django import forms
from django.core.exceptions import ValidationError
from . models import Employee

gen_choices=(
    ('M','Male'),
    ('F','Female'),
)
def checksalary(sal):
    if sal<200000:
        raise ValidationError('salary should be more then 2 lakh')
    
class Formclass(forms.Form):
    empno = forms.IntegerField(required = True)
    empname = forms.CharField(max_length=20)
    salary = forms.IntegerField(validators=[checksalary])
    doj = forms.DateField(widget=forms.SelectDateWidget(years=range(1990,2040)))
    gender = forms.ChoiceField(choices = gen_choices)

    def clean_empname(self):
        ename = self.cleaned_data['empname']
        #if ename.startswith('s') == False:
         #   raise ValidationError('Empname is not startwith s')
        
        return ename
    