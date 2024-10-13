# views.py in shortener app
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render


def index(request):
    """
        Renders the home page for the URL shortening service and handles URL shortening requests.

        If the request method is POST and an original URL is provided, it creates a new ShortURL instance,
        generates the shortened URL, and renders it on the page. Otherwise, it simply renders the home page.

        Args:
            request (HttpRequest): The HTTP request object. It can contain a POST request with the original URL.

        Returns:
            HttpResponse: A rendered 'index.html' template with the shortened URL (if generated) included in the context.
        """
    short_url = None
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        if original_url:
            # Create a new ShortURL instance
            short_url_instance = ShortURL.objects.create(original_url=original_url)
            short_url = request.build_absolute_uri('/') + short_url_instance.short_url
    return render(request, 'index.html', {'short_url': short_url})


@api_view(['POST'])
def shorten_url(request):
    """
        Shortens a given URL and returns the shortened version.

        This view accepts a POST request containing a URL to be shortened.
        It validates the input using the ShortURLSerializer, creates a new
        shortened URL instance, and returns the full shortened URL.

        Args:
            request (HttpRequest): The HTTP request object containing the URL to be shortened in its data.

        Returns:
            Response: If successful, returns a Response with the full shortened URL.
                      If the data is invalid, returns a Response with the validation errors and a 400 status code.
        """
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        short_url_instance = serializer.save()
        return Response(dict(short_url= request.build_absolute_uri('/') + short_url_instance.short_url))
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def redirect_to_original(request, short_url):
    """
        Redirects to the original URL for a given shortened URL.

        This view accepts a GET request with a short URL and attempts to find the corresponding original URL
        in the database. If found, it redirects the user to the original URL. If the short URL does not exist,
        it returns a 404 response.

        Args:
            request (HttpRequest): The HTTP request object.
            short_url (str): The shortened URL path to look up in the database.

        Returns:
            HttpResponseRedirect: A redirect response to the original URL.
                                  If the short URL is not found, raises a 404 error.
        """
    url_instance = get_object_or_404(ShortURL, short_url=short_url)
    return redirect(url_instance.original_url)
