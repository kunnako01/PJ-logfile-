from django import forms



class ContactForm(forms.Form):
    type1 = forms.ChoiceField(choices = (
    (1, ("All")),
    (2, ("IP")),
    (3, ("Status")),
    (4, ("Country")),
                            ),  initial='', widget=forms.Select(), required=True)
    number1 = forms.ChoiceField(choices = (
    (0, ("All")),
    (10, ("10")),
    (20, ("20")),
    (50, ("50")),
    (100, ("100"))
                            ),  initial='', widget=forms.Select(), required=True)
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    date2= forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )
    #date34 = forms.DateField()
    
       
            
            
            #class NameForm(forms.Form):
    #num11 = forms.CharField(max_length=100)
     #number_int = forms.IntegerField(default=0)
    #date34 = forms.DateField()