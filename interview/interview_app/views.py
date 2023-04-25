
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class InterviewView(APIView):
    def get(self, request, format=None):
        """
        1. 取得特定company的customers
        2. 取得特定last_name的customers
        """
        pass

    def post(self, request, format=None):
        """
        建立新customer
        """
        pass

    def put(self, request, format=None):
        """
        更新現有customer
        """
        pass

    def delete(self, request, format=None):
        """
        刪除特定customer
        """
        pass
