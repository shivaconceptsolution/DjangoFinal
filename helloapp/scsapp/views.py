from django.shortcuts import render


def index(request):
	return render(request,"scsapp/index.html")
def about(request):
	return render(request,"scsapp/about.html")
def service(request):
	return render(request,"scsapp/services.html")
def contact(request):
	return render(request,"scsapp/contact.html")
def gallery(request):
	return render(request,"scsapp/gallery.html")

