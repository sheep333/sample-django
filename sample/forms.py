from django import forms
from django.core.validators import RegexValidator

from .models import Dog


class Sample1Form(forms.Form):
    text = forms.CharField(label='text', max_length=255)


class Sample2Form(forms.Form):
    """
    Djangoで使えるFormのフィールド
    https://docs.djangoproject.com/ja/3.0/ref/forms/fields/

    引数として与えられるもの
    https://docs.djangoproject.com/ja/3.0/ref/forms/fields/#core-field-arguments
    """
    text1 = forms.CharField(label='text', max_length=255, required=False)
    num1 = forms.IntegerField(label='数字', required=False)
    yes_no = forms.BooleanField(label='yes_no', required=True)
    choice1 = forms.fields.ChoiceField(
        label='Single Choice',
        help_text='1つ選んでください',
        choices=(
            ('ja', '日本'),
            ('us', 'アメリカ'),
            ('uk', 'イギリス'),
            ('ch', '中国'),
            ('kr', '韓国')
        ),
        required=True
    )
    choice2 = forms.fields.MultipleChoiceField(
        label='Multiple Choice',
        help_text='複数選択が可能です',
        choices=(
            ('ja', '日本'),
            ('us', 'アメリカ'),
            ('uk', 'イギリス'),
            ('ch', '中国'),
            ('kr', '韓国')
        ),
        required=False
    )
    num2 = forms.IntegerField(
        label='数字',
        required=True,
        validators=[RegexValidator(r'^(0[0-9]*)$', 'Only digit characters.')],
    )
    text2 = forms.CharField(
        label='text',
        max_length=255,
        required=False,
        disabled=True
    )


class Sample3Form(forms.Form):
    """
    各フィールドにはデフォルトでWidgetが設定されている
    例) https://docs.djangoproject.com/ja/3.0/ref/forms/fields/#booleanfield

    Djangoで使えるフィールドのWidget
    https://docs.djangoproject.com/ja/3.0/ref/forms/fields/

    実際のHTMLテンプレート
    https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets
    """
    choice1 = forms.fields.ChoiceField(
        label='Single Choice',
        help_text='1つ選んでください',
        choices=(
            ('ja', '日本'),
            ('us', 'アメリカ'),
            ('uk', 'イギリス'),
            ('ch', '中国'),
            ('kr', '韓国')
        ),
        required=True,
        widget=forms.RadioSelect()
    )
    choice2 = forms.fields.MultipleChoiceField(
        label='Multiple Choice',
        help_text='複数選択が可能です',
        choices=(
            ('ja', '日本'),
            ('us', 'アメリカ'),
            ('uk', 'イギリス'),
            ('ch', '中国'),
            ('kr', '韓国')
        ),
        required=False,
        widget=forms.CheckboxSelectMultiple()
    )


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

    birthday = forms.DateField(
        input_formats=('%Y-%m-%d', '%Y/%m/%d'),
        required=True,
    )