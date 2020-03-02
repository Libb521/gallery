from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    images= Image.objects.all()
    return render(request, 'welcome.html',{"images":images})

#..........
def today_images(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date, "image":image})

def past_images(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(today_day)

    return render(request, 'all-images/past-images.html', {"date": date, "images": images})

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def image(request):
    list = Album.objects.filter(is_visible=True).order_by('-created')
    paginator = Paginatior(list,8)

    oafe = request.Gert.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
    return render(request, 'image.html', {'albums': list })

def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})
