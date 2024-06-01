from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import UserProfile, Book, FilmType, Film, Company, Article, Album
from .serializers import UserProfileSerializer, BookSerializer, FilmSerializer, FilmTypeSerializer, BasicCompanySerializer, DetailedCompanySerializer, ArticleSerializer, AlbumSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from django.http import HttpResponse
# Create your views here.


class MyApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        age = data.get('age')

        return Response(f"Person data is this api is name{name} and age {age}")


class MyQueryApi(APIView):
    def post(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        location = request.query_params.get('location')

        return Response(f"this is query paramter in this request name is {name} and location {location}")


class MyParserApiView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            return Response({"message": "Received data and process is sucessfully", "data": data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': "Error Parsing data", "Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(user=request.user.id)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e))


class BookApiView(APIView):
    def get(self, request):
        book = Book.objects.all()
        book_serializer = BookSerializer(book, many=True)
        data = book_serializer.data
        return render(request, 'book_list.html', {'books': data})

    def post(self, request, *args, **kwargs):
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, *args, **kwargs):
        book = Book.objects.get(id=id)
        book_serializer = BookSerializer(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_200_OK)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response({'data': "this object is delete"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"message": "this data is not database"})


class MyRenderView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        data = {'message': 'Hello, world!'}
        return Response(data)


class FilmListCreateView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(id=1)  # Get the queryset of films
        serializer = self.get_serializer(
            queryset, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilmDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

# class CompanyDetailView(RetrieveAPIView):
#     queryset = Company.objects.all()

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return DetailedCompanySerializer
#         else:
#             return BasicCompanySerializer


class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.request.data.get('advanced', False):
            return DetailedCompanySerializer
        else:
            return BasicCompanySerializer


class PaginationMixin:
    pagination_class = PageNumberPagination
    page_size = 1


class CompanyListView(PaginationMixin, ListAPIView):
    queryset = Company.objects.all()
    serializer_class = DetailedCompanySerializer


class ArticleViewset(ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Article.objects.all()
        seralizer = ArticleSerializer(queryset, many=True)
        return Response(seralizer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        seralizer = ArticleSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, *args, **kwargs):
        try:
            queryset = Article.objects.get(id=pk)
            seralizer = ArticleSerializer(queryset)
            return Response(seralizer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=404)

    def update(self, request, pk, *args, **kwargs):
        queryset = Article.objects.get(id=pk)
        seralizer = ArticleSerializer(queryset, data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_200_OK)
        return Response(seralizer.error, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            queryset = Article.objects.get(pk=pk)
            queryset.delete()
            return Response(status=204)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=404)


class AlbumViewset(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=False, methods=['get'])
    def launch_date(self, request):
        queryset = Album.objects.filter(launch_date__gt="2023-12-12")
        seralizer = AlbumSerializer(queryset, many=True)
        return Response(seralizer.data, status=status.HTTP_200_OK)


def my_view(request):
    return HttpResponse("hello world")
