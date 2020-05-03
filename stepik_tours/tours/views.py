from django.shortcuts import render
from django.views import View


# Main page
class MainView(View):
    def get(self, request):
        return render(request, "tours/main.html")


# Departure page
class DepartureView(View):
    def get(self, request, departure):
        return render(request, "tours/departure.html")


# Tour page
class TourView(View):
    def get(self, request, id):
        return render(request, "tours/tour.html")
