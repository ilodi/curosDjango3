# Crea formularios conrectamente
from django import forms
#Importar libreria de validaciones
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mete el titulo',
                'class': 'input-Sty'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es muy corto'),
            validators.RegexValidator('[A-Za-z0-9ñ ]*$', "El titulo esta mal formado", 'invalid_title')
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(140, 'Tienes mucho texto')
        ]
    )
    #segunda forma de modificar los atributos
    content.widget.attrs.update({
        'placeholder': 'Mete el contenido',
        'class': 'input-Sty',
        'id': 'contenido_form'
    })

    # agregar input form
    public_option = [
        (0, 'Si'),
        (1, 'No')
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_option
    )
