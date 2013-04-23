from django.db import models
from django.contrib import admin
from django.forms import ModelForm

class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("dbe.blog.views.post", args=[pk]))
