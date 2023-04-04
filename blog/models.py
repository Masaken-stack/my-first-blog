from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ユーザーが投稿した記事を表すモデル。

    このモデルは、ユーザーが投稿した記事を保存するために使用されます。

    Attributes:
        author (ForeignKey): 投稿を作成したユーザーを表すForeignKeyフィールド。
        title (CharField): 記事のタイトルを表すCharFieldフィールド。
        text (TextField): 記事の本文を表すTextFieldフィールド。
        created_date (DateTimeField): 記事の作成日を表すDateTimeFieldフィールド。
        published_date (DateTimeField): 記事が公開された日を表すDateTimeFieldフィールド。
        
    Methods:
        publish: 記事を公開するためのメソッド。
        __str__: 記事のタイトルを返すためのメソッド。
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) -> None:
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title