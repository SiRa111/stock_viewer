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
)breakpoint :

https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@bd6e4b312f2b4e8d9e89ec63708a367a/block-v1:HarvardX+CS50P+Python+type@vertical+block@623a0c3f8ee941baa7ceeef4204f94e8
