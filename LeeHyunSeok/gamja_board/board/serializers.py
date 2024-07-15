from rest_framework import serializers

from board.entity.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['boardId', 'boardName', 'boardcontent', 'boardWriter', 'regDate', 'updDate']
        read_only_fields = ['refDate', 'updDate']