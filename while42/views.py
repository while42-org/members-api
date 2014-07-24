from .models import Member, Chapter
from .serializers import MemberSerializer, ChapterSerializer, \
    RandomMemberSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(APIView):
    """ detail of 1 single member """
    @staticmethod
    def get_object(pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)


class ChapterList(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    paginate_by = None


class ChapterDetail(generics.ListAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            chapter = Chapter.objects.get(pk=pk)
            return Member.objects.filter(chapter__in=str(chapter.pk))
        except Chapter.DoesNotExist:
            raise Http404


class RandomMember(generics.ListAPIView):
    serializer_class = RandomMemberSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            chapter = Chapter.objects.get(pk=pk)
            return Member.objects.filter(chapter__in=
                                         str(chapter.pk)).order_by('?')[:10]
        except Chapter.DoesNotExist:
             raise Http404