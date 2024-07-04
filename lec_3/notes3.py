Exceptions are things that go wrong within our coding.
print("hello, world)
SyntaxError : error in the written code
eg: incomplete string
-->fix : do it manually by rereading the code


Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead. Your program may throw an error because of this unexpected input from the user.
x = int(input("What's x? "))
print(f"x is {x}")
ValueError : another value type was entered than the one anticipated
input: "cat" , 78.90
both these are not int so we get ValueError
-->fix : use try except in code

try and except are ways of testing out user input before something goes wrong.

)NameError :
-->fix : else can be used

)break : used to break out of any loop

****>> "we try to minimize the number of lines in the code in order to catch errors easily. less code. easier to catch errors"

__________DEBUGGING_____________
)breakpoint : a point set in your code around which you debug by oen by one execution of your code.

"Step In" will enter the function that you're about to call, allowing you to debug it line by line.

"Step Over", on the other hand, executes the entire function you're about to call without entering it, effectively treating it as a single step. This is useful when you know a function is working correctly and you don't want to debug inside of it.


https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@bd6e4b312f2b4e8d9e89ec63708a367a/block-v1:HarvardX+CS50P+Python+type@vertical+block@623a0c3f8ee941baa7ceeef4204f94e8


always write the error which the except block will handle. if w edo not specify the error, it will handle all errors which make debugging difficult job
