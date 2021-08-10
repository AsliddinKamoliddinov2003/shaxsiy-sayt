from django.db.models import fields
from TATU.models import Students
from django import forms


class StudentsForm(forms.ModelForm):
    class Meta:
        model  = Students
        fields = "__all__"


        def __init__(self, *args, **kwargs):
            super(StudentsForm,self).__init__(*args, **kwargs)


            for field in self.fields:
                self.fields[field].widget.attrs["class"] = "form-control"

