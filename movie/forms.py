from django import forms
from movie.models import Movie,Category

class MovieForm(forms.ModelForm):
    CHAR_MAX_LENGTH = 128

    category = forms.ChoiceField(choices = [],required=False)
    movie_image = forms.ImageField()
    # name = forms.CharField(max_length=CHAR_MAX_LENGTH,help_text="Please enter the name of the Movie.")
    # url = forms.URLField(max_length=Page.URL_MAX_LENGTH,help_text="Please enter the URL of the page.")
    # views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    # slug = forms.SlugField(widget=forms.HiddenInput(),required=False)
    pub_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [(c.pk, c.name) for c in Category.objects.all()]

    class Meta:
        model = Movie
        fields = ['name','director','lead_actor','movie_image','description','pub_date',]