from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def records(request):
    all_record_param_keys = ['rid', 'sid', 'uid', 'areaid', 'cid', 'created_at', 'updated_at']

    if request.method == 'GET':
        records_query = models.Record.objects.all()
        records = {
            'count': 0,
            'data': []
        }
        records['count'] = len(records_query)
        for record in records_query:
            record_dict = json.loads(str(record))
            records['data'].append(record_dict)
        return JsonResponse(records)
    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        print(body)
        try:
            json_params = json.loads(body)
            print('req', json_params)
            not_null_param_keys = ['rid']

            is_validate_params_key = all([need_key in json_params.keys() for need_key in not_null_param_keys])
            if is_validate_params_key:
                rid = json_params['rid']

                for key in json_params.keys():
                    if key == 'sid':
                        record.sid = json_params['sid']
                    elif key == 'uid':
                        record.uid = json_params['uid']
                    elif key == 'areaid':
                        record.areaid = json_params['areaid']
                    elif key == 'cid':
                        record.cid = json_params['cid']
                record.save()
                return JsonResponse(json.loads(str(record)))
            else:
                return JsonResponse(json.ERROR_LACK_PARAMS)
        except json.decoder.JSONDecodeError:
            return JSONResponse(errors.ERROR_NOT_JSON)

def record_detail(request,rid):
    if request.method == 'PUT':
        body = request.body.recode('utf-8')
        try:
            json_params = json.loads(body)
            print(json_params)
            try:
                record = models.Record.objects.get(rid=rid)
                editable_record_keys = ['sid', 'uid', 'areaid', 'cid']

                for key in editable_record_keys:
                    if key in json_params.keys():
                        if key == 'sid':
                            print('update sid')
                            record.sid = json_params[key]
                        elif key == 'uid':
                            print('update uid')
                            record.uid = json_params[key]
                        elif key == 'areaid':
                            print('update areaid')
                            record.areaid = json_params[key]
                        elif key == 'cid':
                            print('update cid')
                            record.cid = json_params[key]
                        record.save()
                    return JsonResponse(json.loads(str(record)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)
