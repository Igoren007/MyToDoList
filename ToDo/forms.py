from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

# представляет форпше му регистрации
from django.views.generic import UpdateView


from ToDo.models import CustomUser, Task


class RegisterCustomUserForm(UserCreationForm):
    """
        Форма для регистрации аккаунта пользователя
        """
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


# представляет форму авторизации
class LoginCustomUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))


class CustomUserEditForm(forms.ModelForm):
    """
    Форма для редактирования аккаунта пользователя
    """
    avatar = forms.ImageField(required=False,
                              label='Сменить аватар',
                              widget=forms.FileInput(attrs={
                                  'class': 'user_settings__input'
                              }))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'user_settings__input'}))
    email = forms.EmailField(label='Эл. почта', widget=forms.EmailInput(attrs={'class': 'user_settings__input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'user_settings__input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'user_settings__input'}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'user_settings__input'}))

    class Meta:
        model = CustomUser
        fields = ('avatar', 'username', 'email', 'first_name', 'last_name', 'date_of_birth')


class TaskCreateForm(forms.ModelForm):
    """
    Форма для создания новой задачи
    """
    PRIORITY_LEVEL = (('L', 'низкий'),
                      ('M', 'обычный'),
                      ('H', 'высокий'),
                      )
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'create__task-input'}))
    descr = forms.CharField(label='Описание задачи', widget=forms.Textarea(attrs={'class': 'create__task-input-textarea'}))
    priority = forms.ChoiceField(label='Приоритет', choices=PRIORITY_LEVEL, widget=forms.RadioSelect(attrs={'class': 'sort__select'}))

    class Meta:
        model = Task
        fields = ('title', 'descr', 'priority')


class TaskEditForm(forms.ModelForm):
    """
    Форма для редактирования задачи
    """
    class Meta:
        model = Task
        fields = ('title', 'descr', 'priority', 'is_finished')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'create__task-input'}),
            'descr': forms.Textarea(attrs={'class': 'create__task-input-textarea'}),
            'priority': forms.RadioSelect(attrs={'class': 'sort__select'})
        }
        labels = {
            'title': 'Заголовок',
            'descr': 'Описание задачи',
            'priority': 'Приоритет',
            'is_finished': 'Пометить как выполненную'
        }


class TaskSort(forms.Form):
    SORT_TYPE = (('date_new', 'сначала новые'),
                 ('date_old', 'сначала старые'),
                ('priority', 'по важности'),
                )
    sort = forms.ChoiceField(choices=SORT_TYPE)


class DatePeriodForm(forms.Form):
    start_date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    end_date = forms.DateTimeField(input_formats=['%d/%m/%Y'])

    fields = ('start_date', 'end_date')
