from django.db import models

# Create your models here.
class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 1. Models.py 작성/수정
# 2. python manage.py makemigrations #=> models.py
#    바탕으로 설계도 생성
# 3. python manage.py migrate
#    # => DB(db.sqlite3)에 설계도를 적용 (테이블 생성)

# DB에 데이터를 생성하는 방법 3가지
# 1. article = Article()
#    article.title = '제목'
#    article.content = '내용'
#    article.save()

# 2. article2 = Article(title='', content='')
#    article2.save()

# 3. article = Article.objects.create(title='제목3',content='내용3')

# Read
# all = > Article.objects.all()[1:3]


# Update
# 1. 데이터 가져오기 -a = Article.objects.get(id=1)
# 2. 수정할 값 할당하기 - a.title = 'first!'
# 3. 저장하기 (DB에 반영하기) -a.save()

# Delete
# 1. 데이터 가져오기 - a = Article.objects.get(id=1)
# 2.삭제하기 (DB에 반영) - a.delete()



