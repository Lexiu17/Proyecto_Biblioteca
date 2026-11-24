from django.shortcuts import get_object_or_404, render
from biblioteca.models import autor as Autor

def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autores/autor_list.html',
                  {'autores': autores})


def autor_detail(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'biblioteca/autores/autor_detail.html',
                  {'autor': autor})