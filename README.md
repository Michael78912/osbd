# osbd
## Operating System Based Data
### a data interchange format, like JSON, but based on basic operating system functions

meant to be a markup language, but has ability to directly enter the OS's functionality.  
an example is below:  
```
#(
block comment
this is going to be a markup language that i will use.
)#

s = (author "me" & version 0.0)[
    data = 8901 # number
    string = "hi" 
    string2 = 'hiv' # both strings
    char = ^c # character
    eval = |12 - 34 # evaluated expression
    uni = u555 # unicode characterfrom code number (hex works too)
    uni2 = u^‏‍⁭ # unicode character from character 
    obj = ()[int =   12] # another object (must be encoded properly)
    path = $PATH # environment variable
]   
```

I am currently writing the parser in [python](https://python.org), but I'll also try a C and JS, when I'm done.
