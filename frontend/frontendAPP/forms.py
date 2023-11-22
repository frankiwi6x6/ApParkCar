from django import forms

class CalificacionForm(forms.Form):
    id_usuario = forms.CharField(max_length=100)
    id_calificado = forms.CharField(max_length=100)
    calificacion = forms.CharField(max_length=100)
    comentario = forms.CharField(max_length=100)
    fecha = forms.DateField(widget=forms.DateInput())

class InicioSesionForm(forms.Form):
    email = forms.CharField(label='Correo')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class registerForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    email = forms.EmailField(label='Email', max_length=100)
    ApPaterno = forms.CharField(label='Apellido Paterno', max_length=50)
    ApMaterno = forms.CharField(label='Apellido Materno', max_length=50)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput)
    confirmarPassword = forms.CharField(label='Confirmar Contraseña', max_length=100, widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput)
    tipo_usuario = forms.BooleanField(required=False)
