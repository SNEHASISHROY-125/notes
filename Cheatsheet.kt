package io.github.snehasishroy125

val no_of_sun:Int = 1	// immutable
var name_of_planet = "Earth"
// name_of_fruit = "orange" --> gives error can't modify outside a func

// Data-Types
//	strings
var s:String = "myname"
var raw:String = """ 
halo mine Alexandar die foosbal
"""
// \n ->linebreak , \\ -> \ , \$ -> $
//	integer
var i:Int = 25
var f:Float = 20.7880f
var d:Double = 21.7899
var b:Byte = 127    //  -128 to 127
//	char
var c:Char = '@'
//	Boolean
var truth_or_dare:Boolean = true
// arrey
// conversion
/**
 * toByte()
 * toShort()
 * toInt()
 * toLong()
 * toFloat()
 * toDouble()
 * toChar()
 */
// operaters
/** 
 * +
 * -
 * *
 * /
 * %
 * relational
 * >
 * <
 * >=
 * <=
 * ==
 * !=
 * assignment 
 * +=	like x +=10 -> x = x+10
 * -=
 * *=
 * /=
 * %=
 * 		Unary
 * + positive value
 * - negetive value
 * ++ increament value by 1
 * -- decrease value by 1
 * !true -> false
 * 		Logical
 * && -> logical and
 * || -> logical or
 * ! -> logical not
 * 	Bitwise Operations > https://www.tutorialspoint.com/kotlin/kotlin_operators.htm
 *
 */
// Boolean Operater
/**
 * true && false -> false
 * true || false -> true
 * !true -> false
 * 20>2 -> true
 * 20<=10 -> false
 * 20!=14 -> true
 * true.and(false) -> false
 * true.or(false) -> true
 * false.toString() -> true
 */
// Strings
/**
    .length -> length of string   eg. " $(name.length) " inside a string or name.length normally
    .count() -> lenght of string
    .indices --> range of index
    "raja"[2] -> "j"
    "elephant".lastIndex -> 7
    "mango".toUpperCase() -> MANGO
    .toLowerCase()
    "mango" + "juice" -> "mangojuice"
    .plus()   eg. "tr".plus("ee") -> "tree"
    .drop(index) 
    .dropLast(index)    // drop charec with index form end
    .indexOf("string-to-look-for")  // "mango".idexOf("ng") -> 2
    str1.compareTo(str2)  --> bool
    .getOrNull(index)   --> returns the char at that index or Null
    .toString() --> convert to string " "

*/
// Array
var arr = arrayOf("banana" , "apple")
var farr = arrayOf<Float>(0.33f , 0.54f)
/**
    intArrayOf()   --> array of int only
    floatArrayOf()
    byteArrayOf()
    charArrayOf()
    .get(index)  --> get item from array at that index
    .set(index , value)  --> set the value at that index
    .size   --> length of array
    .indices --> range of index
    .lastIndex  --> index of last element
    .distinct() --> ommit duplicates
    .drop(index)   --> drop from array at that index
    .dropLast(index)   --> drop from end
    .isEmpty()  --> (bool) wheather array is empty or not
*/
// Ranges
var rnge = 1..10 // range 1 --> 10 
/**
    a..z --> range of b to z char 
    'a' .. 'f'  --> (char) a , b , c ... f
    start.rangeTo(end) 
    end downTo start   --> range in reverse
    1 .. 10 step 2  --> leave 2 steps in between
    (1..5).reversed()   --> reversed range
    1 until 5   --> 2 ,3 ,4
    .first --> first element of range
    .last  --> first element of range
    .step  --> step in between elements in range
    .filter{match_expration}  1..10.filter { T -> T % 2 == 0 } --> [2,4,6,8]
    .max()
    .min()
    .avarage()
    .sum()
    .count()
*/
// List
    /* Imutable List */
    var lists = listOf("mango" , "banana" , 12)
/**
    in works with lists  if ("gg" in lists) {print(1)}
    + --> cncatanation : list1 + list2 
    - --> subtraction : list1 - list2 
    .toString()
    .listIterator() --> creates an iterator for that list
    .listIterator().hasNext()  --> (bool) if next loop iteration exists (use inside loop)
    .listIterator().next()  --> next element (use inside loop)
    .indices --> range of index
    .size  --> size of list
    .random()   --> random element
    .contains(element) --> (bool) if list contains that element
    .isEmpty()  --> (bool) if list is empty
    .indexOf(element)  --> returns index of that element if present in list else -1
    .get(index)  --> get element at that index
    .slice(range)  --> sliced list
    .filterNotNull() --> ommit Nulls
    .filter{ it.startswith("ma") } --> [(elements if startswith "ma") , ...]
    .groupBy{ condition }  : listOf(10, 12, 30, 31, 40, 9, -3, 0).groupBy{ it%3 }  >  {1=[10, 31, 40], 0=[12, 30, 9, -3, 0]}
    .map{ cndition }  :  (10, 12, 30, 31, 40, 9, -3, 0).map{ it<=10 }   >   [true, false, false, false, false, true, true, true]
    */
    // Mutable List (Set)
    var mulablelists = mutableSetOf(11 , 17 , 'd' , 2.44499f)
    /*
    .add(item)
    .remove(item)
*/
// Map 
    /* Imutable Map */
    var maps = mapOf("id" to 10 , "name" to "roy" )
    // maps["id"] --> "10"
/*  
    .size
    .isEmpty()
    .values   --> vakues of map
    .keys     --> keys of map
    .entries  --> list representation of map entries
    .toString()
    .toList()
    .iterator()  &  .hasNext()  & next()  works
    .containsKey(key)   --> (bool)
    .containsValue(value)   --> (bool)
    .get(key)   --> corrosponding key
    .remove(key)  --> removing the key-entry
    +   --> map1 + map2 
    -   --> map1 - map2 
    .toSortedMap()  --> returns sorted map in accending order
    .sortedDescending()
    .filter{ condition }
    .filterKeys{ condition }   ---> filter by keys
    .filterValues{ it > 2}  */ 

    /* mutable Map */
    var immutablemap = mutableMapOf()
    // maps[key] = value | adding new entries
    /*
    .put(key , value)   --> register a new entry with that key : value
*/


// functions
/**
    fun fun_name (arg : arg_Type) : return_type {}
*/  
    fun divs(a:Int , b:Int):Int { return a%b }
    // Hier-order methods
    fun operation(a:Int , b:Int , method:(Int , Int) -> Int) { return method(a,b)}
    // call it :
    /*  operation(7 , 2 , ::divs) */
    // LAMBDA
    /* { var : Type -> var+=1 (operation)} */
    var lambd = {cc : String -> cc.uppercase()}
    // call it :
    /* lambd("car") --> "CAR" */
    // InLine methods
    /* inline fun method(methodToCall:() -> return_type) { methodToCall() } */
    inline fun myinline(method:() -> Unit) { method() }
    // call it 
    /* myinline( { print("my iline method works!") } ) */

fun main():Unit {	// return type Unit > None
    var name = ""
    name = "ram"
    name_of_planet = "pluto" 
    println("helo from main , it is the default entrypoint")
    var res = 2 + -2
    print("$name" + "$res" + " $raw")
    // Array ops
    for (elements in arr) {
        println(elements)
    }
    if ("monkey" in arr) {
       println("found it")
    } else {
        println("404...")
    }
}