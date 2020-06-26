import Darwin

// example of a variable
var x = 2

// example of a function
// x appears also as a parameter
// this is sometimes called VARIABLES SHADOWING
func addTwo(first x: Int, second y: Int) -> Int { return x + y }

// example of a function which uses a nonlocal variable.
func addX(_ y: Int) -> Int { return x + y }

assert(addTwo(first: 3, second: 3) == 6)
assert(addX(5) == 7)

// simple if statement
if x == 2 || x == 3 {
    x = 4
}

// compound assingment operator
// same as x = x + 1
x += 1

//simple while loop
var i = 0
while i < 10{
    print(i)
    i += 1
}

// simple for loop with the same behavior
for i in 0..<10 {
    print(i)
}

func isPrime(_ n: Int) -> Bool {
    assert(n > 0, "isPrime called on a nonpositive number: \(n)")
    for i in 2..<n {
        if n % i == 0 { return false }
    }
    return true
}

assert(!isPrime(27))
assert(isPrime(97))

func intToThePositiveInt(_ x: Int, toThe y: Int) -> Int {
    assert(y >= 0, "Cannot apply itToThePositiveInt with negative exponent: \(y)")
    if y == 0 { return 1 }    // necessary because upper bound of range must be >= 1
    var accum = 1
    for _ in 1...y {
        accum *= x
    }
    return accum
}

assert(intToThePositiveInt(2, toThe: 3) == 8)
assert(intToThePositiveInt(2, toThe: 0) == 1)

func getDigit(_ x: Int, at index: Int) -> Int {
    if index < 0 { return -1 }
    let div = abs(x) / intToThePositiveInt(10, toThe: index)
    return div == 0 ? -1 : div % 10   // another way to write it using special trinary operator
                                      // X ? Y : Z means "if X then Y else Z.
}

assert(getDigit(123456, at: 0) == 6)
assert(getDigit(123456, at: 1) == 5)
assert(getDigit(123456, at: 2) == 4)
assert(getDigit(123, at: -1) == -1)
assert(getDigit(123, at: 5) == -1)
assert(getDigit(-123, at: 0) == 3)
