struct Image {
    enum Pixel: Character {
        case on = "*"
        case off = " "
    }

    enum Side {
        case top
        case bottom
        case left
        case right
    }

    var grid: [[Pixel]]

    init(width: Int, height: Int) {
        assert(width > 0 && height > 0)
        grid = []
        for _ in 1...height {
            grid.append(Array(repeating: .off, count: width))
        }
    }

    init(fromString s: String) {
        // TODO: fill in code here
        grid = [] // TODO: change this line
    }

    func width() -> Int {
        return grid.first!.count
    }

    func height() -> Int {
        return grid.count
    }

    func asString() -> String {
        // TODO: fill in code here
        return "" // TODO: change this line
    }

    mutating func stack(_ image: Image, on side: Side) {
        // TODO: fill in code here
    }

    mutating func trim(by amount: Int, on side: Side) {
        // TODO: fill in code here
    }

    mutating func pad(by amount: Int, on side: Side) {
        // TODO: fill in code here
    }
}

let pixel = Image(fromString: "*")

let cross = Image(fromString:
    """
     *
    ***
     *
    """
)

func sierpinskiRightTriangle(_ n: Int) -> Image {
    // TODO: fill in code here
    return pixel // TODO: change this line
}

func sierpinskiCross(_ n: Int) -> Image {
    fractalImage(cross, depth: n)
}

func fractalImage(_ image: Image, depth: Int) -> Image {
    // TODO: fill in code here
    return pixel // TODO: change this line
}

func sierpinskiTriangle(_ n: Int) -> Image {
    // TODO (Challenge Problem): fill in code here
    return pixel // TODO: change this line
}
