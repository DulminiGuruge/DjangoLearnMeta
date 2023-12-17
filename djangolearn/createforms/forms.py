from django import forms

SHIFTS = (
    ("1","Morning"),
    ("2","Afternoon"),
    ("3","Evening"),

)

class InputFrom(forms.Form):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()