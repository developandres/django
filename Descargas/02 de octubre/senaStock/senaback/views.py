from django.shortcuts import render, redirect, get_object_or_404
from .models import ElementoConsumible
from .forms import ElementoConsumibleForm 
from django.http import JsonResponse



def index(request):
    elementos_consumibles = ElementoConsumible.objects.all()
    return render(request, 'senaback/index_main.html')

def login(request):
    return render(request, "senaback/login.html")

def otorgar_elemento(request):
    return render(request, "senaback/otorgar_elemento.html")

def obtener_elemento(request, elemento_id):
    try:
        elemento = ElementoConsumible.objects.get(pk=elemento_id)
        data = {
            'id': elemento.id,
            'nombre': elemento.nombre,
            'serial': elemento.serial,
            'cantidad': elemento.cantidad_total,
            'valor': elemento.valor,
            'categoria': elemento.categoria,
            'descripcion_elemento': elemento.descripcion_elemento,  # Cambiado a 'descripcion_elemento'
        }
        return JsonResponse(data)
    except ElementoConsumible.DoesNotExist:
        return JsonResponse({'error': 'Elemento no encontrado'}, status=404)


def listar_elementos_consumibles(request):
    filtro = request.GET.get('filtro', '')  # Obtener el valor del filtro de la URL
    elementos_consumibles = ElementoConsumible.objects.filter(nombre__icontains=filtro)
    return render(request, 'senaback/index_consumible.html', {'elemento_consumibles': elementos_consumibles, 'filtro': filtro})

def crear_elemento_consumible(request, elemento_id=None):
    elemento = None
    if elemento_id:
        elemento = get_object_or_404(ElementoConsumible, pk=elemento_id)

    if request.method == 'POST':
        form = ElementoConsumibleForm(request.POST, instance=elemento)
        if form.is_valid():
            form.save()
            return redirect('index_consumibles')
    else:
        form = ElementoConsumibleForm(instance=elemento)

    return render(request, 'senaback/index_consumibles.html', {'form': form})

