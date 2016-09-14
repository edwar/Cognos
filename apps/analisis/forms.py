from django import forms

class ExcelForm(forms.ModelForm):
    class Meta:
        model=Excel
