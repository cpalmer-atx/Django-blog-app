When we navigate to localhost:8000/blog, the program first looks to django_project/urls.py to handle /blog

The script says to the app, 
    "Hey... someone navigated to /blog, is there an application that matches this?"

The app responds, "Yes!"  --path('blog/', include('blog.urls')

Script:  "Thanks, I'll process this /blog request to transfer to blog/urls.py

From blog/urls.py, Script asks,
    "I'm here now with my leftover empty string, is there any pattern that matches this?"

Script: "Yes!"  --path('', views.home, name='blog-home')

Script:  "Thanks, I'll head to views.py and look for the function named 'home' to find           out what to do."

From views.py:

def home(request):
    return HttpResponse('<h1>Blog Home</h1>)


NOTE:  After this explanation was given, we reomoved /blog from project/urls.py to ensure that localhost:8000 is the home directory for blog