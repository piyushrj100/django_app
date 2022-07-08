from django.forms import ModelForm
from django import forms
from .models import Project, Review


#will generate the form based on what we have for Project Model. Now to use it, import in views
class ProjectForm(ModelForm) :
    class Meta:
        model=Project
        # fields='__all__'
        fields=['title','description','featured_image','demo_link','source_link']
    def __init__(self, *args, **kwargs) :
        super(ProjectForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attr.update({'class':'input','placeholder':'Add title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm(ModelForm) :
    class Meta :
        model=Review 
        fields =['value','body']
        labels ={
            'value' : 'Place your vote',
            'body' : 'Add a comment with your vote'
        }
    
    def __init__(self, *args, **kwargs) :
        super(ReviewForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attr.update({'class':'input','placeholder':'Add title'})
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

