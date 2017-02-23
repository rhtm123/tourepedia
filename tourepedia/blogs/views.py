from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from subscribe.forms import SubscribeForm

from blogs.models import Title, Detail, TagForBlog


def index(request):

    title_list = Title.objects.all().order_by('-pub_date')
    paginator = Paginator(title_list, 12)

    page = request.GET.get('page')
    try:
        titles = paginator.page(page)
    except PageNotAnInteger :
        titles = paginator.page(1)
    except EmptyPage :
        titles = paginator.page(paginator.num_pages)


    nav_tips = Title.objects.filter(blog_type='tips')[:4]
    nav_tales = Title.objects.filter(blog_type='stories')[:4]
    nav_inspireds = Title.objects.filter(blog_type='inspired')[:4]
    nav_photoblogs = Title.objects.filter(blog_type='photoblog')[:4]

    context_dict = {}
    context_dict['nav_tips'] = nav_tips
    context_dict['nav_tales'] = nav_tales
    context_dict['nav_inspireds'] = nav_inspireds
    context_dict['nav_photoblogs'] = nav_photoblogs


    context_dict['titles'] = titles

    return render(request, 'blogs/blog_home.html', context_dict)

def inspired_index(request):

    inspired_titles= Title.objects.filter(blog_type='inspired')

    paginator = Paginator(inspired_titles, 12)

    page = request.GET.get('page')
    try:
        titles = paginator.page(page)
    except PageNotAnInteger :
        titles = paginator.page(1)
    except EmptyPage :
        titles = paginator.page(paginator.num_pages)

    nav_tips = Title.objects.filter(blog_type='tips')[:4]
    nav_tales = Title.objects.filter(blog_type='stories')[:4]
    nav_inspireds = Title.objects.filter(blog_type='inspired')[:4]
    nav_photoblogs = Title.objects.filter(blog_type='photoblog')[:4]

    context_dict = {}
    context_dict['nav_tips'] = nav_tips
    context_dict['nav_tales'] = nav_tales
    context_dict['nav_inspireds'] = nav_inspireds
    context_dict['nav_photoblogs'] = nav_photoblogs

    context_dict['titles']= titles

    return render(request, 'blogs/cat_inspired.html', context_dict)

def photoblog_index(request):

    photoblog_titles = Title.objects.filter(blog_type="photoblog")

    paginator = Paginator(photoblog_titles, 12)

    page = request.GET.get('page')
    try:
        titles = paginator.page(page)
    except PageNotAnInteger :
        titles = paginator.page(1)
    except EmptyPage :
        titles = paginator.page(paginator.num_pages)



    nav_tips = Title.objects.filter(blog_type='tips')[:4]
    nav_tales = Title.objects.filter(blog_type='stories')[:4]
    nav_inspireds = Title.objects.filter(blog_type='inspired')[:4]
    nav_photoblogs = Title.objects.filter(blog_type='photoblog')[:4]

    context_dict = {}
    context_dict['nav_tips'] = nav_tips
    context_dict['nav_tales'] = nav_tales
    context_dict['nav_inspireds'] = nav_inspireds
    context_dict['nav_photoblogs'] = nav_photoblogs

    context_dict['titles']= titles


    return render(request, 'blogs/cat_photograph.html', context_dict)

def traveltip_index(request):

    tip_titles = Title.objects.filter(blog_type="tips")

    paginator = Paginator(tip_titles, 12)

    page = request.GET.get('page')
    try:
        titles = paginator.page(page)
    except PageNotAnInteger :
        titles = paginator.page(1)
    except EmptyPage :
        titles = paginator.page(paginator.num_pages)

    nav_tips = Title.objects.filter(blog_type='tips')[:4]
    nav_tales = Title.objects.filter(blog_type='stories')[:4]
    nav_inspireds = Title.objects.filter(blog_type='inspired')[:4]
    nav_photoblogs = Title.objects.filter(blog_type='photoblog')[:4]

    context_dict = {}
    context_dict['nav_tips'] = nav_tips
    context_dict['nav_tales'] = nav_tales
    context_dict['nav_inspireds'] = nav_inspireds
    context_dict['nav_photoblogs'] = nav_photoblogs

    context_dict['titles']= titles


    return render(request, 'blogs/cat_tip.html', context_dict)

def tales_index(request):

    story_titles= Title.objects.filter(blog_type="stories")

    paginator = Paginator(story_titles, 12)

    page = request.GET.get('page')
    try:
        titles = paginator.page(page)
    except PageNotAnInteger :
        titles = paginator.page(1)
    except EmptyPage :
        titles = paginator.page(paginator.num_pages)


    nav_tips = Title.objects.filter(blog_type='tips')[:4]
    nav_tales = Title.objects.filter(blog_type='stories')[:4]
    nav_inspireds = Title.objects.filter(blog_type='inspired')[:4]
    nav_photoblogs = Title.objects.filter(blog_type='photoblog')[:4]

    context_dict = {}
    context_dict['nav_tips'] = nav_tips
    context_dict['nav_tales'] = nav_tales
    context_dict['nav_inspireds'] = nav_inspireds
    context_dict['nav_photoblogs'] = nav_photoblogs

    context_dict['titles']= titles
    
    return render(request, 'blogs/cat_tale.html', context_dict)
    

def detail(request, slug):

    subscribed = False

    if request.method == 'POST':

        subscribe_form = SubscribeForm(data=request.POST)

        if subscribe_form.is_valid():
            subscribe= subscribe_form.save(commit=False)
        
            subscribe.save()
                       
            subscribed = True
    else:
        subscribe_form = SubscribeForm()

    context_dict = {}

    try:
        
        title = Title.objects.get(slug=slug)

        details = Detail.objects.filter(title=title)

        context_dict['details'] = details
        context_dict['title'] = title
        context_dict['subscribed'] = subscribed

        context_dict['subscribe_form'] = subscribe_form

        #tagforblog = TagForBlog.objects.get(title=title)

        related_titles = Title.objects.exclude(slug=slug).filter(blog_type=title.blog_type).order_by('pub_date')[:6]

        related_titles_by_author = Title.objects.exclude(slug=slug).filter(publisher=title.publisher).order_by('-pub_date')[:3]

        context_dict['related_titles'] = related_titles

        context_dict['related_titles_by_author'] = related_titles_by_author

        nav_tips = Title.objects.filter(blog_type='tips')[:4]
        nav_tales = Title.objects.filter(blog_type='stories')[:4]
        nav_inspireds = Title.objects.filter(blog_type='inspired')[:4]
        nav_photoblogs = Title.objects.filter(blog_type='photoblog')[:4]

        context_dict['nav_tips'] = nav_tips
        context_dict['nav_tales'] = nav_tales
        context_dict['nav_inspireds'] = nav_inspireds
        context_dict['nav_photoblogs'] = nav_photoblogs

    except Title.DoesNotExist:
        raise Http404("Page does not exist")

    return render(request, 'blogs/blog_detail.html', context_dict)

