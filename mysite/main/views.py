from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

# this first one is for main/list.html as you can see in the return render(...) line
def index(response, id):
    # get id of to do list itself
    ls = ToDoList.objects.get(id=id)

    # define what to do from form submission
    # dictionary "name" points to "value" as defined in list.html form
    # {"save":["save"], "c1":["clicked"]}
    if response.method == "POST":
        print(response.POST)
        # user modifies check boxes and saves form
        if response.POST.get("save"):
            for item in ls.item_set.all():
                # if user clicks item complete, then record it as complete
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                # otherwise record it as not complete
                else:
                    item.complete = False
                # save every time
                item.save()
        
        # user adds a new to do item
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete = False)
            else:
                print("Invalid")

    #Display info on page
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})