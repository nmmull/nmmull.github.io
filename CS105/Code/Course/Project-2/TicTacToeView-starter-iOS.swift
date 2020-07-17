//
// A possible outline for the TicTacToeView
//

import SwiftUI

struct TicTacToeView: View {
    var body: some View {
        Text("TODO: format layout")
    }
}

struct TitleView: View {
    var body: some View {
        Text("TODO: title")
    }
}

struct BoardView: View {
    var body: some View {
        Text("TODO: a VStack of HStacks of PositionViews")
    }
}

struct PositionView: View {
    var position: TicTacToeGame.Board.Position
    var body: some View {
        ZStack {
            Rectangle()
                .foregroundColor(.gray) // or whatever color you want
            Text("TODO: occupying player, determined by the view model")
        }
            .onTapGesture {
                // TODO : ask view model to make a move in the game
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
