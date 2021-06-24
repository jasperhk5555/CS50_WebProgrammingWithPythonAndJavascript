from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util

import markdown
import secrets


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, name):
    entry = util.get_entry(name)
    if entry is None:
        return render(request, "encyclopedia/nopage.html", {
        "name": name
        })
    else:
        return render(request, "encyclopedia/page.html", {
            "name": name, "link":"{}.md".format(name), 
            "content": markdown.markdown(entry)
    })

def search(request):
    value = request.GET.get('q')
    suggestions = []
    if util.get_entry(value) is None:
        for i in util.list_entries():
            if value.upper() in i.upper():
                suggestions.append(i)
        return render(request, "encyclopedia/index.html", {
            "entries": suggestions
            })
    else:
        return HttpResponseRedirect(f'/wiki/{value}')
  
def create(request):
    return render(request, "encyclopedia/create.html")

def upload(request):
    value = request.POST.get('q')
    content = request.POST.get('c')
    action = request.POST.get('a')
    if action == "edit":
        file = open(f"entries/{value}.md", 'w+')
        file.write(f"{content}")
        file.close()
        return HttpResponseRedirect(f'/wiki/{value}')
    elif util.get_entry(value) is None:
        file = open(f"entries/{value}.md", 'w')
        file.write(f"#{value}\n")
        file.write(f"{content}")
        file.close()
        return HttpResponseRedirect(f'/wiki/{value}')
    else:
        return HttpResponseRedirect(f'/existingpage')
        
def existing(request):
    return render(request, "encyclopedia/existingpage")

def edit(request, name):
    file = open(f"entries/{name}.md","r")
    lines = file.read()
    file.close()
    return render(request, "encyclopedia/edit.html", {
        "name":name, "content":lines
    })

def random(request):
    l = util.list_entries()
    choice = secrets.choice(l)
    return HttpResponseRedirect(f"/wiki/{choice}")

