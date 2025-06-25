/*
	Offitial D-Lang Docs at : https://dlang.org/spec/lex.html
*/
module cheatsheet;

import std.stdio;
import std.algorithm;
import std.string;
import std.conv;

// variables
string name = "roy";
char alphabet = 'y';	/* char represents charector 1-byte */
int number = 1234;	
float decimal_number = 1.44449;
bool true_or_false = true;
byte bytes = 127; /*-128 to 127*/

/* for more data types: https://www.tutorialspoint.com/d_programming/d_programming_data_types.htm */

// enums
enum Constant_values {
	sun=7,
	mon=9,
	sat=5
}; /* Constant_values is the enum type name */

enum { orange=10, mango=8 , apple=2 } /* Anonymous enum */

// Arithmetic operator
/*
	 + means sum of two digits
	 - means difference of two digits
	 * means multiple of two digits
	 / means dividing two digits
	 % means divisible reminder of two digits
	 ++ means increase value by 1
	 -- means decrease value by 1
*/

// Relational operator
/*
	== checks wheather values equal
	!= checks wheather values not equal
	>  checks wheather values greater than the other
	< checks wheather values smaller than the other
	>= checks wheather values greater than or equal
	<= checks wheather values lesser than or equal
*/

// Logical operator
/*
	&& AND logic
	|| OR logic
	! Not logic
*/

// Bitwise Operators
/*
	see them here: https://www.tutorialspoint.com/d_programming/d_programming_operators.htm
*/

// Charecters
/*
	isLower	wheather charecter is lowercase
	isUpper	wheather charecter is uppercase
	isAlpha	wheather charecter is alphanemuric
	isWhite wheather charecter is a whitespace
	toLower converts to the lowercase 
	toUpper converts to the uppercase
*/

// Strings
/*
	~ tidle symbol to concatenate strings like "bana"~"@"~"na" => "bana@na"
	length to get the string-length
	char[] charecter_arrey = "hello".dup	string containing arrey of charecters
	char[5] charecter_arrey = "monkey"
	== >= can be used to compare strings
	"bees like honey"[5..8] => "bees"
	std.string.indexof("hello world" , "or") => 7  index of "or" in "hello world"
	strip("  banana  ") => "banana"  eleminates leading&trailing whitespaces
	toUpper() , toLower() , capitalize()
*/

//Array
/*
	int prices[2] = [10 , 8]	(static array) as length is defined at init
	int[] fruits = ["apple", "banana" , ....(unlimited number of contents)]		(dynamic array)
	prices[1] => 8		indexing (starts from 0)
	fruits[5] = "orange"	incerting new eliments at that index(5)
	prices.length => 2
	prices.sizeof => size in bytes
	prices.dup => a dynamic copy
	prices.idup => an immutable dynamic copy 
	prices.reverse => reverse the arrey elements
	prices.sort => sort the array elements
		**multi-dimentional arrey**
	int matrix[3][4] = [0,1,.....11]	type name [row][collumn] (12 elements matrix )
	int a[3][4] = [   
	[0, 1, 2, 3] ,   initializers for row indexed by 0 
   	[4, 5, 6, 7] ,   initializers for row indexed by 1  
   	[8, 9, 10, 11] ] initializers for row indexed by 2
	matrix[1][2] => 6	index starts from 0
		**operations**
	string[] days = ["monday", "sunday", "friday", "saturday"]
	days[1..3] => ["sunday" , "friday"]		//slicing
	int d[5]
	d = 5 => [5,5,5,5,5]
	int f[2] = [2,50]
	d~f	=> [5,5,5,5,5,2,50]		//concatanating
*/

// Associate Array	(dict for python)
	string[char] fruit_codes;	// value_type[key_type] arrey_type
/*
	fruit_codes['m'] = "mango";
	.sizeof => size of the associate array
	.length => numbers of value present in it
	.dup => duplicate it with same size
	.keys => gets all keys
	.values => gets all vales
	.rehash => reorganizes the associate array for effitient lookups
	.byKey()
	.byValue()
	.get(KEY , default_VALUE) => gets the value associated with that key , if key doesnt exist returns default value
	.remove(KEY) => removes that key and its value from the aarray
*/

// Pointers
	auto price = 9.90;
	double *pointr = null;	// memory addres
/*
	int *pointr = null;	null pointer (good practice) on init
	pointr => memory address
	*pointr => value
	// pointer to pointer
	int **pointr2 = &pointr	=> holds address of another pointer
	**pointr => value
	// pass pointer to func()
	void func(int *pointr) {...}	// must declare pointer as a type of argument
	// array to pointer
	int[] prices = [10,20,9,67];
	int *pointr = &prices[0]	// frist element's address
	*(pointr++) => prices[1] => 20	// pointr(address)++ next address in the array
	*(pointr++) => prices[2] => 9	//
*/

// Tuples
	import std.typecons;
	auto myTuple = tuple('s' , 10 , "bread" , false);
	// Tuple Template
	auto myTuple_template = Tuple!(int, "id", string , "name") (2 , "jazmin");
/*
	myTuple[0]	=> 's'
	// Template's operation
	myTuple_template.id	=> 2
	myTuple_template[1] => "jazmin"
*/




void mai() { 
// int[] nums = [1,2,3,4,11];
// writeln( nums.all!(x => x>=0 && x<=9) );
	char[] nums = ['0','1','2','3','4','5','6','7','8','9'];
	bool check(char input) {
		foreach (i; nums)
		{
			if (i == input)
			{ writeln("found match");return true;}
			
		}return false;
 
		// writefln("%c\t%s",input , &nums);
		// return 1;
	}
	string input = readln().strip();
	if (input.all!(x=> check(to!char(x)))) {
		writeln("ok");
	} else {
		writeln("not ok");
	}
	
}

void for_condition() {
	for (int i=1; i<=10 ; i+=i) {
		writeln(i);
	}
}

void for_in() {
	foreach(i;1..10){
		writeln(i);
	}
}

void while_loop() {
	int i = 1;
	while(i<=5) {
		i += i;
		writeln(i);
	}
}

void do_while_loop() {
	int t = 0;
	do {
		writeln("I am from do while loop");
		t += 1;
	} while(t<=5);
}

void if_else() {
	if (9>0) {
		writeln("if you dont solve it , ur saved");
	} else {
		writeln("else I am going to kidnap your dog");
	}
}

void switch_case() {
	// check against each values/cases
	int marks = 9;
	switch(marks) {
		case 1 :
			writeln("Poor grades");
			break;
		case 5 :
			writeln("Moderate grades");
			break;
		case 7 :
			writeln("Good performance");
			break;
		case 9 :
			writeln("Excelent");
			break;
	default :
		writeln("10/10");
	}
}

void main() {
	string[] names = [];

	names ~= "sam";

	writefln("%s" , names);
	// for in loop
	for_in();
	// for in with condition
	for_condition();
	// while loop
	while_loop();
	// do-while loop
	do_while_loop();
	// if-else
	if_else();
	// switches
	switch_case();
	// enums
	writeln(Constant_values.min , " " ,"size/length of the enum: " , Constant_values.sizeof );
	writefln("the most loved fruit is: %s", orange);
	// Concatanating with ~
	writeln("string concatanation " , "bana"~""~"na", " " ,"banana".length);
	// Array 
	char[] s = "monkey loves banana".dup;
	s[13..19]="applee";
	char[] p = ['s','o'];
	writeln("string replacement " , s);
	writeln(s," ","and type is: ",typeof(s).stringof,"\nexample of char arrey[] ",p);
	// associate arrays
	fruit_codes['m'] = "mango";		// setting value
	fruit_codes['o'] = "orange";
	writefln("associate array of fruit codes: %s",fruit_codes['m']);
	writeln(fruit_codes.get('a',"not_found_404"));
	// Pointers
	pointr = &price;
	writeln("pointer: ", pointr);
	// Tuples
	writeln("tuples: ", typeof(myTuple[]).stringof);
}