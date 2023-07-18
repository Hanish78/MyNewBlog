from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogContent
from .forms import TestForm
from .forms import ModelsDemoForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    obj=BlogContent.objects.all()
    context={'data':obj}
    return render (request, 'blogs.html',context)

def addBlogPage(request):
    return render(request, 'add_blog.html')

def addBlogHandler(request):
    if request.GET.get('name'):
        title_r = request.GET.get('name')
        description_r = request.GET.get('description')
        author_r = request.user
        no_of_line_r = request.GET.get('no_of_line')

        obj = BlogContent(title = title_r, description = description_r, author = author_r, no_of_line = no_of_line_r)
        obj.save()
        return render (request, 'add_blog.html',{'response':'Saved Successfuly'})
    
    else:
        return render (request, 'add_blog.html',{'response':'Fill details'})    

def delBlogPage(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
        obj = BlogContent.objects.get(pk=id)
        obj.delete()
        return render (request, 'add_blog.html',{'response1':'Delete Successfuly'})
    
    else:
        return render (request, 'add_blog.html',{'response1':'Fill details'})
    
def create_form(request):

    form = TestForm()
    return render(request, "testform.html", {'form': form}) 

def ModelsForm(request):
    success = ''
    form = ModelsDemoForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        success = 'data saved Successfully'
    # add the dictionary during initialization
    context = {'form': form, 'success': success}
    return render(request, "ModelsForm.html", context)

def deleteblog(request, id):
    BlogContent.objects.get(pk=id).delete()
    success = 'Successfully deleted Item'
    return render(request, 'blogs.html', {'success': success})

def updateblog(request, id):
    obj = BlogContent.objects.get(id = id)
    return render(request, 'update.html', {"info":obj})

def updatedata(request, id):
    success = ''
    c_id = id
    c_title = request.POST.get('name')
    c_description = request.POST.get('description')
    c_author = request.POST.get('author')
    c_no_of_line = request.POST.get('no_of_line')

    obj = get_object_or_404(BlogContent, id = c_id)
    obj.title = c_title
    obj.description = c_description
    obj.author = c_author
    obj.no_of_line = c_no_of_line

    obj.save()
    success = f"{c_id} - Successfully Updated"

    return render(request, 'blogs.html', {'success':success})




    