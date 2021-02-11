from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Day, Morning, Night, Thought
import datetime
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
    print(date.today())
    day = Day.objects.filter(date = date.today()).first()
    # print(day.morning)
    # print(day.night)
    quote = "That's what."
    quoteAuth = "She"
    if day:
        isDayExist = True
    else:
        isDayExist = False
    context = {
        "user": user,
        "date": today,
        'isDay': isDayExist,
        "day": day,
        "quote": quote,
        "quoteAuthor": quoteAuth
    }
    return render(request, "journal_app/dashboard.html", context)

def get_today_date():
    return date.today()

# If a morning entry already exists for that day, it will display with an update button, and a form for the night entry
# When a user creates a night entry, it will see if a day entry already exists. Will add foreign key to day model
def create_day(user):
    user = user
    date = get_today_date()
    # page = 1
    # print("page: " + str(page))
    quote = "That's what."
    quoteAuthor = "She"
    dayObject = Day.objects.create(date = date, quote = quote, quote_author = quoteAuthor, user = user)
    return dayObject

# When a user creates a morning entry, it will create a day entry
def create_morning(request):
    # Checking to see if day already exists
    user = User.objects.get(id=request.session["user_id"])
    date = get_today_date()
    day = Day.objects.filter(date = date)
    # Check to see if day exists before creating day
    if len(day) > 0:
        messages.error(request, "Entry has already been created.", extra_tags="day")
        return redirect("/dashboard")
    # Create day, beore we create morning
    day = create_day(user)
    grateful_1 = request.POST["grateful_first"]
    grateful_2 = request.POST["grateful_second"]
    grateful_3 = request.POST["grateful_third"]
    great_1 = request.POST["great_first"]
    great_2 = request.POST["great_second"]
    great_3 = request.POST["great_third"]
    affirmation = request.POST["affirmation"]
    #Create morning, attach to newly created day object
    morning = Morning.objects.create(
        day = day,
        grateful_first = grateful_1,
        grateful_second = grateful_2,
        grateful_third = grateful_3,
        great_first = great_1,
        great_second = great_2,
        great_third = great_3,
        affirmation = affirmation
    )
    return redirect("/days/" + str(day.id) + "/show")

# Create night post, create relationship with day object
def create_night(request):
    day_id = request.POST["day_id"]
    day = Day.objects.get(id = day_id)
    amazing_1 = request.POST["amazing_first"]
    amazing_2 = request.POST["amazing_second"]
    amazing_3 = request.POST["amazing_third"]
    made_better = request.POST["made_better"]
    Night.objects.create(
        day = day,
        amazing_first = amazing_1,
        amazing_second = amazing_2,
        amazing_third = amazing_3,
        made_better = made_better
    )
    return redirect("/days/" + str(day.id) + "/show")

def days(request):
    if not 'user_id' in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    days = user.days.all().order_by("-date")
    context = {
        "days" : days,
        "user" : user
    }
    return render(request, "journal_app/days.html", context)

def show_day(request, id):
    if not 'user_id' in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    show_day = Day.objects.get(id = id)
    context = {
        "day" : show_day,
        "user" : user
    }
    return render(request, "journal_app/show_day.html", context)

def view_profile(request):
    if not 'user_id' in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    days = user.days.all()
    print(days)
    morning_count = 0
    night_count = 0
    for day in days:
        print(day)
        if day.morning:
            morning_count += 1
        try:
            if day.night:
                night_count += 1
        except Night.DoesNotExist:
            print("Night entry does not exist")
        # finally:
        #     if day.night:
        #         night_count += 1
        # if day.night:
        #     night_count += 1
    context = {
        "user" : user,
        "morning_c" : morning_count,
        "night_c" : night_count
    }
    return render(request, "journal_app/profile.html", context)

def about(request):
    if not 'user_id' in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    context = {'user' : user}
    return render(request, "journal_app/about.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")