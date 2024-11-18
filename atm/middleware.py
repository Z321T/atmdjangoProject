# middleware.py

from django.http import HttpResponse


class PreflightMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 检查是否是OPTIONS请求
        if request.method == 'OPTIONS':
            # 创建一个空的HttpResponse对象
            response = HttpResponse(status=200)
            # 设置CORS相关的头部
            response['Access-Control-Allow-Origin'] = ' http://localhost:5174'  # 允许的源
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'  # 允许的方法
            response['Access-Control-Allow-Headers'] = ('Origin, X-Requested-With, Content-Type, Accept, '
                                                        'Authorization, Authentication')
            response['Access-Control-Allow-Credentials'] = 'true'
            return response
        else:
            # 对于非OPTIONS请求，调用下一个中间件或视图
            response = self.get_response(request)
            return response
