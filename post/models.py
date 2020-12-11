from django.db import models
import datetime





# Create your models here.

class Tag(models.Model):
    # posting_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_content = models.CharField(max_length=30)

# 게시글
class Post(models.Model):
    # 글아이디는 자동생성
    posting_writer = models.ForeignKey('member.MyUser', on_delete=models.CASCADE)
    # posting_writer = models.CharField(max_length=30)
    posting_photo = models.ImageField(upload_to='images')
    posting_content = models.TextField()
    # posting_like = models.IntegerField()
    posting_date = models.DateTimeField(default=datetime.datetime.now)

    like_user = models.ManyToManyField('member.MyUser', related_name="like_user") # 포스트는 여러 유저를 갖는다.

    tagging = models.ManyToManyField(Tag, related_name='tagged', blank=True)

    @property
    def like_count(self):
        return self.like_user.count()


    # def tag_save(self):
    #     tags = re.findall(r'#(\w+)\b', self.posting_content)
    #
    #     if not tags:
    #         return
    #
    #     for t in tags:
    #         tag, tag_created = Tag.objects.get_or_create(tag_content=t)
    #         self.tagging.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가



# 댓글
class Reply(models.Model):
    posting_id = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='posting_id')
    reply_writer = models.CharField(max_length=30)
    reply_content = models.TextField()
    reply_date = models.DateTimeField(default=datetime.datetime.now)
    reply_like = models.IntegerField(default=0)
    reply_date = models.DateTimeField(default=datetime.datetime.now)
