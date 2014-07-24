from django.forms import widgets
from rest_framework import serializers, pagination
from .models import Chapter, Member


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter


class MemberSerializer(serializers.ModelSerializer):
    photos = serializers.Field(source='get_photos')

    class Meta:
        model = Member
        fields = ('first_name', 'last_name',
                  'work', 'school',
                  'graduation_year',
                  'facebook', 'twitter',
                  'chapter',
                  'photos')


class PaginatedChapterSerializer(pagination.PaginationSerializer):

    class Meta:
        object_serializer_class = ChapterSerializer


class PaginatedMemberSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = MemberSerializer


class RandomMemberSerializer(serializers.ModelSerializer):
    full_name = serializers.Field(source='get_fullname')
    photo = serializers.Field(source='get_random_photo')
    fake_names = serializers.Field(source='get_fakename')

    class Meta:
        model = Member
        fields = ('id', 'full_name', 'photo', 'fake_names')
