```c++
#usda 1.0
(
    expressionVariables = {
        string VARIANT_CHOICE = "variantA"
        bool UseProxyModel = false
        int64 IDENTIFIER = 3254
        string[] renderPassList = ["foreground", "background", "FX"]
    }
)
```

### string

A string, which in USD’s utf-8 text format, usda, is delimited by double or single quotes. Quote characters can be escaped using Python-style escaping (”"). A string value itself can contain a variable expression contained in backticks (“`”), that will be evaluated when the variable is used in a variable expression.

Examples:

```c++
string exampleStr = "I am a string"
string exampleStrEscaped = "A \"quote escaped\" string"
string exampleStrEscaped2 = """Another "escaped" string"""
string exampleStrBoolExpression = "`True`"
string exampleStrIfExpression = '`if(${USE_RED}, "red", "blue")`'
string exampleStrExpanded = "`charA_${MODEL_CATEGORY}_${MODEL_VERSION}`"
```

### bool

A boolean value. Accepted values are True, true, False, or false.

Examples:
```c++
bool exampleBool = False
bool exampleBool2 = true
```

### int64

A 64-bit integer.

Examples:
```c++
int64 exampleInt = 43
int64 exampleIntNeg = -500
```

### type

A list of one of the previously mentioned types. The list can only contain values of one type. Lists with mixed types will result in an error.

Examples:
```c++
string[] exampleStringList = ["red", "green", "blue"]
int64[] exampleIntList = [4, 5, 6]
bool[] exampleBoolList = [True, False, False, True]
```


### None

None is a special case value. Currently, you can’t set a variable directly to None. The None value can only be used within an expression, and is useful for expression functions, like the if() function, detailed in [Expression Function Reference](https://openusd.org/release/user_guides/variable_expressions.html#expression-function-reference).

None is also not allowed in a list within an expression. The following examples will result in an error when evaluated:

`[1,2,3,None]` # Lists with None values are not allowed
`[if(False, 1)]` # The if() function will evaluate to None, so this is also not allowed in a list