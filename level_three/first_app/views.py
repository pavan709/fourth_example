from django.shortcuts import render
from . import forms


# Create your views here.


# There 2 situations: using basic Form (forms.Form) and ModelForm (forms.ModelForm).
#
# If you are using a ModelForm then there is no any need of playing with a cleaned_data dictionary because when you
# do form.save() it is already be matched and the clean data is saved. But you are using basic Form then you have to
# manually match each cleaned_data to its database place and then save the instance to the database not the form.
#
# For example basic Form:
#
# if form.is_valid():
#     ex = Example()
#     ex.username = form.cleaned_data['username']
#     ex.save()
# For example ModelForm:
#
# if form.is_valid():
#     form.save()
# NOTE: If the form pass from is_valid() stage then there is no any unvalidated data.






# form.cleaned_data returns a dictionary of validated form input fields and their values, where string primary keys
# are returned as objects.
#
# form.data returns a dictionary of un-validated form input fields and their values in string format (i.e. not objects).
#
# Example by code
# In my forms.py I have two fields:
#
# class Loginform(forms.Form):
#     username=forms.CharField()
#     password=forms.CharField(widget=forms.PasswordInput)
# and in my views.py:
#
# def login_page(request):
#     form=Loginform(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
# The above code prints the following output:
#
# {'username': 'xyz', 'password': 'shinchan'}
# If instead views.py contains:
#
# def login_page(request):
#     form=Loginform(request.POST or None)
#     if form.is_valid():
#         print(form)
# The above code prints the following:
#
#  <tr><th><label for="id_username">Username:</label></th><td><input type="text" name="username" value="xyz" required id="id_username"></td></tr>
# <tr><th><label for="id_password">Password:</label></th><td><input type="password" name="password" required id="id_password"></td></tr>


def index(request):
    return render(request, 'first_app/index.html')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        # our custom validation in forms.py are done in below line like clean() & validators in form field
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('VALIDATAION SUCCESS!')
            print('NAME: '+form.cleaned_data['name'])
            print('email: '+form.cleaned_data['email'])
            print('text: '+form.cleaned_data['text'])


    return render(request, 'first_app/form_page.html', {'form': form})
