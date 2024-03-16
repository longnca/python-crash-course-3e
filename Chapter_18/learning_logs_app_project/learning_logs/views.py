from django.shortcuts import render

def index(request):
    """The home page for Learning Logs."""
    return render(request, 'learning_logs/index.html')
