from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def areas(request):
    all_area_param_keys = ['areaid', 'areaname', 'created_at', 'updated_at']
    if request.method == 'GET':
        area_query = models.Area.objects.all()
        area = {
            'count' : 0,
            'data' : []
        }
        areas['count'] = len(beacons_query)
        for area in area_query:
            area_dict = json.loads(str(area))
            areas['data'].append(area_dict)
        return JsonResponse(areas)

    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            not_null_param_keys = ['areaid', 'areaname']

            if is_validate_params_key:
                area = models.Area(areaid=json_params['areaid'], areaname=json_params['areaname'])
                area.save()
                return JsonResponse(json.loads(str(area)))
            else:
                return JsonResponse(json.loads(str(area)))
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)

def area_detail(request, areaid):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            print(json_params)
            try:
                area = models.Area.objects.get(areaid=areaid)
                editable_area_keys = ['areaname']

                for key in editable_area_keys:
                    if key in json_params.keys():
                        if key == 'areaname':
                            print('update areaname')
                            area.areaname = json_params[key]

                            area.save()
                        return JsonResponse(json.loads(str(area)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JSONResponse(errors.ERROR_NOT_JSON)
