from django.shortcuts import render

swords = [
    {'name': 'Excalibur', 'legend': 'Soul Eater', 'description': 'Sentient legendary sword of legend', 'firstSeen': 'Season 1, Episode 9'},
    {'name': 'Enma', 'legend': 'One Piece', 'description': 'The sword of the King of Hell', 'firstSeen': 'Season 20, Episode 16'},
    {'name': 'Master Sword', 'legend': 'Legend of Zelda', 'description': 'Divine magic sword aka Sword of Resurrection', 'firstSeen': 'Legend of Zelda: Link to the Past (1991)'},
    {'name': 'Kusanagi', 'legend': 'Naruto', 'description': 'legendary Japanese sword that is said to have been possessed by the god of war, Susanoo', 'firstSeen': 'Episode 51'},
    {'name': 'Longclaw', 'legend': 'Game Of Thrones', 'description': 'Valyrian steel bastard sword that was the ancestral weapon of House Mormont', 'firstSeen': 'Season 1, Episode 6'},
    {'name': 'Wado Ichimonji', 'legend': 'One Piece', 'description': 'One of the 21 Great Grade swords', 'firstSeen': 'Season 1, Episode 2'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def swords_index(request):
    return render(request, 'swords/index.html', {
        'swords': swords
    })