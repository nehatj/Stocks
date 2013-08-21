#Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate,login
from django.template import RequestContext
from django.http import HttpResponse
from django.http import Http404
from stock.models import Stock,NewStock
import re
#import pdb
#from datetime import datetime
def home(request):
    stock_list=Stock.objects.all().order_by('-created_at')[:22]
    newstock_list=NewStock.objects.all().order_by('-dt_created')
    search_stock=[]
    if request.POST:
         # stock=Stock.objects.all().order_by('-created_at')[:5]
          keys= []
          keys=request.POST.getlist('keywords')

 #         pdb.set_trace()
#          key_match='/b'+key+'/b'
          for i in stock_list:
            for key in keys:
              m=re.search(r'\b'+key+r'\b',(i.contents))
              if m :
                search_stock.append(Stock.objects.get(id=i.id))
              n=re.search(r'\b'+key+r'\b',(i.title))
              if n and not search_stock.__contains__(Stock.objects.get(id=i.id)):
                search_stock.append(Stock.objects.get(id=i.id))
  #        pdb.set_trace()
          if not search_stock:
            stock_list=NewStock.objects.filter(keywords=key)
          else:
            stock_list=search_stock

    return render_to_response('home.html',{'stock_list':stock_list,'newstock_list':newstock_list})
'''
def detail(request,stock_id):

    try:
        p = Stock.objects.get(pk=stock_id)
    except Stock.DoesNotExist:
        raise Http404
    return render_to_response('detail.html',{'stock':p})

def search(request):
     if request.POST:
        stock=Stock.objects.all().order_by('-created_at')[:5]
        key= ''
#        pdb.set_trace()
        key=request.POST.get('dob')
#        key=datetime.strptime(key,'%Y-%m-%d')

 #       stock_list=Stock.objects.filter(created_at__year=key.year,created_at__month=key.month,created_at__day=key.day)
        stock_list=Stock.objects.filter(keywords=key)

     return render_to_response('search.html',{'key':key,'stock_list':stock_list}, context_instance=RequestContext(request))
'''
