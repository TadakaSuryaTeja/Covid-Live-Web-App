from django.shortcuts import render

import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "8e363bf18dmsh73a305c9abab37ep148d75jsnac0f85c3f3fd",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloworldview(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method == "POST":
        selectedcountry = request.POST["selectedcountry"]
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                active = response['response'][x]['cases']['active']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {"selectedcountry": selectedcountry, "mylist": mylist, "new": new, "active": active, "critical": critical, "deaths": deaths,
                   "recovered": recovered, "total": total}
        return render(request, 'helloworld.html', context)

    context = {'mylist': mylist}
    return render(request, 'helloworld.html', context)
