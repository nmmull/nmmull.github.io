import Foundation

// func dumb() {
//     dumb()
// }
//
// dumb()

// 1! = 1
// n! = n(n - 1)! for n > 1

func factorial(_ n: Int) -> Int {
    assert(n > 0)
    if n == 1 { return 1 }
    let almost = factorial(n - 1)
    return n * almost
}

func reverse<T>(_ l: [T]) -> [T] {
    // reverse of empty is empty
    if l.isEmpty { return [] }
    // reverse of the list l + [x] is [x] + reverse(l)
    var l = l
    let lastElement = l.removeLast()
    var almost = reverse(l)
    almost.insert(lastElement, at: 0)
    return almost
}

assert(reverse([1, 2, 3]) == [3, 2, 1])

func fib(_ n: Int) -> Int {
    if n == 0 || n == 1 { return 1 }
    return fib(n - 1) + fib(n - 2)
}

func isSubsequence(_ x: Int, of y: Int) -> Bool {
    if y == 0 { return x == 0 }
    return y % powerInt(10, numberOfDigits(of: x)) == x ||
           isSubsequence(x, of: y / 10)
}

func numberOfDigits(of x: Int) -> Int {
    if x < 10 && x >= 0 { return 1 }
    return 1 + numberOfDigits(of: x / 10)
}

let powerInt: (Int, Int) -> Int = { (x, y) in
    return Int(pow(Double(x), Double(y)))
}

assert(isSubsequence(42, of: 111142111))

func hourglass(_ x: Int) -> [String] {
    if x == 0 { return ["**"] }
    var glass = hourglass(x - 1)
    glass = glass.map({ line in
        return " " + line
    })
    let largeLine = String(repeating: "*", count: 2 * (x + 1))
    glass.insert(largeLine, at: 0)
    glass.append(largeLine)
    return glass
}


for line in hourglass(10) {
    print(line)
}
