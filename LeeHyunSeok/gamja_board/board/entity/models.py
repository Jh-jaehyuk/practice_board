from django.db import models

# Create your models here.

class Board(models.Model):
    boardId = models.AutoField(primary_key=True)
    boardName = models.CharField(max_length=128, null=False)
    boardcontent =models.TextField()
    boardWriter = models.CharField(max_length=32, null=False)
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)


    def __str__(self):      # board 객체를 print찍으면 어떤 것들이 나오면 좋겠는지 return에 넣는 항목에 넣음. (디버깅용)
        return f"boardId: {self.boardId}, boardName: {self.boardName}"


    class Meta:
        db_table ='board'