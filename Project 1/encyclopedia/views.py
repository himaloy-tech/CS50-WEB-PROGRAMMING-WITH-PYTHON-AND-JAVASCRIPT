from django.shortcuts import render, HttpResponse, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def details(request, title):
    detail = util.get_entry(title=title)
    normal = detail.replace(f'# {title}', '')
    if detail != None:
        return render(request, "encyclopedia/details.html", {
            "title":title,
            "text":normal.split(),
        })
    else:
        return HttpResponse("Page not found")

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        result = util.get_entry(title=query)
        if result is not None:
            return redirect(f'/details/{query}')
        else:
            results = []
            for entry in util.list_entries():
                if query in entry:
                    results.append(entry)
                else:
                    continue
            return render(request, 'encyclopedia/results.html', context={
                "results":results
            })
    else:
        return HttpResponse("Page not found")