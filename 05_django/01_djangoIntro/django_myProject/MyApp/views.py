from django.shortcuts import render, HttpResponse

# Create your views here.
# def one_method(request):
#     pass

# def another_method(request, my_val):
#     pass

# def yet_another(request, name):
#     pass

# def one_more(request, id, color):
#     pass


# from django.shortcuts import HttpResponse, redirect # add redirect to import statement
# from django.http import JsonResponse
# def root_method(request):
#     return HttpResponse("String response from root_method")
# def another_method(request):
#     return redirect("/redirected_route")
# def redirected_method(request):
#     return JsonResponse({"response": "JSON response from redirected_method", "status": True})






def index(request):
    return HttpResponse("response from index method from root route, localhost:8000!")










