from playsound import playsound
def play_sound(result):
    # path = r'C:\Users\PGTB84\workspace_codecool\ideabank\TicTacToe\tic-tac-toe-python-Runnes\Battleships'
    # path_win = path + "\win.mp3"
    # path_miss = path + "miss.mp3"

    if result == "win":
        playsound("win2.mp3")
    if result == "miss":
        playsound('miss.mp3')
    if result == "hit":
        playsound('hit.mp3')
    if result == "gamemusic":
        playsound('gamemusic.mp3')


# ###Epic Cinematic Trailer | ELITE by Alex-Productions | https://www.youtube.com/channel/UCx0_M61F81Nfb-BRXE-SeVA
# Music promoted by https://www.chosic.com/free-music/all/
# Creative Commons CC BY 3.0
# https://creativecommons.org/licenses/by/3.0/###