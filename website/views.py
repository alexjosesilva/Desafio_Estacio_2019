from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from authweb.models import Usuario, Foo, TipoLaboratorio, Situacao, Recurso, Reserva,\
    Curso
from django.contrib.auth.models import User, Permission
#FORM
from website.forms import InsereFooForm, InsereUsuarioForm, LoginUsuarioForm,\
    InsereTipoLaboratorioForm,InsereSituacaoForm, InsereLaboratorioForm,InsereReservaLaboratorioForm,\
    InsereCursoForm, InsereProjetorForm, InsereReservaProjetorForm,\
    InsereReservaLaboratorioUsuariosForm, InsereReservaProjetorUsuariosForm
from website.forms import AuthenticationForm
#SHORTCUTS
from django.shortcuts import redirect, render
from django.shortcuts import reverse
#
from django.contrib.auth.mixins import LoginRequiredMixin,\
    PermissionRequiredMixin

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView, LoginView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.conf import settings

from datetime import datetime
from datetime import timedelta

from django.contrib import messages
from django.db.models import Q






#from django.views.generic.edit import FormView
#class LogView(FormView):



#LOGIN E LOGOUT https://github.com/django/django/blob/master/django/contrib/auth/views.py#L38

class IndexTemplateView(TemplateView):
    template_name = "website/index.html"
    
    
class AgendaTemplateView(TemplateView):
    template_name = "website/fullcalendar/agenda.html"
    
    
class AgendaRecursoTemplateView(ListView):
    template_name = "website/fullcalendar/recurso.html"
    model = Recurso
    context_object_name = "recursos"
    
    def get_context_data(self, **kwargs):
        context = super(AgendaRecursoTemplateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['reservas'] = Reserva.objetos.all()
        
        # And so on for more models
        return context



class CustomLogoutView(LogoutView):
    #template_name = "website/account/logout.html"
    redirect_field_name = 'redirect_to'
    success_url = 'website:index'
    
    def get(self, request):
        
        print("****************************************************")
        print("LOGOUT VIEW")
        print("****************************************************")
        if request.user.is_authenticated:
            print("----------------------------------------------------")
            print("User IS authenticated...")
            logout(request)
            return redirect(self.success_url)
    

class DashBoardView(LoginRequiredMixin, ListView):
    template_name = "website/account/dashboard.html"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    """ 
    def get(self,request):
        print("****************************************************")
        print("DASHBOARD VIEW")
        print("****************************************************")
        if not request.user.is_authenticated:
            print("----------------------------------------------------")
            print("User NOT is authenticated...")
        else:
            print("----------------------------------------------------")
            print("User IS authenticated...")
        
        
        return render(request, self.template_name)
    """
    
    def get(self,request):
        print("****************************************************")
        print("DASHBOARD VIEW")
        print("****************************************************")
        if not request.user.is_authenticated:
            print("----------------------------------------------------")
            print("User NOT is authenticated...")
            return render(request, self.login_url)
        else:
            print("----------------------------------------------------")
            print("User IS authenticated...")
            return render(request, self.template_name)
        
        return render(request, self.login_url)
        
    
    
class CustomLoginView(LoginView):
    template_name = "website/account/login.html"
    authentication_form = LoginUsuarioForm
    model = Usuario
    success_url = 'website/account/dashboard.html'
    
    
   
    
    def post(self, request):
        print("****************************************************")
        print("POST LOGIN VIEW")
        print("****************************************************")
        username = request.POST['username']
        print("----------------------------------------------------")
        print(username)
        password = request.POST['password']
        print("----------------------------------------------------")
        print(password)
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("-------------------------------------------------")
            print("User Already Authenticated...")
            print("-------------------------------------------------")
            print("User Login...")
            login(request, user)
            return redirect("/account/dashboard")
    
        else:
            print("-------------------------------------------------")
            print("User NOT Already Authenticated...")
            user = Usuario.objetos.filter(username=username,password=password).first()
            if user is not None:        
                print("-------------------------------------------------")
                print("User Found...")
                print("-------------------------------------------------")
                print("ID USER =" + str(user.pk))   
                login(request, user)
                return redirect("/account/dashboard")
                #return render(request, reverse("website:login") )
                #return HttpResponseRedirect(reverse(self.success_url))
                
                #return redirect("/account/dashboard")
            
            else:            
                print("User Not Found...")
                return render(request, self.template_name, {'form': self.authentication_form})
                    
        return render(request, self.template_name, {'form': self.authentication_form})
    # No backend authenticated the credentials
        #email = form.cleaned_data['email']
        #password = form.cleaned_data['password']
        #username = form.cleaned_data['username']
        

        
        
        """user = authenticate(self.request, username=username, password=password)
        if user is not None:            #return redirect('/foos')
            login(self.request,user)
        else:
            return render(self.request, self.template_name, { 'form': form })
            """
        #else:

    #def form_valid(self, form):
        
        
        
        
class FirstTimeView(CreateView):
    template_name = "website/account/first_time.html"
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("website:lista_foos")
    
    def post(self, request):
        print("****************************************************")
        print("FIRST TIME  VIEW")
        print("****************************************************")
        username = request.POST['username']
        print("----------------------------------------------------")
        print("USERNAME =" +str(username))
        password = request.POST['password']
        print("----------------------------------------------------")
        print("PASSWORD = " + str(password))
        print("-------------------------------------------------")
        email = request.POST['email']
        print("EMAIL = " + str(email))
        print("-------------------------------------------------")
        categoria = request.POST['categoria']
        print("CATEGORIA = " + str(categoria))
        print("-------------------------------------------------")
        nome = request.POST['nome']
        print("NOME = " + str(nome))
            
        """
        form = InsereUsuarioForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            print(user.pk)
            return redirect('/account/login')
        """
        
        usuario = Usuario.objetos.filter(username=username, matricula=username, email=email,password=password, categoria=categoria).first()
            
                        
        if usuario is  None:
            print("-------------------------------------------------")
            print("USER DOESN'T EXISTS!")
                
                
            
            
            #https://stackoverflow.com/questions/20361235/django-set-user-permissions-when-user-is-automatically-created#answer-36018316
           
            usuario = None
            if categoria == "professor":
                usuario = Usuario.objetos.create(username=username, matricula=username, email=email,password=password, categoria=categoria, nome=nome, first_name=nome )
                permission = Permission.objects.get(codename='view_usuario')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_usuario')
                usuario.user_permissions.add(permission)
                
                permission = Permission.objects.get(codename='view_reserva')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='add_reserva')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_reserva')
                usuario.user_permissions.add(permission)
                
                pass                                
            elif categoria == "laboratorista":
                usuario = Usuario.objetos.create(username=username, matricula=username, email=email,password=password, categoria=categoria,nome = nome, first_name=nome,is_staff =1 )
                permission = Permission.objects.get(codename='view_usuario')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_usuario')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='add_usuario')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='delete_usuario')
                usuario.user_permissions.add(permission)
                
                
                permission = Permission.objects.get(codename='view_tipolaboratorio')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_tipolaboratorio')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='add_tipolaboratorio')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='delete_tipolaboratorio')
                usuario.user_permissions.add(permission)
                
                
                permission = Permission.objects.get(codename='view_reserva')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_reserva')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='add_reserva')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='delete_reserva')
                usuario.user_permissions.add(permission)
                
                permission = Permission.objects.get(codename='view_recurso')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_recurso')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='add_recurso')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='delete_recurso')
                usuario.user_permissions.add(permission)
                
                permission = Permission.objects.get(codename='view_curso')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='change_curso')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='add_curso')
                usuario.user_permissions.add(permission)
                permission = Permission.objects.get(codename='delete_curso')
                usuario.user_permissions.add(permission)

                
            print("-------------------------------------------------")
            print("ID USER CREATED =" + str(usuario.pk))   
            return redirect("/account/login")
        else:
            print("USER ALDEADY EXISTS! ")
            return render(self.request, self.template_name, { 'form': self.form_class  })  
           
            #User.objects.create(email=email,password=password)      
        
        return render(self.request, self.template_name, { 'form': self.form_class  })

class UsuarioListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "authweb.view_usuario"
    template_name = "website/usuario/lista.html"
    model = Usuario
    #/context_object_name = "usuarios"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(UsuarioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['usuarios'] = Usuario.objetos.filter(is_superuser=False)
        
        # And so on for more models
        return context
    
class UsuarioListViewUsuario(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    permission_required = "authweb.view_usuario"
    template_name = "website/usuario/lista2.html"
    model = Usuario
    #context_object_name = "usuarios"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    def get_context_data(self, **kwargs):
        context = super(UsuarioListViewUsuario, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['usuarios'] = Usuario.objetos.filter(id=self.request.user.id)
        
        # And so on for more models
        return context

class UsuarioCreateView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_usuario"
    template_name = "website/usuario/cria.html"
    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("website:lista_usuarios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def form_valid(self, form):
        print("****************************************************")
        #print(form.cleaned_data['origem'])
        print("****************************************************")
        form.save()
        print("****************************************************")
        return super().form_valid(form)

class UsuarioUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "authweb.change_usuario"
    template_name = "website/usuario/atualiza.html"
    model = Usuario
    fields = '__all__'
    context_object_name = 'usuario'
    success_url = reverse_lazy("website:lista_usuarios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class UsuarioUpdateViewUsuario(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "authweb.change_usuario"
    template_name = "website/usuario/atualiza2.html"
    model = Usuario
    fields = '__all__'
    context_object_name = 'usuario'
    success_url = reverse_lazy("website:lista_usuario")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class UsuarioDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_usuario"
    template_name = "website/usuario/exclui.html"
    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy("website:lista_usuarios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'    
#*** FOO ***    
class FooListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_foo"
    template_name = "website/foo/lista.html"
    model = Foo
    context_object_name = "foos"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class FooCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_foo"
    template_name = "website/foo/cria.html"
    model = Foo
    form_class = InsereFooForm
    success_url = reverse_lazy("website:lista_foos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class FooUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_foo"
    template_name = "website/foo/atualiza.html"
    model = Foo
    fields = '__all__'
    context_object_name = 'foo'
    success_url = reverse_lazy("website:lista_foos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    

class FooDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_foo"
    template_name = "website/foo/exclui.html"
    model = Foo
    context_object_name = 'foo'
    success_url = reverse_lazy("website:lista_foos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
class CursoListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_curso"
    template_name = "website/curso/lista.html"
    model = Curso
    context_object_name = "cursos"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class CursoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_curso"
    template_name = "website/curso/cria.html"
    model = Curso
    form_class = InsereCursoForm
    success_url = reverse_lazy("website:lista_cursos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class CursoUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_curso"
    template_name = "website/curso/atualiza.html"
    model = Curso
    fields = '__all__'
    context_object_name = 'curso'
    success_url = reverse_lazy("website:lista_cursos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    

class CursoDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_curso"
    template_name = "website/curso/exclui.html"
    model = Curso
    context_object_name = 'curso'
    success_url = reverse_lazy("website:lista_cursos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
class TipoLaboratorioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_tipolaboratorio"
    template_name = "website/tipo_laboratorio/lista.html"
    model = TipoLaboratorio
    context_object_name = "tipo_laboratorios"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class TipoLaboratorioCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_tipolaboratorio"
    template_name = "website/tipo_laboratorio/cria.html"
    model = TipoLaboratorio
    form_class = InsereTipoLaboratorioForm
    success_url = reverse_lazy("website:lista_tipo_laboratorios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class TipoLaboratorioUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_tipolaboratorio"
    template_name = "website/tipo_laboratorio/atualiza.html"
    model = TipoLaboratorio
    fields = '__all__'
    context_object_name = 'tipo_laboratorio'
    success_url = reverse_lazy("website:lista_tipo_laboratorios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    

class TipoLaboratorioDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_tipolaboratorio"
    template_name = "website/tipo_laboratorio/exclui.html"
    model = TipoLaboratorio
    context_object_name = 'tipo_laboratorio'
    success_url = reverse_lazy("website:lista_tipo_laboratorios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
#*** FOO ***    
class SituacaoListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_situacao"
    template_name = "website/situacao/lista.html"
    model = Situacao
    context_object_name = "situacaos"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class SituacaoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_situacao"
    template_name = "website/situacao/cria.html"
    model = Situacao
    form_class = InsereSituacaoForm
    success_url = reverse_lazy("website:lista_situacaos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class SituacaoUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_situacao"
    template_name = "website/situacao/atualiza.html"
    model = Situacao
    fields = '__all__'
    context_object_name = 'situacao'
    success_url = reverse_lazy("website:lista_situacaos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    

class SituacaoDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_situacao"
    template_name = "website/situacao/exclui.html"
    model = Situacao
    context_object_name = 'situacao'
    success_url = reverse_lazy("website:lista_situacaos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class LaboratorioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_recurso"
    template_name = "website/laboratorio/lista.html"
    model = Recurso
    #context_object_name = "recursos"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(LaboratorioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="laboratorio")
        
        # And so on for more models
        return context


class LaboratorioCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_recurso"
    template_name = "website/laboratorio/cria.html"
    model = Recurso
    form_class = InsereLaboratorioForm
    success_url = reverse_lazy("website:lista_laboratorios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class LaboratorioUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_recurso"
    template_name = "website/laboratorio/atualiza.html"
    model = Recurso
    fields = '__all__'
    context_object_name = 'recurso'
    success_url = reverse_lazy("website:lista_laboratorios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    
    

class LaboratorioDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_recurso"
    template_name = "website/laboratorio/exclui.html"
    model = Recurso
    context_object_name = 'recurso'
    success_url = reverse_lazy("website:lista_laboratorios")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

#Projetor
class ProjetorListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_recurso"
    template_name = "website/projetor/lista.html"
    model = Recurso
    context_object_name = "projetors"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ProjetorListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['projetors'] = Recurso.objetos.filter(tipo_recurso="projetor")
        
        # And so on for more models
        return context

class ProjetorCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_recurso"
    template_name = "website/projetor/cria.html"
    model = Recurso
    form_class = InsereProjetorForm
    success_url = reverse_lazy("website:lista_projetors")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM PROJETOR VIEW")
        print("****************************************************")
        numero = form.cleaned_data['numero']
        print("----------------------------------------------------")
        print(str(numero))
        print("----------------------------------------------------")
        descricao = form.cleaned_data['descricao']
        print("----------------------------------------------------")
        print(str(descricao))
        Recurso.objetos.create(numero=numero, descricao = descricao, tipo_recurso = "projetor")
        return HttpResponseRedirect(reverse('website:lista_projetors'))
    
class ProjetorUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_recurso"
    template_name = "website/projetor/atualiza.html"
    model = Recurso
    #fields = '__all__'
    context_object_name = 'recurso'
    form_class = InsereProjetorForm
    success_url = reverse_lazy("website:lista_projetors")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    

class ProjetorDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_recurso"
    template_name = "website/projetor/exclui.html"
    model = Recurso
    context_object_name = 'recurso'
    success_url = reverse_lazy("website:lista_projetors")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'

class ReservaLaboratorioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_reserva"
    template_name = "website/reserva_laboratorio/lista.html"
    model = Reserva
    #context_object_name = "reservas"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaLaboratorioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="laboratorio", data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context

class ReservaLaboratorioUsuarioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_reserva"
    template_name = "website/reserva_laboratorio/lista_usuario.html"
    model = Reserva
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaLaboratorioUsuarioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['reservas'] = Reserva.objetos.filter(id_usuario=self.request.user.id, tipo_recurso="laboratorio", situacao =2, data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
class ReservaNaoConfirmadaLaboratorioUsuarioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_reserva"
    template_name = "website/reserva_laboratorio/lista_nao_confirmada_usuario.html"
    model = Reserva
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaNaoConfirmadaLaboratorioUsuarioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        time_threshold = datetime.now() + timedelta(hours=30)
        context['reservas'] = Reserva.objetos.filter(id_usuario=self.request.user.id,confirmacao=0,data_hora_saida__gte = time_threshold,  tipo_recurso="laboratorio", situacao =2)
        
        # And so on for more models
        return context

class ReservaLaboratorioCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_reserva"
    template_name = "website/reserva_laboratorio/cria2.html"
    model = Reserva
    form_class = InsereReservaLaboratorioForm
    
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def get_context_data(self, **kwargs):
        context = super(ReservaLaboratorioCreateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="laboratorio")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="laboratorio", data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        justificativa = form.cleaned_data['justificativa']
        print("----------------------------------------------------")
        print(str(justificativa))
        disciplina = form.cleaned_data['disciplina']
        print("----------------------------------------------------")
        print(str(disciplina))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2, tipo_recurso="laboratorio"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(usuario.id))
                Reserva.objetos.create(id_usuario=usuario,id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, justificativa=justificativa, tipo_recurso="laboratorio", confirmacao=False, disciplina=disciplina, nome_professor= usuario.nome )
                messages.success(self.request, 'A reserva criada com sucesso')
            
        
        
        #return redirect('reserva_laboratorio/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
    
class ReservaLaboratorioUsuariosCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_reserva"
    template_name = "website/reserva_laboratorio/cria3.html"
    model = Reserva
    form_class = InsereReservaLaboratorioUsuariosForm
    
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def get_context_data(self, **kwargs):
        context = super(ReservaLaboratorioUsuariosCreateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="laboratorio")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="laboratorio", data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_usuario = form.cleaned_data['id_usuario']
        print("----------------------------------------------------")
        print(str(id_usuario))
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        justificativa = form.cleaned_data['justificativa']
        print("----------------------------------------------------")
        print(str(justificativa))
        disciplina = form.cleaned_data['disciplina']
        print("----------------------------------------------------")
        print(str(disciplina))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2, tipo_recurso="laboratorio"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            #usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(id_usuario.id))
                Reserva.objetos.create(id_usuario=id_usuario,id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, justificativa=justificativa, tipo_recurso="laboratorio", confirmacao=False, disciplina=disciplina, nome_professor= id_usuario.nome )
                messages.success(self.request, 'Reserava do Laboratorio Realizada com Sucesso')
            
        
        
        #return redirect('reserva_laboratorio/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio_usuarios'))
   
class ReservaLaboratorioConfirmaUpdateView(PermissionRequiredMixin, LoginRequiredMixin,DeleteView):
    permission_required = "authweb.change_reserva"
    template_name = "website/reserva_laboratorio/confirma.html"
    model = Reserva
    #fields = '__all__'
    context_object_name = 'reserva'
    success_url = reverse_lazy("website:lista_reserva_laboratorios_nao_confirmada_usuario")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def delete(self, request, *args, **kwargs):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO CONFIRMA VIEW")
        print("****************************************************")
        print("----------------------------------------------------")        
        id = self.kwargs['pk']
        print("ID RESERVA = " + str(id))
        
        print("----------------------------------------------------")
        print("Confirmando reserva")
        Reserva.objetos.filter(id=id).update(confirmacao=True)
        messages.success(self.request, 'A reserva confirmada com sucesso!')
        return HttpResponseRedirect(reverse('website:lista_reserva_laboratorios_nao_confirmada_usuario'))
   
    
    
class ReservaLaboratorioUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_reserva"
    template_name = "website/reserva_laboratorio/atualiza.html"
    model = Reserva
    context_object_name = 'reserva'
    form_class = InsereReservaLaboratorioForm    
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def get_context_data(self, **kwargs):
        context = super(ReservaLaboratorioUpdateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="laboratorio")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="laboratorio",data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        justificativa = form.cleaned_data['justificativa']
        print("----------------------------------------------------")
        print(str(justificativa))
        disciplina = form.cleaned_data['disciplina']
        print("----------------------------------------------------")
        print(str(disciplina))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2, tipo_recurso="laboratorio"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(usuario.id))
                Reserva.objetos.filter(id_usuario=usuario).update(id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, justificativa=justificativa, tipo_recurso="laboratorio", confirmacao=False, disciplina=disciplina, nome_professor= usuario.nome )
                messages.success(self.request, 'A reserva autualizada com sucesso!')
            
        
        
        #return redirect('reserva_laboratorio/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:atualiza_reserva_laboratorio'))
    
    
    

class ReservaLaboratorioDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_reserva"
    template_name = "website/reserva_laboratorio/exclui.html"
    model = Reserva
    context_object_name = 'reserva'
    success_url = reverse_lazy("website:lista_foos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
class ReservaLaboratorioUsuariosUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_reserva"
    template_name = "website/reserva_laboratorio/atualiza2.html"
    model = Reserva
    context_object_name = 'reserva'
    form_class = InsereReservaLaboratorioUsuariosForm    
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def get_context_data(self, **kwargs):
        context = super(ReservaLaboratorioUsuariosUpdateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="laboratorio")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="laboratorio", data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        justificativa = form.cleaned_data['justificativa']
        print("----------------------------------------------------")
        print(str(justificativa))
        disciplina = form.cleaned_data['disciplina']
        print("----------------------------------------------------")
        print(str(disciplina))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_laboratorio'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2, tipo_recurso="laboratorio"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(usuario.id))
                Reserva.objetos.filter(id_usuario=usuario).update(id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, justificativa=justificativa, tipo_recurso="laboratorio", confirmacao=False, disciplina=disciplina, nome_professor= usuario.nome )
                messages.success(self.request, 'A reserva autualizada com sucesso!')
            
        
        
        #return redirect('reserva_laboratorio/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:atualiza_reserva_laboratorio_usuarios'))
class ReservaProjetorListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_reserva"
    template_name = "website/reserva_projetor/lista.html"
    model = Reserva
    #context_object_name = "reservas"
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaProjetorListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="projetor",data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context

class ReservaProjetorUsuarioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_reserva"
    template_name = "website/reserva_projetor/lista_usuario.html"
    model = Reserva
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaProjetorUsuarioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['reservas'] = Reserva.objetos.filter(id_usuario=self.request.user.id, tipo_recurso="projetor", data_hora_saida__gte = datetime.now(), situacao =2)
        
        # And so on for more models
        return context
    
class ReservaNaoConfirmadaProjetorUsuarioListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    permission_required = "authweb.view_reserva"
    template_name = "website/reserva_projetor/lista_nao_confirmada_usuario.html"
    model = Reserva
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaNaoConfirmadaProjetorUsuarioListView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        time_threshold = datetime.now() + timedelta(hours=30)
        context['reservas'] = Reserva.objetos.filter(id_usuario=self.request.user.id,confirmacao=0,data_hora_saida__gte = time_threshold, tipo_recurso="projetor", situacao =2)
        
        # And so on for more models
        return context

class ReservaProjetorCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_reserva"
    template_name = "website/reserva_projetor/cria2.html"
    model = Reserva
    form_class = InsereReservaProjetorForm
    
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def get_context_data(self, **kwargs):
        context = super(ReservaProjetorCreateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="projetor")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="projetor")
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        curso = form.cleaned_data['curso']
        print("----------------------------------------------------")
        print(str(curso))
        primeira_aula = form.cleaned_data['primeira_aula']
        print("----------------------------------------------------")
        print(str(primeira_aula))
        segunda_aula = form.cleaned_data['segunda_aula']
        print("----------------------------------------------------")
        print(str(segunda_aula))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2,  tipo_recurso="projetor"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(usuario.id))
                Reserva.objetos.create(id_usuario=usuario,id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, curso = curso, tipo_recurso="projetor", confirmacao=False, primeira_aula = primeira_aula, segunda_aula = segunda_aula)
                messages.success(self.request, 'Reserava do Projetor Realizada com Sucesso')
            
        
        
        #return redirect('reserva_projetor/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
    
    
class ReservaProjetorUsuariosCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "authweb.add_reserva"
    template_name = "website/reserva_projetor/cria3.html"
    model = Reserva
    form_class = InsereReservaProjetorUsuariosForm
    
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    
    def get_context_data(self, **kwargs):
        context = super(ReservaProjetorUsuariosCreateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="projetor")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="projetor",data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_usuario = form.cleaned_data['id_usuario']
        print("----------------------------------------------------")
        print(str(id_usuario))
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        curso = form.cleaned_data['curso']
        print("----------------------------------------------------")
        print(str(curso))
        primeira_aula = form.cleaned_data['primeira_aula']
        print("----------------------------------------------------")
        print(str(primeira_aula))
        segunda_aula = form.cleaned_data['segunda_aula']
        print("----------------------------------------------------")
        print(str(segunda_aula))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2,  tipo_recurso="projetor"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            #usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(id_usuario))
                Reserva.objetos.create(id_usuario=id_usuario,id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, curso = curso, tipo_recurso="projetor", confirmacao=False, primeira_aula = primeira_aula, segunda_aula = segunda_aula)
                messages.success(self.request, 'Reserva do Projetor Realizada com Sucesso')
            
        
        
        #return redirect('reserva_projetor/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor_usuarios'))

    
class ReservaProjetorConfirmaUpdateView(PermissionRequiredMixin, LoginRequiredMixin,DeleteView):
    permission_required = "authweb.change_reserva"
    template_name = "website/reserva_projetor/confirma.html"
    model = Reserva
    #fields = '__all__'
    context_object_name = 'reserva'
    success_url = reverse_lazy("website:lista_reserva_projetors_nao_confirmada_usuario")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def delete(self, request, *args, **kwargs):
        print("****************************************************")
        print("FORM RESERVA PROJETOR CONFIRMA VIEW")
        print("****************************************************")
        print("----------------------------------------------------")        
        id = self.kwargs['pk']
        print("ID RESERVA = " + str(id))
        
        print("----------------------------------------------------")
        print("Confirmando reserva")
        Reserva.objetos.filter(id=id).update(confirmacao=True)
        messages.success(self.request, 'A Reserva Confirmada com Sucesso!')
        return HttpResponseRedirect(reverse('website:lista_reserva_projetors_nao_confirmada_usuario'))
   
    
   
    
    
class ReservaProjetorUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_reserva"
    template_name = "website/reserva_projetor/atualiza.html"
    model = Reserva
    form_class = InsereReservaProjetorForm
    context_object_name = 'reserva'
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaProjetorCreateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="projetor")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="projetor", data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        curso = form.cleaned_data['curso']
        print("----------------------------------------------------")
        print(str(curso))
        primeira_aula = form.cleaned_data['primeira_aula']
        print("----------------------------------------------------")
        print(str(primeira_aula))
        segunda_aula = form.cleaned_data['segunda_aula']
        print("----------------------------------------------------")
        print(str(segunda_aula))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2,  tipo_recurso="projetor"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(usuario.id))
                Reserva.objetos.filter(id_usuario=usuario).update(id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, curso = curso, tipo_recurso="projetor", confirmacao=False, primeira_aula = primeira_aula, segunda_aula = segunda_aula)
                messages.success(self.request, 'Reserava do Projetor Atualizada com Sucesso!!!')
            
        
        
        #return redirect('reserva_projetor/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:atualiza_reserva_projetor'))

    
class ReservaProjetorUsuariosUpdateView(PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "authweb.change_reserva"
    template_name = "website/reserva_projetor/atualiza2.html"
    model = Reserva
    form_class = InsereReservaProjetorUsuariosForm
    context_object_name = 'reserva'
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        context = super(ReservaProjetorUsuariosUpdateView, self).get_context_data(**kwargs)
        #context['recursos'] = Recurso.objects.all()
        context['recursos'] = Recurso.objetos.filter(tipo_recurso="projetor")
        context['reservas'] = Reserva.objetos.filter(tipo_recurso="projetor",data_hora_saida__gte = datetime.now())
        
        # And so on for more models
        return context
    
    def form_valid(self, form):
        print("****************************************************")
        print("FORM RESERVA LABORATORIO VIEW")
        print("****************************************************")
        id_recurso = form.cleaned_data['id_recurso']
        print("----------------------------------------------------")
        print(str(id_recurso))
        print("----------------------------------------------------")
        data_uso = form.cleaned_data['data_uso']
        print("----------------------------------------------------")
        print(str(data_uso))
        time_uso = form.cleaned_data['time_uso']
        print("----------------------------------------------------")
        print(str(time_uso))
        data_liberacao = form.cleaned_data['data_liberacao']
        print("----------------------------------------------------")
        print(str(data_liberacao))
        time_liberacao = form.cleaned_data['time_liberacao']
        print("----------------------------------------------------")
        print(str(time_liberacao))
        curso = form.cleaned_data['curso']
        print("----------------------------------------------------")
        print(str(curso))
        primeira_aula = form.cleaned_data['primeira_aula']
        print("----------------------------------------------------")
        print(str(primeira_aula))
        segunda_aula = form.cleaned_data['segunda_aula']
        print("----------------------------------------------------")
        print(str(segunda_aula))
        
        
        dow1 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 1);
        dow2 = datetime(data_uso.year,data_uso.month, data_uso.day, 12, 59);
        dow3 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 1);
        
        
        dow4 = datetime(data_uso.year,data_uso.month, data_uso.day, 17, 59);
        dow5 = datetime(data_uso.year,data_uso.month, data_uso.day, 22, 1);
        dow6 = datetime(data_uso.year,data_uso.month, data_uso.day+1, 6, 59);
        
        
        dt1 = datetime(data_uso.year,data_uso.month, data_uso.day, time_uso.hour, time_uso.minute)
        print("----------------------------------------------------")
        print("DATA INICIAL = " + str(dt1))
        dt2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, time_liberacao.hour, time_liberacao.minute )
        print("----------------------------------------------------")
        print("DATA FINAL = " + str(dt2))
        if  dt1 < datetime.now() or dt2 < datetime.now():
            print("----------------------------------------------------")
            print("data menor que o tempo atual")
            messages.error(self.request, "data menor que o tempo atual")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        if dt1 >=  dt2 :
           print("----------------------------------------------------")
           print("data liberaraco e menor ou igual que a data de uso")
           messages.error(self.request, "data liberaraco e menor ou igual que a data de uso")
           return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
           
        if ( (dow1 <= dt1 and dt1 <= dow2 ) or (dow3 <= dt1 and dt1 <= dow4 ) or (dow5 <= dt1 and dt1 <= dow6 )):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data de inicio")
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
        
        dow1 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 1);
        dow2 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 12, 59);
        print("----------------------------------------------------")
        print("[" + str(dow1) + " | " +  str(dt2) + " | " + str(dow2) + "]" )
        dow3 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 1);
        dow4 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 17, 59);
        print("----------------------------------------------------")
        print("[" + str(dow3) + " | " +  str(dt2) + " | " + str(dow4) + "]" )
        dow5 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day, 22, 1);
        dow6 = datetime(data_liberacao.year,data_liberacao.month, data_liberacao.day+1, 6, 59);
        print("----------------------------------------------------")
        print("[" + str(dow5) + " | " +  str(dt2) + " | " + str(dow6) + "]" )
        
        
        if ( (dow1 <= dt2 and dt2 <= dow2 ) or 
             (dow3 <= dt2 and dt2 <= dow4 ) or
             (dow5 <= dt2 and dt2 <= dow6 )
             ):
            print("----------------------------------------------------")
            print("Fora de funcionamento para data final")
            messages.error(self.request, 'Fora de funcionamento para data final')
            return HttpResponseRedirect(reverse('website:cadastra_reserva_projetor'))
            
        #reserva = Reserva.objetos.filter(Q(id_recurso=id_recurso) & (Q(data_hora_saida__lte = dt1) | Q(data_hora_saida__lte = dt1))).first()
        reserva = Reserva.objetos.filter(id_recurso=id_recurso, data_hora_saida__lte = dt1 , data_hora_saida__gte = dt1, data_hora_chegada__lte = dt2 , data_hora_chegada__gte = dt2,  tipo_recurso="projetor"  ).first()
        
        if (reserva != None):
            print("A reserva nao pode ser realizada, ja existe uma reserava para esse recurso")
            print("----------------------------------------------------")
            print("RESERVA_ID =" + str(reserva.id))
            messages.error(self.request, 'A reserva nao pode ser realizada, ja existe uma reserava para esse recurso')
        else:
            print("----------------------------------------------------")
            print("Cadastrando Reserva...")
            situacao = Situacao.objetos.filter(nome="Reservado").first()
            usuario = Usuario.objetos.filter(matricula=self.request.user.username).first()
            
            if situacao != None:
                print("----------------------------------------------------")
                print("SITUACAO =" + str(situacao.nome))
                print("----------------------------------------------------")
                print("USURIO =" + str(usuario.id))
                Reserva.objetos.filter(id_usuario=usuario).update(id_recurso=id_recurso,situacao=situacao, data_hora_saida=dt1, data_hora_chegada=dt2, curso = curso, tipo_recurso="projetor", confirmacao=False, primeira_aula = primeira_aula, segunda_aula = segunda_aula)
                messages.success(self.request, 'Reserava do Projetor Atualizada com Sucesso!!!')
            
        
        
        #return redirect('reserva_projetor/cadastrar')
        #return render(self.request, self.template_name, { 'form': form })
        return HttpResponseRedirect(reverse('website:atualiza_reserva_projetor_usuarios'))

    

class ReservaProjetorDeleteView(PermissionRequiredMixin,LoginRequiredMixin, DeleteView):
    permission_required = "authweb.delete_reserva"
    template_name = "website/reserva_projetor/exclui.html"
    model = Reserva
    context_object_name = 'reserva'
    success_url = reverse_lazy("website:lista_foos")
    login_url = 'website:login'
    redirect_field_name = 'redirect_to'
    