from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

"""
version 1
def members(request):
    return HttpResponse("Hello world!")

version 2
def members(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render() )
"""

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
    mymember =  Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context={
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())



"""
VERSIÓN 1
def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  #context = {
  #  'fruits':['Apple','Banana','Cherry',],
  #  'firstname':'José Pinos'
  #}
  context={
    'mymembers':mymembers,
    'fruits':['Apple','Banana','Cherry','Strawberry'],
  }
  return HttpResponse(template.render(context, request))
"""
def testing(request):
  mydata = Member.objects.all().order_by('-lastName').values()#con values, me devuelve cada objeto como un diccionario
  miembros = Member.objects.filter(firstName='José').values() | Member.objects.filter(firstName='Diego').values()
  template = loader.get_template('template.html')
  #context = {
  #  'fruits':['Apple','Banana','Cherry',],
  #  'firstname':'José Pinos'
  #}
  context={
    'mymembers':mydata,
    'miembros':miembros,
  }
  return HttpResponse(template.render(context, request))