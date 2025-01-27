from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User #Usuario
from django.contrib.auth.hashers import make_password 


class TipoDeAbogadoForm(forms.ModelForm):
    class Meta:
        model=TipoDeAbogado
        fields='__all__'
        labels={
            'nombre': 'Nombre del tipo',
            'descripcion':'Descripcion'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del tipo de abogado',
                    'id':'nombre',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion del tipo de abogado',
                    'id':'descripcion',
                }
            ),
        }
    
class FormLogin(AuthenticationForm):
    class Meta:
        db_table = Usuario
        fields=['correo','password']
        labels={
            'username': 'Nombre del tipo',
            'password':'Contraseña'
        }
    
        widgets={
            'correo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el correo ',
                    'id':'correo'
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese contraseña',
                    'id':'password',
                }
            ),
        }
    # def __init__(self, *args, **kwargs):
    #     super(FormLogin, self).__init__(*args,**kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
    #     self.fields['password'].widget.attrs['class'] = 'form-control'
    #     self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
    
class CasoForm(forms.ModelForm):
        
    class Meta:
        model=Caso
        fields='__all__'
        labels={
            'codigo': 'Codigo',
            'descripcion':'Descripcion'
        }
        widgets={

            'id_cliente': forms.Select(
                attrs={
                    'id':'id_cliente',
                    'class':'form-control form-control-sm col-sm-6',
                }
            ),
            'id_abogado': forms.Select(
                attrs={
                    'id':'id_abogado',
                    'class':'form-control form-control-sm col-sm-6',
                }
            ),
            'codigo': forms.TextInput(
                attrs={
                    'class':'form-control form-control-sm col-sm-6',
                    'placeholder':'Ingrese el codigo del caso',
                    'id':'codigo',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control form-control-sm col-sm-6',
                    'placeholder':'Ingrese descripcion del tipo de abogado',
                    'id':'descripcion',
                }
            ),
            'estado':forms.Select(
                attrs={
                    'id':'estado',
                    'class':'form-control form-control-sm col-sm-6'
                }
            ),
            'tipo_de_proceso':forms.Select(
                attrs={
                    'id':'tipo_de_proceso',
                    'class':'form-control form-control-sm col-sm-6'
                }
            ),
            'tipo_pago':forms.RadioSelect(
                attrs={
                    '':'Contado',
                    '':'Credito',
                    'id':'tipo_pago',
                }
            ),
            
            
        }
    
class TipoDeProcesoForm(forms.ModelForm):
    class Meta:
        model=TipoDeProceso
        fields='__all__'
        labels={
            'nombre': 'Nombre del tipo',
            'descripcion':'Descripcion'
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del tipo de proceso',
                    'id':'nombre',
                    
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese descripcion del tipo de proceso',
                    'id':'descripcion',
                }
            ),
        }
    
#para registrar superusuarios
class FormRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'password',
        }
        ),max_length = 150)
    password1 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'confirm password',
        }
        ),max_length = 150)

    class Meta:
        model=Usuario
        fields=('correo','nombre')
    
    
    def clean_email(self):
        correo=self.cleaned_data.get('correo')
        qs=Usuario.objects.filter(correo=correo)
        if qs.exists():
            raise forms.ValidationError("Correo ya registrado")
        return correo
    
    def clean_password2(self):
        password1=self.clean_data.get("password1")
        password2=self.clean_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
#para actualizar usuario
class FormActualizarUsuario(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model = Usuario
        fields = ('correo','password','nombre','apellido')
    
    def clean_password(self):
        return self.initial['password']

class FormCliente(forms.ModelForm):
    # password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
    #     attrs={
    #         'class':'form-control',
    #         'placeholder':'Contraseña',
    #         'id':'password1',
    #         'required':'required'
    #     }
    #     ))
    # password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(
        # attrs={
        #     'class':'form-control',
        #     'placeholder':'Confirmar Contraseña',
        #     'id':'password2',
        #     'required':'required'
        # }
        # ))
    class Meta:
        model=Cliente
        fields=('nombre','apellido','dui','direccion','correo','telefono','estado_civil','fecha_nacimiento')
        widgets={
                 'nombre': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre del cliente',
                         'id':'nombre',
                       
                     }
            ),
                 'correo':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese correo del cliente',
                         'id':'correo',
                     }
            ),
                 'apellido':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese apellido del cliente',
                         'id':'apellido',
                     }
                 ),
                 'direccion':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese la direccion del cliente',
                         'id':'direccion',
                     }
            ),
                 'telefono':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese telefono del cliente',
                         'id':'telefono',
                     }
            ),
                 'dui': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el dui del cliente',
                         'id':'dui',
                       
                     }
            ),
                 'estado_civil':forms.Select(
                attrs={
                    'id':'estado_civil',
                    'class':'form-control form-control-sm col-sm-2'
                }
            ),
                 'fecha_nacimiento':forms.DateInput(
                     attrs={
                         'class':'form-control form-control-sm col-sm-4',
                         'type': 'date',
                         'id':'fecha_nacimiento'
                         }
    
                 )
                 
             }

    def clean_password2(self):
        password1=make_password('')
        # password2=self.cleaned_data.get("password2")
        # if password1!=password2:
        #     raise forms.ValidationError("Contraseñas no coinciden")
        # return password2
    
    def save(self,commit=True):
         #guarda contraseña en formato Hash
         #crea una contraseña aleatoria
        password1=BaseUserManager().make_random_password(15)
        nombre=self.cleaned_data.get("nombre")
        apellido=self.cleaned_data.get("apellido")
        
        usuario=super().save(commit=False)
        #Se crea un usuario aleatorio
        usuario.username=nombre[0:2]+apellido[0:2]
        #usar es cliente si es necesario, se debe de agregar al modelo de cliente
        #usuario.es_cliente=True
        usuario.set_password(password1)
        
        if commit:
            usuario.save()
        return usuario

class FormUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Contraseña',
            'id':'password1',
            'required':'required'
        }
        ))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirmar Contraseña',
            'id':'password2',
            'required':'required'
        }
        ))
    class Meta:
        model=Usuario
        fields=('correo','nombre','apellido',)
        widgets={
                 'nombre': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre del cliente',
                         'id':'nombre',
                       
                     }
                 ),
                 'correo':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese correo del cliente',
                         'id':'descripcion',
                     }
                 ),
                 'apellido':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese apellido del cliente',
                         'id':'descripcion',
                     }
                 ),
                 'direccion':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese la direccion del cliente',
                         'id':'descripcion',
                     }
                 ),
                 'telefono':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese telefono del cliente',
                         'id':'descripcion',
                     }
                 ),
             }
       
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self,commit=True):
         #guarda contraseña en formato Hash
        usuario=super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario

class FormAbogado(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Contraseña',
            'id':'password1',
            'required':'required'
        }
        ))
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirmar Contraseña',
            'id':'password2',
            'required':'required'
        }
        ))
    class Meta:
        model=Cliente
        fields='__all__'
        widgets={
                 'nombre': forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese el nombre del cliente',
                         'id':'nombre',
                       
                     }
                 ),
                 'correo':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese correo del cliente',
                         'id':'descripcion',
                     }
                 ),
                 'apellido':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese apellido del cliente',
                         'id':'descripcion',
                     }
                 ),
                 'direccion':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese la direccion del cliente',
                         'id':'descripcion',
                     }
                 ),
                 'telefono':forms.TextInput(
                     attrs={
                         'class':'form-control',
                         'placeholder':'Ingrese telefono del cliente',
                         'id':'descripcion',
                     }
                 ),
             }
       
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1!=password2:
            raise forms.ValidationError("Contraseñas no coinciden")
        return password2
    
    def save(self,commit=True):
         #guarda contraseña en formato Hash
        usuario=super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class FormaDePagoForm(forms.ModelForm):
    class Meta:
        model=FormaDePago
        fields='__all__'
        labels={
          
        }
        widgets={

           'plazo':forms.NumberInput (
                attrs={
                    'class':'form-control form-control-sm col-sm-4',
                    'placeholder':'Ingrese cantidad del plazo',
                    'id':'plazo',
                }
            ),   

           'cuota':forms.NumberInput(
                attrs={
                    'id':'cuota',
                    'class':'form-control form-control-sm col-sm-4'
                }
            ),
        
            'monto':forms.TextInput(
                     attrs={
                         'class':'form-control form-control-sm col-sm-4',
                         'id':'monto'
                         }
    
                 ),

            'fecha_fin_credito':forms.DateInput(
                     attrs={
                         'class':'form-control form-control-sm col-sm-4',
                         'type': 'date',
                         'id':'fecha_fin_credito'
                         }
    
                 )
        }