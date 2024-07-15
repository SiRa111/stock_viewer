 unittest: code that CHECKS units of your (typically fxns)

--> assert: you are assuming that the given condition is true. if not it will raise an AssertionError

AssertionError

we ended up writing 38 lines of test_code for 2 lines of fxn
not a very convinent way

pytest - 3rd party library that assissts you in testting your code
pip install pytest
try to write code in fxns
makes debugging easier

give your fxns a return value to make them more testable rather than just printing

__init__.py
the folder in which you make this file is treated as a package
ie a package with multiple fxns
and not just a module or file alone
