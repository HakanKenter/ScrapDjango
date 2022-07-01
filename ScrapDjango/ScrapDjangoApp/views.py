from django.shortcuts import render, redirect
from .models import Annonce
from .forms import AnnonceForm
from .scraping import scrap_info

# Create your views here.
def index(request):
    return render(request, "ScrapDjangoApp/index.html")

#_____________________________________________ Annonce Crud _______________________________________________

#READ ALL
def all_annonce(request):
    Annonce_object = Annonce.objects.all()
    return render(request, "ScrapDjangoApp/annonces.html", {"Annonce_object": Annonce_object})

def details_annonce(request, id):
    Annonce_object = Annonce.objects.get(id=id)
    return render(request, "ScrapDjangoApp/details_annonce.html", {"Annonce_object": Annonce_object})

def add_annonce(request):
    form = AnnonceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=AnnonceForm()
        return redirect("confirmation")
    return render(request, "ScrapDjangoApp/add_annonce.html", {"form": form})

def update_annonce(request, id):
    Annonce_object = Annonce.objects.get(id=id)
    if request.method == "POST":
        form = AnnonceForm(request.POST, instance=Annonce_object)
        if form.is_valid():
            form.save()
            return redirect("confirmation")
    else:
        form = AnnonceForm(instance=Annonce_object)  
    return render(request, "ScrapDjangoApp/udpate_annonce.html", {"form": form})

def delete_annonce(request, id):
    Annonce_object=Annonce.objects.get(id=id)
    if request.method == "POST":
        Annonce_object.delete()
        return redirect("confirmation")
    return render(request, "ScrapDjangoApp/delete_annonce.html", {"Annonce_object":Annonce_object})

#__________________________________________________________________________________________________________

def confirmation(request):
    return render(request, "ScrapDjangoApp/confirmation.html")

#______________________________________________SCRAPING____________________________________________________

def scraping(request):
    datas = scrap_info("https://www.letudiant.fr/fiches/etudes/filieres-ecole-d-ingenieurs/secteurs-43+49.html")
    return render(request, "ScrapDjangoApp/scraping.html", {"datas": datas})