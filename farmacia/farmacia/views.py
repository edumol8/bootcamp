#from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Medicamento, Venta
from .forms import MedicamentoForm

from .models import Medicamento
from .serializers import MedicamentoSerializer
from rest_framework import viewsets

class MedicamentoView(viewsets.ModelViewSet):
    serializer_class = MedicamentoSerializer
    queryset = Medicamento.objects.all()


# def lista_medicamentos(request):
#     medicamentos = Medicamento.objects.all()
#     return render(request, 'farmacia/lista_medicamentos.html', {'medicamentos': medicamentos})


# def detalle_medicamento(request, id):
#     medicamento = get_object_or_404(Medicamento, id=id)
#     return render(request, 'farmacia/detalle_medicamento.html', {'medicamento': medicamento})




# def crear_medicamento(request):
#     if request.method == 'POST':
#         form = MedicamentoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Medicamento guardado correctamente")
#             return redirect('lista_medicamentos')
#         messages.error(request, "Hubo un error al guardar el medicamento")
#     else: 
#        form = MedicamentoForm()
#     return render(request, 'crear_medicamento.html', {'form': form})


# def editar_medicamento(request, id):
#     medicamento = get_object_or_404(Medicamento, id=id)
#     if request.method == 'POST':
#         form = MedicamentoForm(request.POST, instance=medicamento)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_medicamentos')
#     else:
#         form = MedicamentoForm(instance=medicamento)
#     return render(request, 'farmacia/editar_medicamento.html', {'form': form})

# def eliminar_medicamento(request, id):
#     medicamento = get_object_or_404(Medicamento, id=id)
#     if request.method == 'POST':
#         medicamento.delete()
#         return redirect('lista_medicamentos')
#     return render(request, 'farmacia/eliminar_medicamento.html', {'medicamento':medicamento})