# Storage

## Typical `int` Size in Popular Programming Languages

| Language      | Typical `int` Size (bits) |
| ------------- | ------------------------- |
| C (32/64-bit) | 32                        |
| C++           | 32                        |
| Java          | 32                        |
| C#            | 32                        |
| Python\*      | 32 (platform-dependent)   |
| Go            | 32 or 64 (platform)       |
| JavaScript    | 32 (bitwise ops)          |

\*Python's `int` is arbitrary-precision, but C-extensions and some platforms use 32 or 64 bits for fixed-width integers.

**Sources:**

- [C/C++ int size](https://en.cppreference.com/w/cpp/language/types)
- [Java int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
- [C# int](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types)
- [Go int](https://go.dev/ref/spec#Numeric_types)
- [JavaScript bitwise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_Operators)

## Typical Read Latencies

| Operation                          | Time (nanoseconds) | Time (milliseconds) |
| ---------------------------------- | ------------------ | ------------------- |
| L1 Cache Reference                 | ~0.5               | 0.0000005           |
| L2 Cache Reference                 | ~7                 | 0.000007            |
| RAM Reference                      | ~100               | 0.0001              |
| SSD (local)                        | ~150,000           | 0.15                |
| HDD (local)                        | ~10,000,000        | 10                  |
| Network (same data center)         | ~500,000           | 0.5                 |
| Network (cross-country/datacenter) | ~150,000,000       | 150                 |

**Sources:**

- [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832)
- [Jeff Dean, "Numbers Everyone Should Know"](https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html)
