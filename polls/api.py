from .models import Customer,Firstclass
from .serializers import CustomerSerializer,Firstclassserializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from data import Customer_data


class CustomerList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        l=[]
        for i in Customer_data["Customer"]["objects"]:
            l.append(i)
            return l
        
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)





class Firstclasslist(APIView):


    def get_object(self, pk):
        try:
            return Firstclass.objects.get(pk=pk)
        except Firstclass.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        snippets = Firstclass.objects.all()
        serializer = Firstclassserializer(snippets, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = Firstclassserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        firstclass = self.get_object(pk)
        serializer = Firstclassserializer(firstclass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        firstclass = self.get_object(pk)
        serializer = Firstclassserializer(firstclass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)