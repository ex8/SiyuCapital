from django.shortcuts import render, get_object_or_404
from newsletter.forms import RecipientForm, CommentForm
from django.contrib import messages
from newsletter.models import NewsLetter, Comment


def home(request):
    if request.method == 'POST':
        form = RecipientForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='You have been successfully added to the newsletter mailing list.')
        else:
            messages.error(request=request, message='Error adding recipient. Please try again.')
    else:
        form = RecipientForm()
    return render(request=request, template_name='newsy/index.html', context={'form': form})


def about(request):
    return render(request=request, template_name='newsy/about.html', context={})


def newsletter_list(request):
    newsletters = NewsLetter.objects.filter(published=True)
    return render(request=request, template_name='newsy/list.html', context={'newsletters': newsletters})


def newsletter_detail(request, id):
    newsletter = get_object_or_404(klass=NewsLetter, id=id)
    comments = Comment.objects.filter(newsletter=newsletter)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.newsletter = newsletter
            new_comment.save()
    else:
        form = CommentForm()
    return render(request=request, template_name='newsy/detail.html', context={'newsletter': newsletter,
                                                                                          'comments': comments,
                                                                                          'form': form})
