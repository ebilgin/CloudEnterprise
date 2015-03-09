from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from a_inv.models import Supplier

# Create your views here.




def index(request):
    return HttpResponse("Hello, world. You're at the Inventory index.")

def supplier_view(request, idn):
    try:
        supplier_list = [s for s in Supplier.objects.all() if s.supplier_idn<=idn]
        context = {'supplier_list_hvar': supplier_list}
    except Supplier.DoesNotExist:
        raise Http404("Supplier does not exist")
    return render(request, 'a_inv/index.html', context)
    
    
def supplier_detail(request, idn):
    try:
        name = Supplier.objects.get(supplier_idn=idn).supplier_name
        response = name+" is number %s."
    except Supplier.DoesNotExist:
        raise Http404("Supplier does not exist")
    return HttpResponse(response % idn)

class DetailView(generic.DetailView):
    model = Supplier
    template_name = 'a_inv/detail.html'
