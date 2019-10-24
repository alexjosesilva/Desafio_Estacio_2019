

from django import forms

from authweb.models import Usuario, Foo, TipoLaboratorio, Situacao, Recurso, Reserva,\
    Curso
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import CheckboxInput
from pickle import NONE

class LoginUsuarioForm(AuthenticationForm):
    """
    email = forms.CharField(required =True, max_length=255, help_text='100 characters max.')
    matricula = forms.CharField(required =True,max_length=14, help_text='100 characters max.')
"""
    """
    matricula = forms.CharField(required =True, max_length=14, help_text='Matricula.', initial = "test")
    email = forms.CharField(required =True, max_length=255, help_text='Email.', initial = "123456")
    """
    
    class Meta:
        # Modelo base
        model = Usuario
        # Campos que estarão no form
        
        fields = [         
        'matricula',
        'password',
        'email',
        'categoria'       
        ]
      


class InsereUsuarioForm(forms.ModelForm):
    

    class Meta:
        # Modelo base
        model = Usuario
        # Campos que estarão no form
        fields = [         
        'matricula',
        'password',
        'email',
        'categoria',
        'username',
        'nome'       
        ]
    
class InsereTipoLaboratorioForm(forms.ModelForm):
    

    class Meta:
        # Modelo base
        model = TipoLaboratorio
        # Campos que estarão no form
        fields = [
     
         
        'nome',
        'descricao',
  
        ]
        
class InsereSituacaoForm(forms.ModelForm):
    

    class Meta:
        # Modelo base
        model = Situacao
        # Campos que estarão no form
        fields = [
     
         
        'nome',
        'descricao',
  
        ]
        
class InsereLaboratorioForm(forms.ModelForm):
    

        class Meta:
            # Modelo base
            model = Recurso
            # Campos que estarão no form
            fields = [
         
             
                'localizacao',
                'sala',
                'descricao',
                'tipo_laboratorio'
      
            ]
            
class InsereProjetorForm(forms.ModelForm):
    

        class Meta:
            # Modelo base
            model = Recurso
            # Campos que estarão no form
            fields = [
         
             
                'numero',
                'descricao',
      
            ]
            


class InsereReservaLaboratorioUsuariosForm(forms.ModelForm):
    
        data_uso =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_uso =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        data_liberacao =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_liberacao =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        id_recurso = forms.ModelChoiceField(queryset=Recurso.objetos.filter(tipo_recurso="laboratorio"))
        id_usuario = forms.ModelChoiceField(queryset=Usuario.objetos.filter(is_staff=False))
        class Meta:
            # Modelo base
            model = Reserva
            # Campos que estarão no form
            fields = [
         
             
            #'data_hora_chegada',
            #'data_hora_saida',
            'justificativa',
            'disciplina',
            'id_recurso',
            'id_usuario',
            

            ]
            """widgets = {
            'my_date': forms.DateInput(),
            'my_time': forms.TimeInput(attrs={'type': 'time'})
            }"""
            

            
class InsereReservaLaboratorioForm(forms.ModelForm):
    
        data_uso =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_uso =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        data_liberacao =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_liberacao =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        id_recurso = forms.ModelChoiceField(queryset=Recurso.objetos.filter(tipo_recurso="laboratorio"))
        class Meta:
            # Modelo base
            model = Reserva
            # Campos que estarão no form
            fields = [
         
             
            #'data_hora_chegada',
            #'data_hora_saida',
            'justificativa',
            'disciplina',
            'id_recurso',
            

            ]
            """widgets = {
            'my_date': forms.DateInput(),
            'my_time': forms.TimeInput(attrs={'type': 'time'})
            }"""

class InsereReservaProjetorUsuariosForm(forms.ModelForm):
    
        data_uso =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_uso =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        data_liberacao =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_liberacao =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        """id_recurso = forms.ModelChoiceField(queryset=Recurso.objetos.filter(tipo_recurso="projetor"),widget=forms.RadioSelect(attrs={
            'display': 'inline-block',
        }), to_field_name="numero", empty_label =None)"""
        id_recurso = forms.ModelChoiceField(queryset=Recurso.objetos.filter(tipo_recurso="projetor"))
        primeira_aula = forms.BooleanField(widget=forms.CheckboxInput)
        segunda_aula = forms.BooleanField(widget=forms.CheckboxInput)
        id_usuario = forms.ModelChoiceField(queryset=Usuario.objetos.filter(is_staff=False))
        class Meta:
            # Modelo base
            model = Reserva
            # Campos que estarão no form
            fields = [
         
             
            #'data_hora_chegada',
            #'data_hora_saida',
            'curso',
            'primeira_aula',
            'segunda_aula',
            'id_recurso',
            'id_usuario'
            

            ]
            
            
class InsereReservaProjetorForm(forms.ModelForm):
    
        data_uso =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_uso =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        data_liberacao =  forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}))
        time_liberacao =  forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
        """id_recurso = forms.ModelChoiceField(queryset=Recurso.objetos.filter(tipo_recurso="projetor"),widget=forms.RadioSelect(attrs={
            'display': 'inline-block',
        }), to_field_name="numero", empty_label =None)"""
        id_recurso = forms.ModelChoiceField(queryset=Recurso.objetos.filter(tipo_recurso="projetor"))
        primeira_aula = forms.BooleanField(widget=forms.CheckboxInput)
        segunda_aula = forms.BooleanField(widget=forms.CheckboxInput)
        class Meta:
            # Modelo base
            model = Reserva
            # Campos que estarão no form
            fields = [
         
             
            #'data_hora_chegada',
            #'data_hora_saida',
            'curso',
            'primeira_aula',
            'segunda_aula',
            'id_recurso',
            

            ]
            
class InsereCursoForm(forms.ModelForm):
    

        class Meta:
            # Modelo base
            model = Curso
            # Campos que estarão no form
            fields = [
         
             
            'nome',
      
            ]
        
class InsereFooForm(forms.ModelForm):
    

        class Meta:
            # Modelo base
            model = Foo
            # Campos que estarão no form
            fields = [
         
             
            'name',
      
            ]
    
    