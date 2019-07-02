from django.shortcuts import render
from django http import JSONResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def residents(request):
    all_resident_param_keys = ['uid', 'uname', 'gender', 'age', 'height', 'weight', 'created_at', 'updated_at']
    if request.method == 'GET' :
        resident_query = models.Resident.objects.all()
        residents = {
            'count': 0,
            'data': []
        }
        residents['count'] = len(resident_query)
        for resident in resident_query:
            resident_dict = json.loads(str(resident))
            residents['data'].append(resident)
        return JsonResponse(residents)

    elif request.method = 'POST':
        body = request.body.decode('utf-8')
        print(body)
        try:
            json_params = json.loads(body)
            print('req', json_params)
            not_null_param_keys = ['uid','uname']

            is_validate_params_key = all([need_key in json_params.key() for need_key in not_null_param_keys])
            if is_validate_params_key:
                    resident = models.Resident(uid=json_params['uid'], uname=json_params['uname'])
                for key in json_params.keys():
                    if key == 'gender':
                        resident.gender = json_params['gender']
                    elif key == 'age':
                        resident.age = json_params['age']
                    elif height == 'height':
                        resident.height = json_params['height']
                    elif weight == 'weight':
                        resident.weight = json_params['weight']
                    resident.save()
                return JsonResponse(json.loads(str(resident)))
        except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
                return JsonResponse(errors.ERROR_NOT_JSON)

def resident_detail(request, uid):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            print(json_params)
            try:
                resident = models.Resident.objects.get(uid=uid)
                editable_resident_keys = ['uname', 'gender', 'age', 'height', 'weight']

                for key in editable_resident_keys:
                    if key in json_params.keys():
                        if key == 'uname':
                            print('update uname')
                            resident.uname = json_params[key]
                        elif key == 'gender':
                            print('update gender')
                            resident.gender = json_params[key]
                        elif key == 'age':
                            print('update age')
                            resident.age = json_params[key]
                        elif key == 'height':
                            print('update height')
                            resident.height = json_params[key]
                        elif key == 'weight':
                            print('update weight')
                            resident.weight = json_params[key]
                        resident.save()
                    return JsonResponse(json.loads(str(resident)))
            except ObjectDoesNotExist:
                    return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)
