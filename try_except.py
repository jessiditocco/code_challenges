# # Errors and Exceptions in Python
# # Exception handling allows us to continue or program (or terminate it), if an
# # exception occurs
# # Error handling in python isdone through the use of exceptions that are caught
# # in try blocks and handled in except blocks
# # an exception is an error that happenss during the executin of a pgroam
# # when the error occurs, Python generates an exception that can be handled,
# # which avoids you program to crash-- exceptions are a good way to handle erros and
# # special conditions in a program

# # Try and Except
# # if an error is encountered, a try block code executionis stopped
# # and transfered down to the except block
# # you can raise an exception in your own program by using the raise exception [, value]
# # statment

try:
    print "Hello world"
    print sdf
except NameError:
    print "This is an error message!"

# # some of the common exception errors are:
#     # IOError-- if the file cannot be opened
#     # ImportError-- if python cannot find the module
#     # ValueError-- raised when a built-in operation or functionrecieves an 
#     # argument that has the right type but inappropriate value
#     # KeyboardInterrupt-- raised when the user hits the interrupt key (normally control c or Delete)
#     # EOFError-- raised when one of the built-in functions input() or raw_input()
#     # hits an end  of the file conditionwithout reading any data

# # you can raise an exception in your program by using the raise exception error
# # raising an exception breaks you out of your current code execution and returns
# # the exception back until it is  handled

# # the syntax is try: this code block
# # except [exception-name]:
# # This code instead

try:
    "some statements here"
except:
    "exception handling"


try:
    print 1/0

except ZeroDivisionError:
    print "you cant divide by zero"

# # The error handling is done through the use of exceptions that are caught in the
# # try block and handled in the except block
# # if an error is encountered, a try blcok code execution is stopped
# # and transferred down to tht except block

try:
    user_num = int(raw_input("Please pick a number between 1 and 10: "))
    print "your number entered was", user_num
except ValueError:
    print "You must enter a number; please try again"

