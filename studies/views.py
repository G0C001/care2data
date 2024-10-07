from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm

def index(request):
    studies = Study.objects.all()
    return render(request, 'index.html', {'studies': studies})

def add_study(request):
    form = StudyForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            return redirect('index')
        except Exception as e:
            return render(request, 'add_study.html', {'form': form, 'error': str(e)})
    return render(request, 'add_study.html', {'form': form})

def view_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    return render(request, 'view_study.html', {'study': study})

def edit_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    form = StudyForm(request.POST or None, instance=study)
    if form.is_valid():
        try:
            form.save()
            return redirect('index')
        except Exception as e:
            return render(request, 'edit_study.html', {'form': form, 'error': str(e)})
    return render(request, 'edit_study.html', {'form': form})
    
def delete_study(request):
    if request.method == 'POST':
        study_ids = request.POST.getlist('study_ids')
        if study_ids:
            Study.objects.filter(id__in=study_ids).delete()
    return redirect('index')
