from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def writeReview(request):
    context = {'menu_class': 'menu-login'}
    return render(request, 'review/displayWriteReview.html', context)