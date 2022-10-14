from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"pages/home.html")
def reg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        worktype = request.POST.get("worktype")
        skills = request.POST.getlist("skills")

        if request.FILES:
            file = request.FILES['profilepic']
            fs = FileSystemStorage()
            savedfile = fs.save(file.name,file)
            file_url = fs.url(savedfile)
        return HttpResponse("<h1>SUCCESS!!</h1><br><h3>DATA IS </h3> <br> {},{},{},{},{},{},<img src = '{}' ,height = 200px, width = 100px>".format(name,email,gender,worktype,skills,file,file_url))

    return render(request,"pages/form.html")
