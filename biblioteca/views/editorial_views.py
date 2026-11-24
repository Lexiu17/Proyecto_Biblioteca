from django.shortcuts import get_object_or_404, render
from biblioteca.models import editorial as Editorial

def editorial_list(request):
    editoriales = Editorial.objects.all()
    return render(request, 'biblioteca/editoriales/editorial_list.html',
                  {'editoriales': editoriales})


def editorial_detail(request, editorial_id):
    editorial = get_object_or_404(Editorial, pk=editorial_id)
    return render(request, 'biblioteca/editoriales/editorial_detail.html',
                  {'editorial': editorial})