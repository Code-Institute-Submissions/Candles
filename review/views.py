from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.utils import timezone

@login_required
def writeReview(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.date = timezone.now() 
            new_review.save()

            context = {'form': new_review}
            return render(request, 'review/review_submitted.html', context)
    else:
        review_form = ReviewForm()
    context = {'form': review_form}
    return render(request, 'review/displayWriteReview.html', context)