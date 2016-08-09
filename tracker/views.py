from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from.forms import *
import socket
import sys
import MySQLdb


# Create your views here.
@login_required
def home(request):
    return render(request,'home.html',{'user': request.user})

def adduser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            return  HttpResponseRedirect('/')
    else:
        form = AddUserForm()
    return render(request,"adduser.html",{'form':form})

def adddevice(request):
    user_list = User.objects.all()
    ip_list = IP.objects.all()
    port_list = Port.objects.all()
    if request.method == 'POST':
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            #form.user = request.REQUEST['user']

            device = form.save()
            device.save()
            return  HttpResponseRedirect('/')
    else:
        form = AddDeviceForm()
    return render(request,"adddevice.html",{'form':form,'user_list':user_list, 'ip':ip_list, 'port':port_list})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            profile = form.save()
            profile.save()
            return HttpResponseRedirect('/')
    else:
        form = UpdateProfile(initial={'email':user.email, 'first_name':user.first_name,'last_name':user.last_name})
    return render(request, 'update_profile.html', {'form':form})


def track(request):
    try:
        db = MySQLdb.connect(host="188.166.219.4",
                                 user="root",
                                 passwd="root",
                                 db="gmap")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit();
    cursor = db.cursor()
    cursor.execute("""SELECT DISTINCT DeviceId  FROM coordinates """)
    row = cursor.fetchall()
    rows = list(row)

    for row in rows:
        device_id = row[0]
        #lat = row[1]
        #lng = row[2]
        #speed = row[3]

    return render(request,"track.html",{'rows':rows})


@csrf_exempt
def trackdetails(request):
    device_id = request.POST.get('vardeviceid',False)
    try:
        db = MySQLdb.connect(host="188.166.219.4",
                             user="root",
                             passwd="root",
                             db="gmap")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit();
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM coordinates WHERE DeviceId LIKE %s  ORDER BY time  DESC LIMIT 1""",  ("%" + device_id + "%",))
    #cursor.execute("""SELECT * FROM coordinates WHERE DeviceId LIKE %s LIMIT 1""", ("%" + device_id + "%",))
    rows = cursor.fetchall()
    for r in rows:
        device = r[0]
        lat = r[1]
        lng = r[2]
        speed = r[3]
        time =  r[4]
        html = '''<ul class="data" style="list-style:none;margin:8px 0px 0px -38px;">
                    <li><div><label class="label1">Status: Running </label></div></li>
                    <li><div><label class="label1">Latitude:<span id= lat> %s </span> </label></div></li>
                    <li><div><label class="label1">Langitude:<span id= lng> %s </span></label></div></li>
                    <li><div><label class="label1">Time: %s</label></div></li>
                    <li><div><label class="label1">Speed: %s</label></div></li>
                    <li><div><label class="label1">AC: On </label></div></li>
                    <li><div><label class="label1">Fuel: Low  </label></div></li>
                    </ul>''' %(lat,lng,time,speed)

    return HttpResponse(html)

@csrf_exempt
def mobileReg(request):
    try:
        db = MySQLdb.connect(host="", user="root", passwd="root",  db="gmap")
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit();
    cursor = db.cursor()
    if request.method == 'POST':
        form = Mobile_regForm(request.POST)
        if form.is_valid():
            '''mobile_no = request.POST.get('mobile_no')
            device_no = request.POST.get('device_no')
            eng_notify = request.POST.get('notify_eng')
            ac_notify = request.POST.get('notify_ac')
            door_notify = request.POST.get('notify_door')
            status_notify = request.POST.get('notify_status')
            fuel_notify = request.POST.get('notify_fuel')
            speed_notify = request.POST.get('notify_speed')
            where_notify = request.POST.get('notify_where')
            eng_alert = request.POST.get('alert_eng')
            ac_alert = request.POST.get('alert_ac')
            door_alert = request.POST.get('alert_door')
            status_alert = request.POST.get('alert_status')
            fuel_alert = request.POST.get('alert_fuel')
            speed_alert = request.POST.get('alert_speed')
            where_alert = request.POST.get('alert_where')
            eng_enable = request.POST.get('enable_eng')
            ac_enable = request.POST.get('enable_ac')
            door_enable = request.POST.get('enable_door')
            status_enable = request.POST.get('enable_status')
            fuel_enable = request.POST.get('enable_fuel')
            speed_enable = request.POST.get('enable_speed')
            where_enable = request.POST.get('enable_where')
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            radius = request.POST.get('radius')
            speed = request.POST.get('speed')

            print eng_enable
            print ac_notify
            print eng_notify

            data = MobileReg(device_id = device_no, mobile_no = mobile_no, eng_notify = eng_notify, ac_notify= ac_notify, door_notify = door_notify,
                             status_notify = status_notify, fuel_notify=fuel_notify, speed_notify = speed_notify, where_notify = where_notify,
                             eng_alert = eng_alert, ac_alert = ac_alert, door_alert = door_alert,status_alert = status_alert, fuel_alert = fuel_alert,
                             speed_alert = speed_alert, where_alert= where_alert, eng_eable = eng_enable, ac_enable = ac_enable,door_enable = door_enable,
                             status_enable = status_enable, fuel_enable = fuel_enable, speed_enable  = speed_enable, where_enable = where_enable,
                             lat = lat, lng = lng, radius = radius, speed = speed)
            data.save()'''

            '''data = MobileReg.objects.update_or_create(
                mobile_no = form.cleaned_data['mobile_no'],
                device_id = form.cleaned_data['device_no'],
                eng_notify = form.cleaned_data['eng_notify'],
                ac_notify =form.cleaned_data['notify_eng'],
                door_notify = form.changed_data['door_notify'],
                status_notify =form.cleaned_data['status_notify'],
                fuel_notify = form.cleaned_data['fuel_notify'],
                speed_notify = form.cleaned_data['speed_notify'],
                where_notify = form.cleaned_data['where_notify'],

                eng_alert = form.cleaned_data[' eng_alert'],
                ac_alert = form.cleaned_data[' ac_alert'],
                door_alert = form.cleaned_data[' door_alert'],
                status_alert = form.cleaned_data[' status_alert'],
                fuel_alert = form.cleaned_data[' fuel_alert'],
                speed_alert=form.cleaned_data[' speed_alert'],
                where_alert = form.cleaned_data[' speed_alert'],

                eng_eable = form.cleaned_data['notify_eng'],
                ac_enable = form.changed_data['ac_enable'],
                door_enable = form.changed_data['door_enable'],
                status_enable = form.changed_data['status_enable'],
                fuel_enable = form.changed_data['fuel_enable'],
                speed_enable = form.changed_data['speed_enable'],
                where_enable = form.changed_data['where_enable'],

                lat = form.changed_data['lat'],
                lng = form.changed_data['lng'],
                radius = form.changed_data['radius'],
                speed = form.changed_data['speed'],
            )'''
            data = form.save()
            data.save()

            device_id = data.device_id
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            '''cursor.execute("""SELECT * FROM gpstracker WHERE DeviceId LIKE %s LIMIT 1""", ("%" + device_id + "%",))
            rows = cursor.fetchall()
            for row in rows:
                device_id = row[0]
                PORT = row[2]'''
            host = ''
            port  = 8900
            s.connect((host,port))
            notify = str(int(data.eng_notify))+str(int(data.ac_notify)) + str(int(data.door_notify)) +str(int(data.status_notify)) +str(int(data.fuel_notify)) +str(int(data.speed_notify)) +str(int(data.where_notify))
            alert = str(int(data.departure_alert))+str(int(data.eng_alert))+str(int(data.ac_alert)) + str(int(data.door_alert)) +str(int(data.arrival_alert)) +str(int(data.fuel_alert)) +str(int(data.speed_alert)) +str(int(data.radius_alert))
            alert_enable = str(int(data.departure_enable))+str(int(data.eng_enable))+str(int(data.ac_enable)) + str(int(data.door_enable)) +str(int(data.arrival_enable)) +str(int(data.fuel_enable)) +str(int(data.speed_enable)) +str(int(data.radius_enable))
            msg = 'b_reg:000' + ':' + str(data.device_id) + ':' + str(data.mobile_no) + ':'+ notify + '-' + alert+ '-' + alert_enable+':' + str(data.lat) + ':' + str(data.lng) + ':' + str(data.radius)+ ':' + str(data.speed)
            print msg
            s.sendall(msg)
            html = "created"
            print "created"
            return HttpResponseRedirect('/')
    else:
        form = Mobile_regForm()

    return render(request, "mobileReg.html",{'form':form})


