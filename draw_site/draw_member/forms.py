from django import forms
from .models import Member


def member_group_choices():
    valid_groups = Member.objects.unique_groups()
    choices = []
    for grp in valid_groups:
        choices.append((grp, grp))
    choices.append(('ALL', '（全）'))
    return choices


class DrawForm(forms.Form):
    group = forms.ChoiceField(
        choices=member_group_choices,
        label='團隊名稱',
        label_suffix='：',
        widget=forms.RadioSelect,
        initial='ALL'
    )

