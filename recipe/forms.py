from django import forms
from .models import Recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description','image')

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        # self.fields['location'].widget.attrs['placeholder'] = 'Type in your city.'
        # self.fields['address'].widget.attrs['placeholder'] = 'Type in your address.'

        for visible in self.visible_fields():
            if visible.__dict__.get('name')=='image':
                print(visible.field)
                print("hh")
                visible.field.widget.attrs['class'] = 'myInput'

            else:
                visible.field.widget.attrs['class'] = 'form-control'
            # print(str(visible) is '<input type="file" name="image" accept="image/*" id="id_image">')
            print(dir(visible))
            print(visible.__dict__.get('name'))
