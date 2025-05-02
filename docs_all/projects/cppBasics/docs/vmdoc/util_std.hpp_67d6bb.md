---
title: /util_std.hpp
source_file: /util_std.hpp
description: Contains documentation for how to do some things using the standard library: Everything should be supported in C++11 and newer versions across most major platforms(Windows, Linux, Browser using emscripten)
generated_from: vmdoc
source_code_file: util_std.hpp_67d6bb.txt
---

[📄 View raw source code](util_std.hpp_67d6bb.txt)

## Assert(x)
Assert that some expression is true, and throw an error if not

## ThrowError(x)
Print an error message and throw an exception

## AssertEq(v1, v2, deviance)
Assert that two numerical values are equal within a given deviance
- `v1`: First value
- `v2`: Second value
- `deviance`: Allowed difference between `v1` and `v2`

## pad_str(str, length)
    Pad a string with spaces until it reaches the desired length
    - `str`: Input string
    - `length`: Target length after padding

## split_string(str, separator)
    Split a string by a given separator character
    - `str`: The string to split
    - `separator`: The character used to divide the string

## Print(x)
Print a value with contextual info (file, line, function)

## PrintExpr(x)
Print an expression and its value with contextual info

## AddTest(test_name)
Register a function as a test case to be executed later

int add_(int x, int y)
    {
        return x + y;
    }

    // Add a test for the function
    void TEST_add_()
    {
        assert(add_(1, 2) == 3);
    }
    AddTest(TEST_add_);

    // Run all tests
    // int main() {
    //    vicmil::TestClass::run_all_tests();
    //    return 0;
    //}
    //

## vec_to_str(vec)
Convert a vector of numbers to a formatted string
- `vec`: The input vector

example: "{123.321, 314.0, 42.0}"

