from app.models import products

def prodprocess(request):
    return {'prodprocess': products.objects.all()}