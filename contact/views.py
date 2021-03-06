from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from contact.models import Contact
from contact.serializers import ContactSerializer


@api_view(['GET'])
def contacts(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True, context={'request':request})

    return Response(serializer.data)


@api_view(['GET'])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except:
        data = {'error':'this contact does not exists'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(contact, context={'request':request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def contact_create(request):
    contact = Contact(user=request.user)
    serializer = ContactSerializer(contact, data=request.data, context={'request':request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def contact_update(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except:
        data = {'error':'this contact does not exists'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.user != contact.user:
        return Response({'detail':'access denied'}, status=status.HTTP_403_FORBIDDEN)

    serializer = ContactSerializer(contact, data=request.data, context={'request':request})
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'successfuly updated'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def contact_delete(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except:
        data = {'error':'this contact does not exists'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    if request.user != contact.user:
        return Response({'detail':'access denied'}, status=status.HTTP_403_FORBIDDEN)

    operation = contact.delete()
    data = {}
    if operation:
        data['success'] = 'successfuly deleted'
    else:
        data['error'] = 'delete failed'
    return Response(data=data)
    