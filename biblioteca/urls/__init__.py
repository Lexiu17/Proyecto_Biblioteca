from biblioteca.urls.home_url import urlpatterns as home_urls
from biblioteca.urls.editorial_urls import urlpatterns as editorial_urls
from biblioteca.urls.autor_urls import urlpatterns as autor_urls
from biblioteca.urls.libro_urls import urlpatterns as libro_urls
from biblioteca.urls.prestamo_urls import urlpatterns as prestamo_urls

urlpatterns = home_urls + editorial_urls + autor_urls + libro_urls + prestamo_urls