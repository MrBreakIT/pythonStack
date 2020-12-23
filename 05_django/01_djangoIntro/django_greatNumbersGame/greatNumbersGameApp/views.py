from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    # print('*'*50)
    numGen = random.randint(1,10) 
    request.session['numGen'] = numGen
    # inputFromForm = request.POST['userInput']
    context = {
        "storedValue": numGen,
        # "storedValue2": inputFromForm
    }
    print("Computer chose:", numGen)
    # print("User chose:", userInput)
    # print('*'*50)
    return render (request, 'index.html', context)

def checkNum(request):
    print('*'*50)
    # print("User entered:", request.POST["userInput"])
    if int(request.POST["userInput"]) == request.session['numGen']:
        match= int(request.POST["userInput"])        
        # print("Computer chose:", numGen)
        print("----------<<<<< Run Program  >>>>>----------")
        print("Computer chose:", request.session["numGen"]) 
        print("Your guess was:", request.POST["userInput"])
        print("WinnnnnnnnnER!")
        print("----------<<<<< End Program  >>>>>----------")
        print('*'*50)
    elif int(request.POST["userInput"]) > request.session['numGen']:
        high= int(request.POST["userInput"])
        print('*'*50)
        # print("Computer chose:", numGen)
        print("----------<<<<< Run Program  >>>>>----------") 
        print("Computer chose:", request.session["numGen"]) 
        print("Your guess was:", request.POST["userInput"])
        print("Too High Dummy!")
        print("----------<<<<< End Program  >>>>>----------")
        print('*'*50)
    elif int(request.POST["userInput"]) < request.session['numGen']:
        low= int(request.POST["userInput"])        
        print('*'*50)
        # print("Computer chose:", numGen)
        print("----------<<<<< Run Program  >>>>>----------")
        print("Computer chose:", request.session["numGen"]) 
        print("Your guess was:", request.POST["userInput"])
        print("Too Low DumDum!")
        print("----------<<<<< End Program  >>>>>----------")
        print('*'*50)
    return redirect('/')








