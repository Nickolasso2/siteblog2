from cProfile import label
from pyexpat import model
from django import forms
from  .models import Comment
from mptt.forms import TreeNodeChoiceField

class NewComment(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset= Comment.objects.all(),       required = False,
            widget = forms.Select(attrs={'style':'display:none'}), label='') # <=
                        # interchangable
                        # =>
                        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['parent'].required = False
    #     self.fields['parent'].widget.attrs.update(
    #         {'style': 'display:none'})
    #     self.fields['parent'].label = ''


    # widgets can be written down here or in class  Meta
    # content = forms.CharField(widget= forms.Textarea(attrs={'rows':3, 'cols':60}))
   
 
    class Meta:
        model= Comment
        fields = ['author', 'content', 'post', 'parent']
        widgets = {
            'content' : forms.Textarea(attrs={'rows':3, 'cols':60}),
            'author' : forms.TextInput(attrs={'style':'padding:0; width:40%'}),
            'post' : forms.TextInput(attrs={'style':'display:none'})
        }