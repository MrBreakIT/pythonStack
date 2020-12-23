from django.shortcuts import render, HttpResponse, redirect


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    pageview = request.session.get('pageview', 0)
    request.session['pageview'] = pageview + 1
    return render(request, 'index.html')

def add2(request):
    num_visits = request.session.get('num_visits') 
    request.session['num_visits'] = num_visits + 1
    return redirect('/')

def yourChoice(request):
    num_visits = request.session.get('num_visits') 
    # print (request.POST['choice'])
    print('*'*100)
    request.session['num_visits'] = num_visits + int(request.POST['choice']) -1 
    return redirect('/')

def destroySession(request): 
    del request.session['num_visits']
    del request.session['pageview']
    return redirect('/')


def visits(request):
    total = request.session['num_value']
    print(total)
    return redirect("/")








# ALTERNATIVE SOLUTION
# def index(request):
#     if 'counter' in request.session:
#         request.session[""] += 1
#     else:
#         request.session["counter"] = 1
#     return render(request, "index.html")


# def destroy_session(request):
#     if "counter" in request.session:
#         # resetting to zero
#         request.session["counter"] = 0
#         print(request.session.clear())
#         print(request.session.keys())
#     return redirect ('/')








# //////////////////////////////////////////////////////////
#                                          FIX LATER
# def destroy_session(request):
#     if request.session ['counter'] > 0:
#         return redirect("/")

# def deleteData(request):
#     del request.session['key_name']
#     return redirect('/')


    # if request.session['counter'] == 0:
    #     print('*'*50)
    #     request.session['counter'] += 1
    # else:
    #     request.session['counter'] = 0

    # return render(request, "index.html")