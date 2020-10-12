from django.shortcuts import render, HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def details(request, title):
    detail = util.get_entry(title=title)
    if detail != None:
        return render(request, "encyclopedia/details.html", {
            "details": detail
        })
    else:
        return HttpResponse("Page not found")