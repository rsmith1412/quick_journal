from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Day, Morning, Night, Thought
from datetime import date
import bcrypt

# Create your views here.
def index(request):
    return render(request, "journal_app/index.html")

def register(request):
    return render(request, "journal_app/register.html")

def register_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='reg')
        return redirect("/register")
    else:
        name = request.POST["name"]
        alias = request.POST["alias"]
        age = request.POST["age"]
        email = request.POST["email"]
        pw = request.POST["password"]
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        print(pw_hash.decode())
        new_user = User.objects.create(name=name, alias=alias,age = age, email=email, password=pw_hash.decode())
        request.session["user_id"] = new_user.id
        return redirect("/dashboard")

def login(request):
    email = request.POST["email"]
    pw = request.POST["password_login"]
    # pw_hash = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    users = User.objects.filter(email = email)
    if len(users) == 0:
        messages.error(request, "User does not exist.", extra_tags='login')
        return redirect("/")

    user = users[0]
    if bcrypt.checkpw(pw.encode(), user.password.encode()):
        request.session["user_id"] = user.id
        return redirect("/dashboard")
    messages.error(request, "Invalid login.", extra_tags='login')
    return redirect("/")

#if isDay == false, form will show, else, entry will show and night form will appear
def dashboard(request):
    if not 'user_id' in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    today = date.today().strftime("%m/%d/%Y")
    day = Day.objects.filter(date = date.today())
    quote = "That's what."
    quoteAuth = "She"
    if len(day) == 0:
        isDayExist = False
    else:
        isDayExist = True
    context = {
        "user": user,
        "date": today,
        'isDay': isDayExist,
        "quote": quote,
        "quoteAuthor": quoteAuth
    }
    return render(request, "journal_app/dashboard.html", context)

# When a user creates a morning entry, it will create a day entry
def create_morning(request):
    grateful_1 = request.POST["grateful_first"]
    grateful_2 = request.POST["grateful_second"]
    grateful_3 = request.POST["grateful_third"]
    great_1 = request.POST["great_first"]
    great_2 = request.POST["great_second"]
    great_3 = request.POST["great_third"]
    affirmation = request.POST["affirmation"]
    date = request.POST[""]
    morning = Morning.objects.create(
        grateful_first = grateful_1,
        grateful_second = grateful_2,
        grateful_third = grateful_3,
        great_first = great_1,
        great_second = great_2,
        great_third = great_3,
        affirmation = affirmation
    )
    day = Day.objects.create(date=date)
    return redirect("/dashboard")
# If a morning entry already exists for that day, it will display with an update button, and a form for the night entry
# When a user creates a night entry, it will see if a day entry already exists. Will add foreign key to day model
# def create_day(page, date):
#     date = 

def logout(request):
    request.session.clear()
    return redirect("/")