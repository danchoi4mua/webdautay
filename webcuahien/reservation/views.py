from django.shortcuts import render
from .models import Tuyen_Dung





# Create your views here.
    
def tuyedung(request):
    congviec = Tuyen_Dung.objects.all()
    # Giả sử bạn muốn lấy một đối tượng cụ thể, ví dụ, lấy cái đầu tiên trong danh sách
    vieccantuyen = Tuyen_Dung.objects.first()  # hoặc bạn có thể dùng Tuyen_Dung.objects.get(pk=pk) nếu có pk cụ thể
    return render(request, 'templates_reservation/templates_reservation.html', {
        "congvieccantuyen": congviec,
        "vieccantuyen": vieccantuyen  # Thêm vieccantuyen vào context
    })

def congviec(request,pk):
    vieccantuyen =Tuyen_Dung.objects.get(pk=pk)
    return render(request, 'templates_reservation/reservation_viec.html',{"vieccantuyen" : vieccantuyen})