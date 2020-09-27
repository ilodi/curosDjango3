# Crea formularios conrectamente
from django import forms


class FormArticle(forms.Form):
    title = forms.CharField(
        label="Titulo"
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )

    # agregar input form
    public_option = [
        (0, 'Si'),
        (1, 'No')
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_option
    )
