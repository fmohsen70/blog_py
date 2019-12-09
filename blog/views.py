from django.shortcuts import render,redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post,Product
from .forms import PostForm,ProForm



def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    products = Product.objects.all()
    # posts = Post.objects.get(title="sample")
    return render(request, 'blog/post_list.html', {'posts': posts,'products':products})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def pro_list(request):
    product = Product.objects.all()
    return render(request, 'blog/pro_list.html', {'product':product})    
def pro_new(request):
    if request.method == "POST":
        form = ProForm(request.POST)
        if form.is_valid():
            pro = form.save(commit=False)        
            pro.save()
            return redirect('pro_list')
    else:
        form = ProForm()    
    return render(request, 'blog/pro_edit.html', {'form': form})
def pro_edit(request, pk):
    pro = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ProForm(request.POST, instance=product)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.save()
            return redirect('pro_edit', pk=post.pk)
    else:
        form = ProForm(instance=post)
    return render(request, 'blog/pro_edit.html', {'form': form})