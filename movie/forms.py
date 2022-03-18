from django import forms
from movie.models import Movie,Category

class MovieForm(forms.ModelForm):
    # category = models.forms.ChoiceField(, choices=[CHOICES], required=False)
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH,help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=Page.URL_MAX_LENGTH,help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)



    class Meta:
        model = Page
        fields = ('category',)

    views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)