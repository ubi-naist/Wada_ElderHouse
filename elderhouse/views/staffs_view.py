from django.shortcuts import render
from django http import JSONResponse, HttpResponse
import json
from .. import models
from .. import errors
from datetime import datetime, timedelta, timezone

# Create your views here.
"""
def Hello(request):
 #print("HelloWorld")
 if request.method == 'GET':
  message = {
   'text':'HelloWorld'
  }
 return JsonResponse(message)
"""

def staffs(request):
    all_staff_param_keys = ['sid', 'sname', 'gender', 'age' 'created_at', 'updated_at', 'device_name']
    if request.method == 'GET' :
        staff_query = models.Staff.objects.all()
        staffs = {
            'count': 0,
            'data': []
        }
        staffs['count'] = len(staff_query)
        for staff in staff_query:
            staff_dict = json.loads(str(staff))
            staffs['data'].append(staff_dict)
        return JsonResponse(staffs)

    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        print(body)
        try:
            json_params = json.loads(body)
            print('req', json_params)
            not_null_param_keys = ['sid','sname']

            is_validate_params_key = all([need_key in json_params.keys() for
                need_key in not_null_param_keys])
            if is_validate_params_key:
                #一番大事な項目？
                staff = models.Staff(sid=json_params['sid'],sname=json_params['sname'])

                for key in json_params.keys():
                    if key == 'gender':
                        staff.gender = json_params['gender']
                    elif key == 'age':
                        staff.age = json_params['age']
                    elif key == 'device_name':
                        staff.device_name = json.params['device_name']
                staff.save()
                return JsonResponse(json.loads(str(staff)))
            else:
                return JsonResponse(errors.ERROR_LACK_PARAMS)
        except json.decoder.JSONDecodeError:
            return JsonResponse(errors.ERROR_NOT_JSON)

def staff_detail(request,sid):
    if request.method == 'PUT':
        body = request.body.decode('utf-8')
        try:
            json_params = json.loads(body)
            print(json_params)
            try:
                staff = models.Staff.objects.get(sid=sid)
                editable_staff_keys = ['sname', 'gender', 'age', 'device_name']

                for key in editable_staff_keys:
                    if key in json_params.keys():
                        if key == 'sname':
                            print("update name")
                            staff.name = json_params[key]
                        elif key == 'gender':
                            print("update gender")
                            staff.gender = json_params[key]
                        elif key == 'age':
                            print("update age")
                            staff.age = json_params[key]
                        elif key == 'device_name':
                            print("update device_name")
                            staff.device_name = json_params[key]
                        staff.save()
                return JsonResponse(json.loads(str(staff)))
            except ObjectDoesNotExist:
                return JsonResponse(errors.ERROR_DOES_NOT_EXIST)
        except json.decoder.JSONDecodeError:
            return JSONResponse(errors.ERROR_NOT_JSON)
