from django.http import HttpResponse
import random


name = "Faizan Tanveer"
number = random.randint(1, 22222)




H1_STRING = f"""<h1>Hello {name} -- {number}</h1>"""
P_STRING = f"""<p>Hello {name} -- {number}</p>"""
HTML_STRING = H1_STRING + P_STRING
def home_view(request):
    return HttpResponse(HTML_STRING)