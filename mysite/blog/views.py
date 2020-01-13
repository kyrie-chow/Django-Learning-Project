from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from .forms import Shared_form, CommentForm
from django.core.mail import send_mail



# Create your views here.
def show_blogs(request):
    articles = Article.objects.all()
    return render(request, "blog/post/list.html", {"posts": articles})


def blog_detail(request, year, month, day, post):

    get_article = get_object_or_404(Article, slug=post,
                                    status='published',
                                    publish__year=year,
                                    # publish__month=month,
                                    # publish__day=day,
                                    )

    comments = get_article.comment_article.filter(active=False)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)


        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = get_article
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, "blog/post/detail.html", {"post": get_article,
                                                     "comments": comments,
                                                     "new_comment": new_comment,
                                                     "comment_form": comment_form})


def article_share(request, article_id):
    article = get_object_or_404(Article, id=article_id, status='published')
    sent = False
    if request.method == 'POST':
        get_form = Shared_form(request.POST)
        post_url = request.build_absolute_uri(article.get_absolute_url())
        if get_form.is_valid():
            cd = get_form.cleaned_data
            subject = "{}(name) with {}(email) send you {}(title)".format(cd['name'], cd['send_email'], article.name)
            message = "{}(title) from {} with {}(comments)".format(article.name, post_url, cd['comments'])

            send_mail(subject, message, "m17788747725@163.com", [cd['to_email']])
            sent = True

    else:
        get_form = Shared_form()
    return render(request, "blog/post/share.html", {'post': article,
                                                    'form': get_form,
                                                    'sent': sent})






