# This is my views.py

from django.shortcuts import render


def home(request):
    import json
    import requests

    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=0&API_KEY=E6F5C6C1-EE31-48EC-A454-A9E0642C1062")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode + ""
           " &distance=0&API_KEY=E6F5C6C1-EE31-48EC-A454-A9E0642C1062")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_decription = "(0-50) Air quality is considered satisfactory, and air polution poses litle or no risk"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_decription = "(50-100) Air quality is acceptable."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_decription = "(101-150) Air quality is Unhealthy"
            category_color = "unhealthy"

        return render(request, 'home.html', {'api': api, 'category_decription': category_decription, 'category_color':
            category_color})


    else:

        if api[0]['Category']['Name'] == "Good":
            category_decription = "(0-50) Air quality is considered satisfactory, and air polution poses litle or no risk"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_decription = "(50-100) Air quality is acceptable."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_decription = "(101-150) Air quality is Unhealthy"
            category_color = "unhealthy"

        return render(request, 'home.html', {'api': api, 'category_decription': category_decription, 'category_color':
            category_color})


def about(request):
    return render(request, 'about.html', {})
