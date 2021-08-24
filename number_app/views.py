from django.shortcuts import redirect, render
import random

# Create your views here.
def index (request):
    if 'random_num' not in request.session:
        request.session['random_num'] = int(random.random() * 10)
        request.session['guess_count'] = 0
        request.session['previous_nums'] = []
    print(request.session['guess_count'])
    print(request.session['previous_nums'])
    return render(request, 'index.html')

def process(request):
    request.session['guess_count'] += 1
    request.session['previous_nums'].append(request.POST['number'])
    if int(request.POST['number']) == request.session['random_num']:
        request.session['game_results'] = 'won'
        return redirect('/results')
    else:
        request.session['game_results'] = 'lost'
        return redirect('/results')

def results(request):
    return render(request, 'results.html')

def reset(request):
    request.session.flush()
    return redirect('/')