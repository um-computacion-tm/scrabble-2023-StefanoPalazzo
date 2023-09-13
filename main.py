from game.scrabble import ScrabbleGame
from game.player import Player
from game.board import Board
from game.cell import Cell
from game.models import Tile
from game.tools import Tools
from colorama import Fore, Back, Style

def separator():
    print ('''______________________________________________________________________________________________________
           ''')
    
def player_tiles():
    print ('')
    print ('Player', game.turn+1, 'tiles:')
    tiles = []
    for i in game.players[game.turn].tiles:
        tiles.append(i.letter)
    print ('                   ' , tiles)


def main_menu():
    separator()
    print ('Tiles in Bag:', len(game.bag_tiles.tiles),'                         ', Back.CYAN + 'Player', game.turn+1, 'turn' + Style.RESET_ALL, '                       ', "Player's score:", Fore.GREEN + str(game.players[game.turn].score) + Fore.WHITE )
    separator()
    game.board.show_board()
    player_tiles()



welcomeText = f"         {Fore.RED}W{Fore.GREEN}E{Fore.YELLOW}L{Fore.BLUE}C{Fore.MAGENTA}O{Fore.CYAN}M{Fore.WHITE}E {Fore.RED}T{Fore.GREEN}O {Fore.YELLOW}S{Fore.BLUE}C{Fore.MAGENTA}R{Fore.CYAN}A{Fore.WHITE}B{Fore.RED}B{Fore.GREEN}L{Fore.YELLOW}E{Fore.RED}G{Fore.GREEN}A{Fore.YELLOW}M{Fore.BLUE}E{Fore.MAGENTA}{Fore.BLUE}!{Style.RESET_ALL}"

print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(welcomeText)
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
numPlayers = int(input('Select the number of players: '))
game = ScrabbleGame(numPlayers)
game_status = True
    

while game_status == True:
    main_menu()
    print ('')
    print ('Choose an option: ')
    print ('                    A- Exchange Tiles   B- Put word   C- Shuffle   D - Surrender')
    option = input ()
    if option.upper() == 'C':
        game.players[game.turn].shuffle_tiles()
    if option.upper() == 'D':
        game_status = False
    else:
        game.next_turn()

