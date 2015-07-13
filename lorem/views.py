from django.shortcuts import render

def post_list(request):
    return render(request, 'lorem/post_list.html',{})
