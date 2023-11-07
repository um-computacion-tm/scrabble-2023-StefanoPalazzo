from game.scrabble import (ScrabbleGame, 
                           WordDoesntFitOnBoardException,
                           UserDoesntHaveTilesException, 
                           WordEntersInConflictWithOtherWordsException,
                           WordIsNotNewException,
                           WordIsNotConnectedException,
                           WordIsNotInDictionaryException,
                           wordDoesntPassesByTheCenterException,
                           WordCreatesNonValidWordsWithTheExistingOnes,
                           UserDoesntHaveConnection)
from game.player import Player
from game.board import Board
from game.cell import Cell
from game.models import Tile
from game.tools import Tools
from colorama import Fore, Back, Style
from unidecode import unidecode
import os 


class ScrabbleCli():
    def initial_menu(self):
            # os.system('clear')

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
                except ValueError as e:
                    print ('Error! Please select a valid number of players.')
                    
            return numPlayers
    
    def choose_option(self):
        print ('')
        print ('Choose an option: ')
        print ('                    A- Exchange Tiles   B- Put word   C- Shuffle   D - Skip Turn   E - End Game')
        while True:
            option = input('').upper()
            if option in ['A', 'B', 'C', 'D', 'E', '']:
                break
            else:
                print ('Error! Please, choose a valid option: ')
        return option
    
    def option_A(self, game):
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
        game.next_turn()
        os.system('clear')

    def option_B(self, game):
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
        location = [N, M]
        self.put_word_and_exceptions(game, word, location, Orientation)
    
    def put_word_and_exceptions(self, game,word, location, orientation): 
        try:
            game.validate_and_put_word(word,location, orientation)
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
        except UserDoesntHaveConnection as e:
            print(e)
        except WordCreatesNonValidWordsWithTheExistingOnes as e:
            print(e)
        

    def option_E(self,game):
        maxValue = 0
        winner = None
        os.system('clear')
        for i in game.players:
            print('Player', game.players.index(i)+1, 'score:', i.score, 'points')
            if maxValue < i.score:
                winner = game.players.index(i) + 1
                maxValue = i.score
        Tools().separator()
        print ('                                The winner is player', winner, 'with', maxValue, 'points!')
        Tools().separator()
 
            


    def __init__(self): 
        game_status = True
        while game_status:
            numPlayers = self.initial_menu()

            game = ScrabbleGame(numPlayers)

            game_status = True

            os.system('clear')
            while game_status == True:
                game.main_menu()
                option = self.choose_option()

                if option == 'A':
                    self.option_A(game)

                elif option == 'B':  
                    self.option_B(game)

                elif option == 'C':
                    game.players[game.turn].shuffle_tiles()
                    os.system('clear')

                elif option == 'D' or option == '':
                    game.next_turn()
                    os.system('clear')

                elif option == 'E':
                    self.option_E(game)
                    game_status = False

                    
                else:
                    game.next_turn()
                    os.system('clear')
        
        