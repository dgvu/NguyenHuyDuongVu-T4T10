
from pyglet.media import Source, Player, loady
def play_options(choice,player):
    
    if choice == 'play':
        player.play()
    elif choice == 'pause':
        player.pause()
    elif choice == 'stop':
        player.delete()
        player = False
    else:
        print("Sorry, your command is Invalid") 