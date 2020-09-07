from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse   
from . import util
from random import randrange

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request,title):
    html_entry=util.get_html(title)
    if(html_entry is not None):
        return render(request,"encyclopedia/entry.html",{"title":title, "entry":html_entry})
    else:
        html_entry="<h1><i class='material-icons'>error</i> Sorry, the page you requested was not found.</h1>"
        return render(request,"encyclopedia/entry.html",{"title":"error", "entry":html_entry})

def search_entry(request):   
    data=request.GET['q']
    html_entry=util.get_html(data)
    if(html_entry is not None):
        return render(request,"encyclopedia/entry.html",{"titel":data, "entry":html_entry})
    else:
        list_entries=util.contains_str(data)
        if list_entries is not None:
            return render(request, "encyclopedia/index.html", {"entries": list_entries})
        else:
            html_entry="<h1><i class='material-icons'>error</i> Sorry, the page you requested was not found.</h1>"
            return render(request,"encyclopedia/entry.html",{"title":"error", "entry":html_entry})

def new_page(request):
    return render(request, "encyclopedia/new_page.html")

def new_entry(request):
    title=request.POST['title']
    markdown=request.POST['markdown']
    if util.exists_entry(title) is False:
        util.save_entry(title,markdown)
        return HttpResponseRedirect(f"../{title}")
    else:
        mg="<h1><i class='material-icons'>warning</i> Entry already exists.</h1>"
        return render(request,"encyclopedia/entry.html",{"title":"prueba","entry":mg})

def edit_entry(request,title):
    if util.exists_entry(title):
        return render(request,"encyclopedia/edit.html",{"title":title,"entry":util.get_entry(title)})

def save_entry(request):
    title=request.POST['title']
    markdown=request.POST['markdown']
    if util.exists_entry(title):
        util.save_entry(title,markdown)
        return HttpResponseRedirect(title)
    else:
        mg="<h1><i class='material-icons'>warning</i>An error has occurred</h1>"
        return render(request,"encyclopedia/entry.html",{"title":"prueba","entry":mg})

def random_page(request):
    entries=util.list_entries()
    num_entries=len(entries)
    if num_entries>1:
        rand=randrange(num_entries)
        title=entries[rand]
        html_entry=util.get_html(title)
        return render(request, "encyclopedia/entry.html",{"title": title,"entry":html_entry})
        



     