from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank = True, null = True)

    def __str__(self):  # override
        return self.title

    def summary(self):  # 요약해주는 메서드 - 본문 100자
        return self.body[:100]
