from game.scrabble import (ScrabbleGame, 
                           WordDoesntFitOnBoardException,
                           UserDoesntHaveTilesException, 
                           WordEntersInConflictWithOtherWordsException,
                           WordIsNotNewException,
                           WordIsNotConnectedException,
                           WordIsNotInDictionaryException,
                           wordDoesntPassesByTheCenterException,
                           WordCreatesNonValidWordsWithTheExistingOnes)
from game.player import Player
from game.board import Board
from game.cell import Cell
from game.models import Tile
from game.tools import Tools
from colorama import Fore, Back, Style
from unidecode import unidecode
import os 

class TilesException(Exception):
    pass

os.system('clear')

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

while True: 
    try:
        numPlayers = int(input('Select the number of players: '))
        if numPlayers > 1 and numPlayers < 5:
            break
        else:
            print ('Please select a minimum of 2 players and maximum of 4 players.')
            continue
    except ValueError:
        print ('Error! Please select a valid number of players.')


game = ScrabbleGame(numPlayers)
game_status = True

game.players[0].tiles = [Tile('D', 1), Tile('A', 1), Tile('D', 1), Tile('O', 1), Tile('S', 1), Tile('O', 1), Tile('L', 1)]
    
os.system('clear')
while game_status == True:
    main_menu()
    print ('')
    print ('Choose an option: ')
    print ('                    A- Exchange Tiles   B- Put word   C- Shuffle   D - Skip Turn   E - End Game')
    while True:
        option = input('').upper()
        if option == 'A' or option == 'B' or option == 'C' or option == 'D' or option == 'E' or option == '':
            break
        else:
            print ('Error! Please, choose a valid option: ')
            
    if option == 'A':
        while True:
            try:
                tiles = input('Type the positions of the tiles you want to exchange: ').split(',')
                tiles = [int(tile) for tile in tiles]
                if not all(0 < tile <= 7 for tile in tiles):
                    raise ValueError('Invalid tile position')
                break
            except ValueError as e:
                 print('Error! Please enter valid tile positions between 1 and 7.')
        player = game.players[game.turn]
        tilesToExchange = [int(x) - 1 for x in tiles]
        player.exchange(tilesToExchange)
        print(player.tiles)
        game.turn += 1
        os.system('clear')
        
    elif option == 'B':
        while True:
            word = input('Type the word you want to put: ').upper()
            if not word.isalpha():
                print('Error! Please write a valid word.')
            else:
                break
        while True:
            try:
                N = int(input('Row: '))
                M = int(input('Column: '))
                break
            except:
                print('Error! please type a valid number.')
        while True:
            Orientation = input("Orientation ('H' or 'V'):" ).upper()
            if Orientation == 'H' or Orientation == 'V':
                break
            else:
                print('Error! Please type a valid orientation.')
        os.system('clear')
        try:
            game.validate_and_put_word(word,[N,M], Orientation)
        except UserDoesntHaveTilesException as e:
            print(e)
        except WordIsNotNewException as e:
            print(e)
        except WordDoesntFitOnBoardException as e:
            print(e)
        except WordIsNotConnectedException as e:
            print(e)
        except WordEntersInConflictWithOtherWordsException as e:
            print(e)
        except wordDoesntPassesByTheCenterException as e:
            print(e)
        except WordIsNotInDictionaryException as e:
            print(e)
        except WordCreatesNonValidWordsWithTheExistingOnes as e:
            print(e)

    elif option == 'C':
        game.players[game.turn].shuffle_tiles()
        os.system('clear')

    elif option == 'D' or option == '':
        game.next_turn()
        os.system('clear')

    elif option == 'E':
        maxValue = 0
        winner = None
        os.system('clear')
        for i in game.players:
            print('Player', game.players.index(i)+1, 'score:', i.score, 'points')
            if maxValue < i.score:
                winner = game.players.index(i) + 1
                maxValue = i.score
        
        
        separator()
        print ('                                The winner is player', winner, 'with', maxValue, 'points!')
        separator()
        game_status = False

    else:
        game.next_turn()
        os.system('clear')


