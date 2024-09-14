from django.shortcuts import render
from django.core.paginator import Page, Paginator

# Create your views here.

from django.views import View
from .models import Student

class studentView(View):
    def get(self, request):
        all_students = Student.objects.all()
        data = all_students
        return render(request, "student.html", {"data": data})
    

class studentPageView(View):


    def get(self, request):
        """
        pnum = 当前页
        psize = 每页数量
        """
        pnum = request.GET.get('pnum', 1)
        psize = request.GET.get('psize', 10)
        all_students = Student.objects.all()    

        paginator = Paginator(all_students, psize, 5)

        data = paginator.get_page(pnum)
        page_range = self.get_range_list(data.number, paginator.num_pages)
        print(page_range)
        return render(request, "student_page.html", {"data": data, "page_range": page_range})
    
    
    def get_range_list( self, page, max_page, num=9):
        """
        num: 列表个数
        """
        min = page-int(num/2)
        min = min if min > 1 else 1
        max = min + num - 1
        max = max if max < max_page else max_page
    
        return range(min, max + 1)
      