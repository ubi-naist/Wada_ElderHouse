from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def toiletRecord(request):
    all_toiletRecord_param_keys = ['toilet_id', 'toilet_status', 'toilet_amount']
    if request.method == 'GET':
        toilets_query = models.ToiletRecord.objects.all()
        toilets = {
            'count': 0,
            'data': []
        }
        toilets['count'] = len(toilets_query)
        for toilet in toilets_query:
            toilet_dict = json.loads(str(toilet))
            toilets['data'].append(toilet_dict)
        return JsonResponse(toilets)

    elif request.method == 'POST'
        body = request.body.decode('utf-8')
        print(body)
        try:
            json_params = json.loads(body)
            print('req', json_params)
            not_null_param_keys = ['toilet_id']

            is_validate_params_key = all([need_key in json_params.keys() for need_key in not_null_param_keys])
            if is_validate_params_key:
                toilet = models.ToiletRecord(toilet_id = json_params['toilet_id'])
                for key in json_params.keys():
                    if key == 'toilet_status':
                        toilet.toilet_status = json_params['toilet_status']
                    elif key == 'toilet_amount':
                        toilet.toilet_amount = json_params['toilet_amount']
                toilet.save()
                return JsonResponse(json.loads(str(toilet)))
            else:
                return JsonResponse(json.loads(str(toilet)))
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)

def toilet_detail(request, toilet_id):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            jdon_params = json.loads(body)
            print(json_params)
            try:
                toilet = models.ToiletRecord.get(toilet_id=toilet_id)
                editable_toilet_keys = ['toilet_status', 'toilet_amount']
                for key in editable_toilet_keys:
                    if key in json_params.keys():
                        if key == 'toilet_status':
                            print('update toilet_status')
                            toilet.toilet_status = json_params[toilet_status]
                        elif key == 'toilet_amount':
                            print('update toilet_amount')
                            toilet.toilet_amount = json_params[toilet_amount]
                        toilet.save()
                    return JSONResponse(json.loads(str(toilet)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)
