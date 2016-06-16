from django.shortcuts import render
from frmexp.models import Article
from django.http import HttpResponse
from frmexp.forms import ArticleForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('frmexp:create'))
    else:
        form = ArticleForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['article'] = Article.objects.all()
    #Article.refresh_from_db()

    return render(request, 'create.html', args)

def all(request):
    context = dict()
    context['article'] = Article.objects.all()
    #a= Article.objects.all()

    return render(request,'all.html',context)




#obj.refresh_from_db()
