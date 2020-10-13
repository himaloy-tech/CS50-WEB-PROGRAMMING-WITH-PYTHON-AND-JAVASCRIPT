from django.shortcuts import render, HttpResponse, redirect
import markdown2
from django.contrib import messages
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
    if detail == None:
        return HttpResponse("Page Not Found")
    else:
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
def create(request):
    """
    create a new page
    """
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title=title) is not None:
            messages.error(request, f"A entry with the name {title} already exists")
            return redirect('/create')
        else:
            if "#" in title:
                pass
            else:
                title = "# "+title
            util.save_entry(title=title, content=content)
            detail = util.get_entry(title=title.replace('# ', ''))
            normal_text = markdown2.markdown(detail)
            return render(request, 'encyclopedia/details.html', {
                "text":normal_text,
                "title":title
            })
    return render(request, 'encyclopedia/add.html')