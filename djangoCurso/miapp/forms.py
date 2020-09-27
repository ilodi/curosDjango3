#Crea formularios conrectamente
from django import forms

class FormArticle(forms.Form):
    title = forms.CharField(
        label="Titulo"
    )

    content = forms.Textarea(
        label = "Contenido"
    )