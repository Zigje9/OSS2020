from rest_framework import serializers

from vuenote.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('memo', 'latitudes', 'longitudes', 'created')
