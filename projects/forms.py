from django.forms import ModelForm
from .models import Project


#will generate the form based on what we have for Project Model. Now to use it, import in views
class ProjectForm(ModelForm) :
    class Meta:
        model=Project
        # fields='__all__'
        fields=['title','description','featured_image','demo_link','source_link','tags']


