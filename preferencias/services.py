from regalos.models import Regalo
def sugerir_regalos(preferencias):
    regalos = Regalo.objects.filter(
        precio__gte = preferencias.rango_min,
        precio__lte = preferencias.rango_max
    )
    
    #Filtrar por coincidencias simpples dedescripcion
    if preferencias.color:
        regalos = regalos.filter(descripcion__icontains=preferencias.color)
    if preferencias.perfume:
        regalos = regalos.filter(descripcion__icontains=preferencias.perfume)
    if preferencias.sabor:
        regalos = regalos.filter(descripcion__icontains=preferencias.sabor)
    
    return regalos    
        