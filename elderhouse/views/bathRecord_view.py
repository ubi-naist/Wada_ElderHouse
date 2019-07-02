from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def bathRecord(request):
    all_bathRecord_param_keys = ['bath_id', 'bath_status', 'bath_medicine']
    if request.method == 'GET':
        bath_query = models.bathRecord.objects.all()
        baths = {
            'count': 0,
            'data': []
        }
        baths['count'] = len(barh_query)
        for bath in bath_query:
            bath_dict = json.loads(str(bath))
            baths['data'].append(bath_dict)
        return JsonResponse(baths)

    elif request.method == 'POST'
        body = request.body.decode('utf-8')
        print(body)
        try:
            json_params = json.loads(body)
            print('req', json_params)
            not_null_param_keys = ['bath_id']

            is_validate_params_key = all([need_key in json_params.keys() for need_key in not_null_param_keys])
            if is_validate_params_key:
                bath = models.BathRecord(bath_id = json_params['bath_id'])
                for key in json_params.keys():
                    if key == 'bath_status':
                        bath.bath_status = json_params['bath_status']
                    elif key == 'bath_medicine':
                        bath.bath_amount = json_params['bath_medicine']
                bath.save()
                return JsonResponse(json.loads(str(bath)))
            else:
                return JsonResponse(json.loads(str(bath)))
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)

def bath_detail(request, bath_id):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            jdon_params = json.loads(body)
            print(json_params)
            try:
                bath = models.BathRecord.get(bath_id=bath_id)
                editable_bath_keys = ['bath_status', 'bath_medicine']
                for key in editable_bath_keys:
                    if key in json_params.keys():
                        if key == 'bath_status':
                            print('update bath_status')
                            bath.bath_status = json_params[bath_status]
                        elif key == 'bath_medicine':
                            print('update bath_medicine')
                            bath.bath_medicine = json_params[bath_medicine]
                        bath.save()
                    return JSONResponse(json.loads(str(bath)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)
