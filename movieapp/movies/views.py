from django.shortcuts import render

kategori_liste = ["macera", "dram", "komedi", "korku"]
film_liste = [
    {
        "film_adi": "film1",
        "film_aciklama": "aciklama1",
        "film_resim": "https://picsum.photos/id/237/200/300"
    },
        {
        "film_adi": "film2",
        "film_aciklama": "aciklama2",
        "film_resim": "https://picsum.photos/id/237/200/300"
    },
        {
        "film_adi": "film3",
        "film_aciklama": "aciklama3",
        "film_resim": "https://picsum.photos/id/237/200/300"
    },

]
def home(request):
    return(render(request, "index.html"))

def movies(request):
    
    data = {
        "kategoriler": kategori_liste,
        "filmler": film_liste
    }

    return(render(request, "movies.html", data))
