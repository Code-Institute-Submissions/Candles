from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *

@login_required
def writeReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks')
    else:
        form = ReviewForm()
    context = {'form': form, 'menu_class': 'menu-login'}
    return render(request, 'review/displayWriteReview.html', context)