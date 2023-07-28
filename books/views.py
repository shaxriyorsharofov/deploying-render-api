from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView, ListAPIView, get_object_or_404
from rest_framework.views import APIView
from books.models import Books
from books.serializers import BookSerializers
from rest_framework.response import Response

# Create your views here.


class ListView(APIView):
    def get(self, request):
        book = Books.objects.all()
        serializer_data = BookSerializers(book, many=True).data
        data = {
            'status': '200 ok',
            'kitoblar': serializer_data
        }
        return Response(data)


class DetailView(APIView):
    def get(self, request, pk):
        book =  get_object_or_404(Books.objects.all(), id=pk)
        serializer_data = BookSerializers(book).data
        data = {
            'status': True,
            'message': serializer_data
        }
        return Response(data)


class CreateView(APIView):
    def post(self, request):
        data = request.data
        serializer_data = BookSerializers(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            data = {
                'status': True,
                'message': 'Succesfully created!'
            }
            return Response(data)
        else:
            return Response({
                "status": False,
                "message": "Xato malumot kiritdingiz"
            })


class UpdateView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Books.objects.all(), id=pk)
        data =request.data
        serializer_data = BookSerializers(instance=book, data=data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
                serializer_data.save()
        return Response({
            'status': True,
            'message': 'Succesfully updated'
        })


class DeleteView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Books.objects.all(), id=pk)
        book.delete()
        return Response({
            'status': True,
            'message': 'Succesfully deleted'
        })



# class BookReviewViewSets(viewsets.ModelViewSet):
#     serializer_class = BookSerializers
#     queryset = Books.objects.all()
#     lookup_field = 'pk'




# class BookListCreateView(ListCreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookListView(ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookDetailView(RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookDeleteView(DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookUpdateView(UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers
#
#
# class BookCreateView(CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializers



