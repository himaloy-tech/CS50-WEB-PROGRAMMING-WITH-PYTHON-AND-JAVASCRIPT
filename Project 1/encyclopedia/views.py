from django.shortcuts import render, HttpResponse, redirect
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def details(request, title):
    """
    detail of an entry
    """
    detail = util.get_entry(title=title)
    normal_text = markdown2.markdown(detail)
    return render(request, 'encyclopedia/details.html', {
        "text":normal_text,
        "title":title
    })

def search(request):
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
        return render(request, 'encyclopedia/results.html', {
            "results":results
        })