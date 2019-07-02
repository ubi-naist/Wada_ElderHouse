from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def careType(request):
    all_careType_param_keys = ['careid', 'caretype']
    if request.method == 'GET':
        careType_query = models.CareType.objects.all()
        careTypes = {
            'count': 0,
            'data': []
        }
        careTypes['count'] = len(careType_query)
        for careType in careType_query:
            careType_dict = json.loads(str(careType))
            careTypes['data'].append(careType_dict)
            return JsonResponse(careTypes)
    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        print(body)
        try:
            json_params = json.loads(body)
            print('req', json_params)
            not_null_param_keys = ['careid', 'caretype']

            is_validate_params_key = all([need_key in json_params.keys() for need_key in not_null_param_keys])

            if is_validate_params_key:
                careType = models.CareType(careid = json_params[careid], caretype = json_params[caretype])
                careType.save()
                return JsonResponse(json.loads(str(careType)))
            else:
                return JsonResponse(errors.ERROR_LACK_PARAMS)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)

def careType_detail(request, careid):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            print(json_params)
            try:
                careType = models.CareType.objects.get(careid=careid)
                editable_careType_keys = ['caretype']

                for key in editable_careType_keys:
                    if key in json_params.key():
                        if key == 'caretype':
                            print("update caretype")
                            careType.caretype = json_params[key]
                        careType.save()
                    return JsonResponse(json.loads(str(careType)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)
