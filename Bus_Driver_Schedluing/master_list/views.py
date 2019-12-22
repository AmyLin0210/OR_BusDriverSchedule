import pandas as pd
import json, os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return HttpResponse("I am in master_list!")

# Create your views here.
def showtemplate(request, date= "2019-12-19", route_id=0):

    route_data = pd.read_json(path_or_buf = settings.BASE_DIR + '/static/data/route.json', typ='series')

    route_schedule = pd.read_json(path_or_buf = settings.BASE_DIR + '/static/data/schedule_route/route_' + date + '.json', typ='series')
    schedule_info = {}
    for item in route_schedule:
        if item["route_id"] == route_id:
            schedule_info = item["route_item"]

    route_info = [{"id": i["route_id"], "name": i["route_name"]} for i in route_data ]
    route_item = route_data[route_id]["route_item"]

    driver_data = pd.read_json(path_or_buf = settings.BASE_DIR + '/static/data/driver.json', typ='series')

    for i, item in enumerate(route_item):
        for j, detail in enumerate(item["schedule"]["content"]):
            driver_id = schedule_info[str(item["route_item_id"])][str(detail["route_detail_id"])]
            route_item[i]["schedule"]["content"][j]["driver"] = str(driver_data[driver_id])
            route_item[i]["schedule"]["content"][j]["driver_id"] = driver_id


    return render(request, 'route_schedule.html', {
        "route_id":   route_id,
        "route_info": route_info,
        "route_item": route_item,
        "schedule_info": schedule_info,
        "driver_info": driver_data,
        "schedule_date": "2019-12-19"
    })
