from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task


@api_view(['GET', 'POST'])
def apiTest(request):

    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/', 
    }
    return Response(api_urls)   






@api_view(['GET'])
def taskList(request):

    #current_user = request.user
    #current_user.id
    task = Task.objects.filter(author = request.user).order_by('-id')
    serializer = TaskSerializer(task, many = True)
    return Response(serializer.data)






@api_view(['POST'])
def taskSearch(request):

    search_text = request.data['search']
    task = Task.objects.filter(description__contains= search_text).order_by('-id')
    serializer = TaskSerializer(task, many = True)
    return Response(serializer.data)






@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.filter(author = request.user.id ,id = pk).order_by('-id')
    #task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)






@api_view(['POST'])
def taskCreate(request):
    
    author = request.user.id
    request.data.update({ "author": author })
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    # else:
        # print(request.data)
        # print ("SERLIALIZER NO VALIDO EN taskCreate..................")
    return Response(serializer.data)






@api_view(['POST'])
def taskUpdate(request, pk):
    
    task = Task.objects.get(author = request.user, id = pk)
    
    author = request.user.id
    request.data.update({ "author": author })
    serializer = TaskSerializer(instance = task, data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        print(request.data)
        print ("SERLIALIZER NO VALIDO EN taskUpdate..................")
    
    return Response(serializer.data)





@api_view(['DELETE'])
def taskDelete(request, pk):
    
    task = Task.objects.get(author = request.user,id = pk)
    task.delete()

    return Response("borrado")