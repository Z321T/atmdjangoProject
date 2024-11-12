# from django.utils.deprecation import MiddlewareMixin
#
#
# class HttpResponseCustomHeader(MiddlewareMixin):
#     def __init__(self, get_response):
#         super().__init__(get_response)
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         if 'System' not in response:
#             response['System'] = 'hunter/2.0.0'
#         return response
