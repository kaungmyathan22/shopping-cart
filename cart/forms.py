from django import forms


class CartAddForm(forms.Form):

    CHOICES = ((str(i), i) for i in range(1, 20))

    quantity = forms.ChoiceField(
        choices=CHOICES,

    )
