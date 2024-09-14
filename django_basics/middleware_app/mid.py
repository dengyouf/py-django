from django.utils.deprecation import MiddlewareMixin

class FirstMiddleware(MiddlewareMixin):
    """
        处理请求对象，第一时间调用
        - return response 会调用 process_response 处理, 逆序调用
        - return None 调用下一个中间件的  process_request处理
    """
    def process_request(self, request):
        print("1. FirstMiddleware Processing request")
        
    def process_response(self, request, response):
        print("11. FirstMiddleware Processing response")
        return response
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("111. FirstMiddleware Processing view")

class SecondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("2. SecondMiddleware Processing request")
        # from django.http import HttpResponse
        # return HttpResponse("2. HttpResponse ....")
    def process_response(self, request, response):
        print("22. SecondMiddleware Processing response")
        
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("222. SecondMiddleware Processing view")

class ThreedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("3. ThreedMiddleware Processing request")
    def process_response(self, request, response):
        print("33. ThreedMiddleware Processing response")
        return response
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("333. ThreedMiddleware Processing view")