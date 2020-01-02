import pandas as pd
import json, os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return HttpResponse("I am in master_list!")

def getRouteInfo(route_data, route_id, route_item_id, route_detail_id):
    route_info = {}
    route_info["route_detail_id"] = route_detail_id

    route = [item for item in route_data if item["route_id"] == route_id]
    route_item = [item for item in route[0]["route_item"] if item["route_item_id"] == route_item_id]
    route_info["route_item_name"] = route_item[0]["item_name"]

    route_detail = [item for item in route_item[0]["schedule"]["content"] if item["route_detail_id"] == route_detail_id]
    route_arrive_time = route_detail[0]["arrive_time"]
    for i in range(len(route_arrive_time)):
        if route_arrive_time[i] != "":
            route_info["arrive_time"] = route_arrive_time[i]
            route_info["stop"] = route_item[0]["schedule"]["title"][i]
            break

    return route_info
                    

# Create your views here.
def showtemplate(request, driver_id=21, week = "7", date_from= "2019-12-19", date_to= "2019-12-19"):

    driver_data = pd.read_json(path_or_buf = settings.BASE_DIR + '/static/data/driver.json', typ='series')
    driver_info = []
    for i, name in driver_data.items():
        driver_info.append({
            "id": i,
            "name": name
        })

    driver_schedule_data = pd.read_json(path_or_buf = settings.BASE_DIR + '/static/data/schedule_driver/driver_' + week + '.json', typ='series')
    driver_schedule_info = []
    for driver in driver_schedule_data["schedule"] :
        if driver["bus_driver_id"] == int(driver_id):
            driver_schedule_info.append(driver["bus_driver_schedule"])

    route_data = pd.read_json(path_or_buf = settings.BASE_DIR + '/static/data/routes/route_' + week + '.json', typ='series')
    route_info = []
    for item in driver_schedule_info[0]:
        route_info.append(getRouteInfo(route_data, item["route_id"], item["route_item_id"], item["route_detail_id"]))
    
    print(route_info)

    return render(request, 'driver_schedule.html', {
        "driver_id":   driver_id,
        "driver_name": driver_data[driver_id],
        "driver_info": driver_info,
        "week":        week,
        "driver_schedule": driver_schedule_info,
        "route_info":   route_info
    })
