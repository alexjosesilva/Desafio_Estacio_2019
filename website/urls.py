from website.views import IndexTemplateView, FooCreateView, FooListView,\
    FooUpdateView, FooDeleteView, CustomLoginView, FirstTimeView, DashBoardView,\
    CustomLogoutView, AgendaTemplateView, AgendaRecursoTemplateView,\
    ReservaLaboratorioUsuarioListView,\
    ReservaNaoConfirmadaLaboratorioUsuarioListView, \
    ReservaProjetorUsuarioListView,\
    ReservaNaoConfirmadaProjetorUsuarioListView,\
    ReservaLaboratorioUsuariosCreateView, UsuarioListViewUsuario,\
    UsuarioUpdateViewUsuario, ReservaProjetorUsuariosCreateView,\
    ReservaLaboratorioUsuariosUpdateView, ReservaProjetorUsuariosUpdateView,\
    ReservaLaboratorioConfirmaUpdateView, ReservaProjetorConfirmaUpdateView

from website.views import UsuarioListView, UsuarioUpdateView, UsuarioCreateView, \
UsuarioDeleteView

from website.views import TipoLaboratorioCreateView, TipoLaboratorioListView,\
    TipoLaboratorioUpdateView, TipoLaboratorioDeleteView
    
    
from website.views import SituacaoCreateView, SituacaoListView,\
    SituacaoUpdateView, SituacaoDeleteView 
    
from website.views import LaboratorioCreateView, LaboratorioListView,\
    LaboratorioUpdateView, LaboratorioDeleteView
    
from website.views import ProjetorCreateView, ProjetorListView,\
    ProjetorUpdateView, ProjetorDeleteView  
    
    
from website.views import ReservaLaboratorioCreateView, ReservaLaboratorioListView,\
    ReservaLaboratorioUpdateView, ReservaLaboratorioDeleteView
    
from website.views import ReservaProjetorCreateView, ReservaProjetorListView,\
    ReservaProjetorUpdateView, ReservaProjetorDeleteView  
    
from website.views import CursoCreateView, CursoListView,\
    CursoUpdateView, CursoDeleteView     
    

    

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),
    path('index/', IndexTemplateView.as_view(), name="index"),
    path('agenda/', AgendaTemplateView.as_view(), name="agenda"),
    path('agenda_recurso/', AgendaRecursoTemplateView.as_view(), name="agenda_recurso"),
    
     # GET /funcionario/cadastrar
    path('usuario/cadastrar', UsuarioCreateView.as_view(), name="cadastra_usuario"),

    # GET /usuarios
    path('usuarios/', UsuarioListView.as_view(), name="lista_usuarios"),
    path('usuario/', UsuarioListViewUsuario.as_view(), name="lista_usuario"),

    # GET/POST /usuario/{pk}
    path('usuarios/<pk>', UsuarioUpdateView.as_view(), name="atualiza_usuarios"),
    
    path('usuario/<pk>', UsuarioUpdateViewUsuario.as_view(), name="atualiza_usuario"),
    
    # GET/POST /usuarios/excluir/{pk}
    path('usuario/excluir/<pk>', UsuarioDeleteView.as_view(), name="deleta_usuario"),
    
    
    #  << CLIENTE >>
    # GET /funcionario/cadastrar
    path('foo/cadastrar', FooCreateView.as_view(), name="cadastra_foo"),

    # GET /foos
    path('foos/', FooListView.as_view(), name="lista_foos"),

    # GET/POST /foo/{pk}
    path('foo/<pk>', FooUpdateView.as_view(), name="atualiza_foo"),

    # GET/POST /foos/excluir/{pk}
    path('foo/excluir/<pk>', FooDeleteView.as_view(), name="deleta_foo"),
    
    #  << CLIENTE >>
    # GET /funcionario/cadastrar
    path('curso/cadastrar', CursoCreateView.as_view(), name="cadastra_curso"),

    # GET /cursos
    path('cursos/', CursoListView.as_view(), name="lista_cursos"),

    # GET/POST /curso/{pk}
    path('curso/<pk>', CursoUpdateView.as_view(), name="atualiza_curso"),

    # GET/POST /cursos/excluir/{pk}
    path('curso/excluir/<pk>', CursoDeleteView.as_view(), name="deleta_curso"),

    
    path('account/login/', CustomLoginView.as_view(), name="login"),
    
    path('account/logout/', CustomLogoutView.as_view(), name="logout"),
    
    path('account/first_time/', FirstTimeView.as_view(), name="first_time"),
    
    path('account/dashboard', DashBoardView.as_view(), name="dashboard"),
    
    
    path('tipo_laboratorio/cadastrar', TipoLaboratorioCreateView.as_view(), name="cadastra_tipo_laboratorio"),

    # GET /tipo_laboratorios
    path('tipo_laboratorios/', TipoLaboratorioListView.as_view(), name="lista_tipo_laboratorios"),

    # GET/POST /tipo_laboratorio/{pk}
    path('tipo_laboratorio/<pk>', TipoLaboratorioUpdateView.as_view(), name="atualiza_tipo_laboratorio"),

    # GET/POST /tipo_laboratorios/excluir/{pk}
    path('tipo_laboratorio/excluir/<pk>', TipoLaboratorioDeleteView.as_view(), name="deleta_tipo_laboratorio"),

     #  << CLIENTE >>
    # GET /funcionario/cadastrar
    path('situacao/cadastrar', SituacaoCreateView.as_view(), name="cadastra_situacao"),

    # GET /situacaos
    path('situacaos/', SituacaoListView.as_view(), name="lista_situacaos"),

    # GET/POST /situacao/{pk}
    path('situacao/<pk>', SituacaoUpdateView.as_view(), name="atualiza_situacao"),

    # GET/POST /situacaos/excluir/{pk}
    path('situacao/excluir/<pk>', SituacaoDeleteView.as_view(), name="deleta_situacao"),
    
    path('laboratorio/cadastrar', LaboratorioCreateView.as_view(), name="cadastra_laboratorio"),

    # GET /laboratorios
    path('laboratorios/', LaboratorioListView.as_view(), name="lista_laboratorios"),

    # GET/POST /laboratorio/{pk}
    path('laboratorio/<pk>', LaboratorioUpdateView.as_view(), name="atualiza_laboratorio"),

    # GET/POST /laboratorios/excluir/{pk}
    path('laboratorio/excluir/<pk>',LaboratorioDeleteView.as_view(), name="deleta_laboratorio"),
    
    path('projetor/cadastrar', ProjetorCreateView.as_view(), name="cadastra_projetor"),

    # GET /projetors
    path('projetors/', ProjetorListView.as_view(), name="lista_projetors"),

    # GET/POST /projetor/{pk}
    path('projetor/<pk>', ProjetorUpdateView.as_view(), name="atualiza_projetor"),

    # GET/POST /projetors/excluir/{pk}
    path('projetor/excluir/<pk>',ProjetorDeleteView.as_view(), name="deleta_projetor"),
    
    path('reserva_laboratorio/cadastrar', ReservaLaboratorioCreateView.as_view(), name="cadastra_reserva_laboratorio"),   
    path('reserva_laboratorio/<pk>', ReservaLaboratorioUpdateView.as_view(), name="atualiza_reserva_laboratorio"),
    
    path('reserva_laboratorio_confirma/<pk>', ReservaLaboratorioConfirmaUpdateView.as_view(), name="atualiza_reserva_laboratorio_confirma"),
    
    
    path('reserva_laboratorio_usuarios/cadastrar', ReservaLaboratorioUsuariosCreateView.as_view(), name="cadastra_reserva_laboratorio_usuarios"),    
    path('reserva_laboratorio_usuarios/<pk>', ReservaLaboratorioUsuariosUpdateView.as_view(), name="atualiza_reserva_laboratorio_usuarios"),

    # GET /reserva_laboratorios
    path('reserva_laboratorios/', ReservaLaboratorioListView.as_view(), name="lista_reserva_laboratorios"),
    
    path('reserva_laboratorios_usuario/', ReservaLaboratorioUsuarioListView.as_view(), name="lista_reserva_laboratorios_usuario"),
    
    path('reserva_laboratorios_nao_confirmada_usuario/', ReservaNaoConfirmadaLaboratorioUsuarioListView.as_view(), name="lista_reserva_laboratorios_nao_confirmada_usuario"),
    
    

   

    # GET/POST /reserva_laboratorios/excluir/{pk}
    path('reserva_laboratorio/excluir/<pk>', ReservaLaboratorioDeleteView.as_view(), name="deleta_reserva_laboratorio"),
    
    
    path('reserva_projetor/cadastrar', ReservaProjetorCreateView.as_view(), name="cadastra_reserva_projetor"),   
    # POST /reserva_projetor/{pk}
    path('reserva_projetor/<pk>', ReservaProjetorUpdateView.as_view(), name="atualiza_reserva_projetor"),
    
    path('reserva_projetor_confirma/<pk>', ReservaProjetorConfirmaUpdateView.as_view(), name="atualiza_reserva_projetor_confirma"),
    

    path('reserva_projetor_usuarios/cadastrar', ReservaProjetorUsuariosCreateView.as_view(), name="cadastra_reserva_projetor_usuarios"),   
    
    path('reserva_projetor_usuarios/<pk>', ReservaProjetorUsuariosUpdateView.as_view(), name="atualiza_reserva_projetor_usuarios"),
   
    # POST /reserva_projetors
    path('reserva_projetors/', ReservaProjetorListView.as_view(), name="lista_reserva_projetors"),
    
    path('reserva_projetors_usuario/', ReservaProjetorUsuarioListView.as_view(), name="lista_reserva_projetors_usuario"),
    
    path('reserva_projetors_nao_confirmada_usuario/', ReservaNaoConfirmadaProjetorUsuarioListView.as_view(), name="lista_reserva_projetors_nao_confirmada_usuario"),

    # GET/POST /reserva_projetors/excluir/{pk}
    path('reserva_projetor/excluir/<pk>', ReservaProjetorDeleteView.as_view(), name="deleta_reserva_projetor"),


]    
