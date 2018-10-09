from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120, blank=False)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s"%(self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural='Посты'
        ordering=['-created_date']


class Comment(models.Model):
    #without related_name = post.comment_set.all

    post = models.ForeignKey(Post, verbose_name='Post', related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name='name')
    text = models.TextField(max_length=500, verbose_name='text')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'комменты'

    def __str__(self):
        return "%s - %s"%(self.post, self.name)


