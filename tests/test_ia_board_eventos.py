import unittest
import ia_board_eventos
import tablero

class test_tablero_black_pieces(unittest.TestCase):
    def setUp(self):
        self.juego = tablero.game(True)
        self.juego.board = [
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['r', 'r', 'h', 'h', 'b', 'b', 'q', 'Q', 'k', 'k', 'b', 'b', 'h', 'h', 'r', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['k', 'k', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'k'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'R', 'H', 'H', 'B', 'q', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R'],
            ['R', 'R', 'H', 'H', 'B', 'B', 'Q', 'Q', 'K', 'K', 'B', 'B', 'H', 'H', 'R', 'R']]
        
        change=0                                                       
        self.moves       = self.juego.get_All_Possible_Moves(change)      
                
        change=1                                                       
        self.moves_enemy = self.juego.get_All_Possible_Moves(change) 


    def test_clasificacion(self):
    
        analisis_expected = [   ['-', '-', '-', '-', '-', '-', '?', '?', '?', '-', '-', '-', '-', '-', '-', '-'],
                                ['-', '-', '-', '-', '-', '-', '?', '&&', '?', '-', '-', '-', '-', '-', '-', '-'],
                                ['-', '-', '-', '-', '-', '-', '?', '?', '?', '-', '-', '-', '-', '-', '-', '-'],
                                ['-', '-', '-', '?', '?', '?', '-', '-', '-', '-', '-', '-', '-', '-', '?', '?'],
                                ['#', '#', '#', '#', '&&', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '&'],
                                [' ', ' ', '-', '+', '#', '+', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+', '+'],
                                [' ', ' ', '+', '-', '#', '-', '+', ' ', ' ', ' ', ' ', ' ', ' ', '+', ' ', '+'],
                                ['-', '#', '-', '-', '$', '-', '-', '#', '-', '-', '-', '-', '#', '-', '-', '#'],
                                ['+', ' ', ' ', '-', '-', '-', ' ', ' ', '+', ' ', ' ', '+', ' ', ' ', ' ', '+'],
                                [' ', ' ', '-', ' ', '-', ' ', '-', ' ', ' ', '+', '+', ' ', ' ', ' ', ' ', '+'],
                                ['-', '-', '-', ' ', '-', ' ', ' ', '-', ' ', '+', '+', ' ', ' ', ' ', '-', '#'],
                                ['?', '?', '#', '+', '#', '+', '+', '+', '#', '+', '+', '+', '+', '+', '#', '$$'],
                                ['&&', '&&', '&', ' ', '&', ' ', ' ', ' ', ' ', '&', ' ', ' ', ' ', ' ', '&', '&'],
                                [' ', ' ', ' ', ' ', '&', '&', '&', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', '&', '$$', '&', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', '&', '&', '&', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

        

        resultado = ia_board_eventos.analizador_eventos(self.moves,self.moves_enemy,True) 

        self.assertEqual(analisis_expected, resultado)

    '''
    def test_move_sin_captura(self):
        board = [                                                                                      
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
        board_expected = 


        board_received = move_sin_captura(moves, True, board)
    '''