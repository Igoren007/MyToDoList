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
                      ('H', 'высокий'),
                      ('M', 'обычный'),
                      )
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'create__task-input'}))
    descr = forms.CharField(label='Краткое описание', widget=forms.Textarea(attrs={'class': 'create__task-input-textarea'}))
    priority = forms.ChoiceField(label='Приоритет', choices=PRIORITY_LEVEL, widget=forms.RadioSelect(attrs={'class': 'sort__select'}))

    class Meta:
        model = Task

        fields = ('title', 'descr', 'priority')


class TaskEditForm(UpdateView):
    """
    Форма для создания новой задачи
    """
    PRIORITY_LEVEL = (('L', 'low'),
                      ('H', 'hight'),
                      ('M', 'medium'),
                      )
    title = forms.CharField(label='Задача', widget=forms.TextInput(attrs={'class': 'user_settings__input'}))
    descr = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'user_settings__input'}))
    priority = forms.ChoiceField(label='Приоритет', choices=PRIORITY_LEVEL)
    is_finished = forms.BooleanField(label='Закончена?', widget=forms.TextInput(attrs={'class': 'user_settings__input'}))

    class Meta:
        model = Task
        fields = ('title', 'descr', 'priority', 'is_finished')

        fields = ('title', 'descr', 'priority')


class TaskSort(forms.Form):
    SORT_TYPE = (('date_new', 'сначала новые'),
                 ('date_old', 'сначала старые'),
                ('priority', 'по важности'),
                )
    sort = forms.ChoiceField(choices=SORT_TYPE)