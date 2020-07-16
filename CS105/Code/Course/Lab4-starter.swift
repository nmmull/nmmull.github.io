import Foundation

struct OrderedDictionary<S: Hashable, T> {

    // -------------------
    // DATA REPRESENTATION
    // -------------------

    var data = [(S, T)]()

    //var data1 = [S: T]()
    //var data2 = [S]()

    // -------------------
    // GET-SET FUNCTIONS
    // -------------------

    var keysAndValues: [(S, T)] {
        get {
            // TODO
            return []
        }
    }

    subscript(key: S) -> T? {
        get {
            // TODO
            return nil
        }
        set(newValue) {
        }
    }

    // -------------------
    // ABSTRACTION BARRIER
    // -------------------

    var isEmpty: Bool {
        get {
            // TODO
            return true
        }
    }
    var count: Int {
        get {
            // TODO
            return 0
        }
    }
    func atIndex(_ i : Int) -> (key: S, value: T) {
        assert(i >= 0 && i < count, "ERROR: index out of range")
        // TODO, THE NEXT LINE IS CLEARLY WRONG, FIX IT
        return keysAndValues.first!
    }

    func index(forKey k : S) -> Int? {
        // TODO
        return nil
    }

    mutating func removeValue(forKey key: S) -> T? {
        // TODO
        return nil
    }

    mutating func remove(at index: Int) -> (key: S, value: T) {
        assert(index >= 0 && index < count, "ERROR: index out of range")
        // TODO, THE NEXT LINE IS CLEARLY WRONG, FIX IT
        return keysAndValues.first!
    }

    mutating func updateValue(_ value: T, forKey key: S) -> T? {
        //TODO
        return nil
    }

    mutating func updateValue(_ value: T, atIndex index: Int) -> T? {
        assert(index >= 0 && index < count, "ERROR: index out of range")
        // TODO
        return nil
    }
}


// -----
// TESTS
// -----

//var d = OrderedDictionary<Int, Int>()
//assert(d.isEmpty)
//d[1] = 1
//assert(!d.isEmpty)
//d[2] = 2
//assert(d.count == 2)
//assert(d.keys == [1, 2])
//d[1] = 3
//assert(d.values == [3, 2])
//d[1] = nil
//d[1] = 1
//assert(d.atIndex(0) == (2, 2))
//assert(d.index(forKey: 1) == 1)
//assert(d.removeValue(forKey: 2) == 2)
//d[3] = 3
//assert(d.remove(at: 1) == (3, 3))
//assert(d.updateValue(2, forKey: 2) == nil)
//assert(d.updateValue(2, atIndex: 0) == 1)

