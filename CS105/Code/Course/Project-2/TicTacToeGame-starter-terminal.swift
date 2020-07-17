//
// starter code for the tic tac toe terminal game
//

import Foundation

struct TicTacToeGame {
    enum Player: String {
        case x = "X"
        case o = "O"
    }

    struct Board {
        struct Position: Hashable {
            var row: Int
            var column: Int
        }

        let size: Int
        var boardState = [Position: Player]()

        init(size: Int) {
            assert(size >= 1, "Board size must be positive")
            self.size = size
        }

        var rowIndices: Range<Int> {
            get {
                return 0..<size
            }
        }

        var columnIndices: Range<Int> {
            get {
                return 0..<size
            }
        }

        subscript(row: Int, column: Int) -> Player? {
            get {
                assert(rowIndices.contains(row) && columnIndices.contains(column), "Board index out of bounds")
                return boardState[Position(row: row, column: column)]
            } set(player) {
                assert(rowIndices.contains(row) && columnIndices.contains(column), "Board index out of bounds")
                return boardState[Position(row: row, column: column)] = player
            }
        }

        subscript(position: Position) -> Player? {
            get {
                return self[position.row, position.column]
            }
            set(player) {
                self[position.row, position.column] = player
            }
        }
    }

    var size: Int
    var board: Board

    init(size: Int) {
        self.size = size
        board = Board(size: size)
    }

    var currentPlayer: Player {
        get {
            // TODO : Returns the player whose turn it is. The first player is
            //        the X player
            return .x
        }
    }

    var winner: Player? {
        get {
            // TODO : Returns the player who has won if there is a winner and
            //        nil otherwise
            return nil
        }
    }

    var isOver: Bool {
        get {
            // TODO : Returns true if there is a winner of the game is a draw
            //        and false otherwise
            return false
        }
    }

    mutating func makeMove(row: Int, column: Int) {
        // TODO : Add the current player to the board at the given position if
        //        it is a valid move
    }

    mutating func makeMove(at position: Board.Position) {
        // TODO : Same as above but for Positions
    }
}

extension TicTacToeGame.Board: CustomStringConvertible {
    var description: String {
        var out = ""
        for row in rowIndices {
            var line = ""
            for column in columnIndices {
                line += " " + (self[row, column]?.rawValue ?? " ") + " "
                line += column < size - 1 ? "|" : ""
            }
            let lineWithoutSymbols = String(line.map({ $0 == "X" || $0 == "O" ? " " : $0 }))
            let bar = String(repeating: "-", count: 4 * size - 1)
            out += "\(lineWithoutSymbols)\n\(line)\n\(lineWithoutSymbols)"
            out += row < size - 1 ? "\n" + bar + "\n" : ""
        }
        return out
    }
}

extension TicTacToeGame.Board {
    var occupiedPositions: [Position] {
        get {
            // TODO : returns an array containing those positions on the board
            //        occupied by a player
            return []
        }
    }
    var unoccupiedPositions: [Position] {
        get {
            // TODO : returns an array containing those positions on the board
            //        not occupied by a player
            return []
        }
    }

    func isValidMove(row: Int, column: Int) -> Bool {
        // TODO : Returns true if the given position is unoccupied and the
        //        inputs are in bound
        return false
    }

    func isValidMove(_ position: Position) -> Bool {
        // TODO : same as above but for Positions
        return false
    }
}

// ------------------------------
// COMPUTER PLAYER IMPLEMENTATION
// ------------------------------

extension TicTacToeGame {

    mutating func makeComputerMove() {
        func minimax(of game: TicTacToeGame) -> Double {
            // TODO : returns the minimax value of a given game
            // OUTLINE OF PROCEDURE
            // value of game with X as winner is 1.0
            // value of game with O as winner is -1.0
            // value of draw is 0.0
            // for all possible moves of current player
                // make said move in game and determine the minimax value of the
                //     resulting function
            // return the maximum or minimum of those minimax values, depending
            //     on the current player.
            return 0.0
        }
        // TODO : call makeMove on the Position that maximizes the minimax value
        //        of the resulting state of the game.
    }

    func heuristicValue() ->  Double {
        // (EXTRA CREDIT) returns a heuristic value of the game state
        return 0.0
    }

    mutating func makeComputerMove(depth: Int) {
        // (EXTRA CREDIT) same as above, but with a depth limit
    }
}

let header =
"""
WELCOME TO TERMINAL
 _______ _        _______           _______
|__   __(_)      |__   __|         |__   __|
   | |   _  ___     | | __ _  ___     | | ___   ___
   | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\_/ _ \\
   | |  | | (__     | | (_| | (__     | | (_) |  __/
   |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|

To make a move, type two Ints separated by space. The
first is the index of the row and the second is the
index of the column. So the input

0 0

place a piece at the top lefthand corner.
"""

func main() {
    let display : (CustomStringConvertible) -> () = {
        print("")
        print($0)
    }
    display(header)
    var game = TicTacToeGame(size: 3)
    while !game.isOver {
        switch game.currentPlayer {
        case .x:
            display(game.board)
            display("Your move...")
            while true {
                if
                    let inputs = readLine()?.split(separator: " "),
                    inputs.count == 2,
                    let row = Int(inputs[0]),
                    let column = Int(inputs[1]),
                    game.board.rowIndices.contains(row),
                    game.board.columnIndices.contains(column) {
                    if game.board.isValidMove(row: row, column: column) {
                        game.makeMove(row: row, column: column)
                        break
                    } else {
                        display(game.board)
                        display("That position is already taken. Try again...")
                    }
                } else {
                    display(game.board)
                    display("That is not a valid input. Try again...")
                }
            }
        case .o:
            display("The computer's move...")
            game.makeComputerMove()
        }
    }
    display(game.board)
    if let player = game.winner {
        display("\(player.rawValue) player won!")
    } else {
        display("It's a draw.")
    }
}

// UNCOMMENT TO RUN COMMAND-LINE GAME
//main()
