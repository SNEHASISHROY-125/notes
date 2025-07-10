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
// functions
/**
    fun fun_name (arg : arg_Type) : return_type {}
*/

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