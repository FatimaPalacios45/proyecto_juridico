from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.db.models import Q
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.

    
class Inicio(TemplateView, LoginRequiredMixin):
    template_name='inicio.html'
    
class ListarTiposDeAbogados(ListView):
    model = TipoDeAbogado
    template_name = "abogados/tp_abogado_listado.html"
    context_object_name='tipos'
    queryset=TipoDeAbogado.objects.all()
    paginate_by=10
    
    #Para la barra de busqueda
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return TipoDeAbogado.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    
class CrearTipoDeAbogado(CreateView):
    model = TipoDeAbogado
    form_class=TipoDeAbogadoForm
    template_name = "abogados/tp_abogado_crear.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_abogado')
    
class ActualizarTipoDeAbogado(UpdateView):
    model = TipoDeAbogado
    form_class=TipoDeAbogadoForm
    template_name = "abogados/tp_abogado_editar.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_abogado')
    
class EliminarTipoDeAbogado(DeleteView):
    model = TipoDeAbogado
    template_name = "abogados/tp_abogado_borrar.html"
    success_url=reverse_lazy('tipo_de_abogado')
    

class Login(FormView):
    template_name = 'sesion/login.html'
    form_class = FormLogin
    context_object_name='login'
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/sesion/login/')

from django.http import HttpResponseRedirect

def someview(request):
   ...
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CrearCaso(CreateView):
    model = Caso
    form_class=CasoForm
    template_name = "casos/caso.html"
    success_url=reverse_lazy('caso')

class CrearTipoDeProceso(CreateView):
    model =TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/crear_tipo_proceso.html"
    success_url=reverse_lazy('tipo_de_abogado')
    
class ListarTiposDeProcesos(ListView):
    model = TipoDeProceso
    template_name = "procesos/tp_proceso_listado.html"
    context_object_name='tp_p'
    queryset=TipoDeProceso.objects.all()
    paginate_by=10
    
    #Para la barra de busqueda
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return TipoDeProceso.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    
class CrearTipoDeProceso(CreateView):
    model = TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/tp_proceso_crear.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_proceso')
    
class ActualizarTipoDeProceso(UpdateView):
    model = TipoDeProceso
    form_class=TipoDeProcesoForm
    template_name = "procesos/tp_proceso_editar.html"
    context_object_name='tipos'
    success_url=reverse_lazy('tipo_de_proceso')
    
class EliminarTipoDeProceso(DeleteView):
    model = TipoDeProceso
    template_name = "abogados/tp_abogado_borrar.html"
    success_url=reverse_lazy('tipo_de_proceso')
    
class ListaCliente(ListView):
    model=Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name='clientes'
    #solo los que son cliente
    queryset=Cliente.objects.all()
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Cliente.objects.filter(
            Q(nombre__icontains=self.request.GET['buscar'])|
            Q(correo__icontains=self.request.GET['buscar'])|
            Q(dui__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    #success_url=reverse_lazy('inicio')
    
class CrearCliente(CreateView):
    model = Cliente
    form_class=FormCliente
    template_name = "clientes/cliente_crear.html"
    context_object_name='tipos'
    success_url=reverse_lazy('cliente')
 

class ActualizarCliente(UpdateView):
    model = Cliente
    form_class=FormCliente
    template_name = "clientes/cliente_editar.html"
    success_url=reverse_lazy('cliente')
    
class EliminarCliente(DeleteView):
    model = Cliente
    template_name = "clientes/cliente_borrar.html"
    success_url=reverse_lazy('cliente')
    
    

class ListaCasos(ListView):
    model=Caso
    template_name = "casos/listar.html"
    context_object_name='clientes'
    #solo los que son cliente
    queryset=Caso.objects.all()
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Caso.objects.filter(
            Q(codigo__icontains=self.request.GET['buscar'])|
            Q(descripcion__icontains=self.request.GET['buscar'])
        ).distinct()
        return super().get_queryset()
    #success_url=reverse_lazy('inicio')

class EliminarCaso(DeleteView):
    model = Caso
    template_name = "casos/caso_borrar.html"
    success_url=reverse_lazy('caso')

class ActualizarCaso(UpdateView):
    model = Caso
    form_class=CasoForm
    template_name = "casos/caso_editar.html"
    success_url=reverse_lazy('caso')
    
class CrearFormaDePago(CreateView):
    model = FormaDePago
    form_class=FormaDePagoForm
    template_name = "formapago/crear.html"
    context_object_name='formapagos'
    success_url=reverse_lazy('CrearCaso')    