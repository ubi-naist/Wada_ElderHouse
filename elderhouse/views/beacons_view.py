from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

def beacons(request):
    all_beacon_param_keys = ['bid', 'uuid', 'major', 'minor', 'type', 'created_at', 'updated_at']
    if request.method == 'GET':
        beacons_query = models.Beacon.objects.all()
        beacons = {
            'count': 0,
            'data': []
        }
        beacons['count'] = len(beacons_query)
        for beacon in beacons_query:
            beacon_dict = json.loads(str(beacon))
            beacons['data'].append(beacon_dict)
        return JsonResponse(beacons)

    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            not_null_param_keys = ['bid', 'uuid', 'major', 'minor']

            is_validate_params_key = all([need_key in json_params.keys() for need_key in not_null_param_keys])
            if is_validate_params_key:
                bid = json_params['bid']
                try:
                    #user = models.User.objects.get(uid = uid)
                    uuid = json_params['uuid']
                    major = json_params['major']
                    minor = json_params['minor']
                    beacon = models.Beacon(uuid=uuid, major=major, minor=minor)

                    for key in json_params.keys():
                        if key == 'type':
                            beacon.type = json_params['type']

                    beacon.save()
                    return JsonResponse(json.loads(str(beacon)))
                except ObjectDoesNotExist:
                    return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
            return JsonResponse(errors.ERROR_LACK_PARAMS)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)

def beacon_detail(request, bid):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            print(json_params)
            try:
                beacon = models.Beacon.objects.get(bid=bid)
                editable_beacon_keys = ['uuid', 'major', 'minor', 'type']

                for key in editable_staff_keys:
                    if key in json_params.keys():
                        if key == 'uuid':
                            print('update uuid')
                            beacon.uuid = json_params[key]
                        elif key == 'major':
                            print('update major')
                            beacon.major = json_params[key]
                        elif key == 'minor':
                            print('update minor')
                            beacon.minor = json_params[key]
                        elif key == 'type':
                            print('update type')
                            beacon.type = json_params[key]
                        beacon.save()
                return JsonResponse(json.loads(str(beacon)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)
