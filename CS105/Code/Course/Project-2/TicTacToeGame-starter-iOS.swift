//
// starter code for the tic tac toe model
// create a new file in your xcode project with this code
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
