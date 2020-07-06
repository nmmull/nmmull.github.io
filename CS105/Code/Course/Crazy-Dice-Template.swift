/*
    Crazy-Dice.swift

    a program which searches for crazy dice (Sicherman-like dice)
    given a number of side and a number of dice

*/

import Foundation

var numberOfSides = 6
var numberOfDice = 2
var extraCredit = false

let usageString =
"""
OVERVIEW: Program for Finding Sicherman Dice

USAGE: swift Crazy-Dice.swift

OPTIONS:
    -number=<value>    set the number of dice used in the program to <value>
                       <value> must be a positive integer
                       if not included, the number of dice is 2

    -sides=<value>     set the number of sides on the dice used to <value>
                       <value> must be a positive integer
                       if not included, the number of sides is 6
"""

func main() {
    setParameters()
    printCrazyDice()
}

main()

func printUsage() {
    print(usageString)
    exit(1)
}

func setParameters() {
    func readArg(_ s: String) {
        // TODO: fill in this function
        printUsage() // TODO: change this line
    }
    if CommandLine.arguments.count > 1 {
        for arg in CommandLine.arguments[1...] {
            readArg(arg)
        }
    }
}

func approxChoose(_ n: Int, _ k: Int) -> Double {
    // TODO: fill in this function
    return 0 // TODO: change this line
}

func approxMultiset(_ n: Int, _ k: Int) -> Double {
    return approxChoose(n + k - 1, k)
}

func printCrazyDice() {
    if numberOfSides == 2, extraCredit {
        //TODO: fill in code here
        return

    }
    let standardDieSet = DieSet(repeating: [Int](1...numberOfSides).reversed(), count: numberOfDice)
    let standardDistribution = distribution(ofDieSet: standardDieSet)
    let maxSide = numberOfSides * numberOfDice - 2

    // TODO: fill in code here

    var currentDieSetOrNil: DieSet? = firstDieSet(minSide: 1)
    while let dieSet = currentDieSetOrNil {
        //TODO: fill in code here
        currentDieSetOrNil = nextDieSet(after: dieSet, minSide: 1, maxSide: maxSide)
    }
}

typealias Die = [Int]
typealias DieSet = [Die]
typealias Roll = [Int]
typealias Distribution = [Int: Int]

func firstDie(minSide: Int) -> Die {
    return [] // TODO: change this line
}

func nextDie(after die: Die, minSide: Int, maxSide: Int) -> Die? {
    // TODO: fill in this function
    return nil // TODO: change this line
}

func firstDieSet(minSide: Int) -> DieSet {
    return [] // TODO: change this line
}

func nextDieSet(after dice: DieSet, minSide: Int, maxSide: Int) -> DieSet? {
    // TODO: fill in this function
    return nil // TODO: change this line
}

func firstRoll() -> Roll {
    return [] // TODO: change this line
}

func nextRoll(after roll: Roll) -> Roll? {
    // TODO: fill in this function
    return [] // TODO: change this line
}

func rollValue(ofDieSet dice: DieSet, onRoll roll: Roll) -> Int {
    // TODO: fill in this function
    return 0 // TODO: change this line
}

func distribution(ofDieSet dice: DieSet) -> Distribution {
    // TODO: fill in this function
    return [:] // TODO: change this line
}
