from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Product
from .forms import PostForm,ProForm
from django.contrib.auth import authenticate, login,logout





def home(request):
    if request.user.is_authenticated:
        return render(request,'blog/home.html')    
    else:
        return redirect('login') 
def check_login(request):
    if request.user.is_authenticated:
        return render(request,'blog/home.html')    
    else:
        return redirect('login')        
 
def logins(request):
    # return render(request,'blog/login.html')  
     if request.method == "POST":  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'blog/home.html')            
        else:
            return redirect('login')    
     else:
        return render(request, 'blog/login.html')
def log_out(request):
    logout(request)
    return redirect('home')       

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

def user_gains_perms(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permissions
    user.has_perm('blog.Post')

    content_type = ContentType.objects.get_for_model(Post)
    permission = Permission.objects.get(
        codename='change_blogpost',
        content_type=content_type,
    )
    user.user_permissions.add(permission)

    # Checking the cached permission set
    user.has_perm('blog.Post')  # False

    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache.
    user = get_object_or_404(User, pk=user_id)

    # Permission cache is repopulated from the database
    user.has_perm('blog.Post')  # True


    
  