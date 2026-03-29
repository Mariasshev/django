from django import forms

class RegistrationForm(forms.Form):
    # Текстове поле (Input type="text")
    username = forms.CharField(
        label="Логін", 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть логін'})
    )
    
    # Поле пароля (Input type="password")
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    # Числове поле (Input type="number")
    age = forms.IntegerField(
        label="Вік",
        min_value=12,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # Поле дати (Input type="date")
    birth_date = forms.DateField(
        label="Дата народження",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    
    # Чекбокс (Input type="checkbox")
    agree_to_terms = forms.BooleanField(
        label="Я погоджуюся з політикою конфіденційності",
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    # Вибір (Select)
    GENDER_CHOICES = [
        ('M', 'Чоловік'),
        ('F', 'Жінка'),
        ('O', 'Інше'),
    ]
    gender = forms.ChoiceField(
        label="Стать",
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    # Радіо-кнопки (Radio)
    experience = forms.ChoiceField(
        label="Рівень досвіду в програмуванні",
        choices=[('beginner', 'Новачок'), ('pro', 'Профі')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )