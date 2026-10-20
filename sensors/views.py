
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sensor
from .forms import SensorForm


def index(request):
    sensors = Sensor.objects.all() #查询数据库中所有传感器记录。

    context = {
        'sensors': sensors, #把查询结果传递给 HTML 模板。
    }

    return render(request, 'sensors/index.html', context) # 将模板和数据组合，生成 HTML 响应返回给浏览器。


def sensor_detail(request, sensor_id):
    sensor = get_object_or_404(Sensor, id=sensor_id)

    return render(request, 'sensors/detail.html', {
        'sensor': sensor,
    })


def sensor_create(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)

        if form.is_valid():
            sensor = form.save()
            return redirect('sensor_detail', sensor_id=sensor.id)
    else:
        form = SensorForm()

    return render(request, 'sensors/create.html', {
        'form': form,
    })
