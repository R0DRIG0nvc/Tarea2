from django.shortcuts import render, get_object_or_404
from basket.models import Player
from basket.forms import *
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse


def index(request):
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = 'player/list_player.html'
    return render(request, template_name, data)


def add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add_player.html'
    return render(request, template_name, data)


def list(request):
    if request.method == 'POST':
        get_object_or_404(Player, pk=request.POST['id']).delete()
        return JsonResponse({})
    data = {'players': Player.objects.all()}
    template_name = "player/listar.html"
    return render(request, template_name, data)


def edit(request, player_id):
    data = {}
    if request.POST:
        formPlayer = EditPlayerForm(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
    template_name = 'player/edit.html'
    data['player'] = EditPlayerForm(instance=Player.objects.get(pk=player_id))

    return render(request, template_name, data)
