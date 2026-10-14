# Static Code Analysis — Issues and Fixes

| **Issue** | **Type** | **Line(s)** | **Description** | **Fix Approach** |
| --------- | -------- | ----------- | --------------- | ---------------- |
| SQL query constructed using string interpolation | Security — Medium | 9 | User-controlled values were inserted directly into an SQL statement, potentially allowing SQL injection. | Replaced the interpolated query with a parameterized SQL statement using placeholders. |
| Use of `eval()` | Security — Medium | 21 | `eval()` executes a string as Python code and can execute unintended or malicious expressions. | Replaced `eval()` with direct arithmetic using numeric arguments for the penalty rate and number of months late. |
| Mutable default argument | Code quality / Bug risk | 8 | The default `history=[]` list could be shared between calls, causing unexpected state retention. | Changed the default to `None` and initialized a new list inside the function when needed. |
| Inconsistent return statements | Code quality | 12–15 | `collect()` returned the amount when a record existed but implicitly returned `None` otherwise. | Added an explicit `return None` when no matching record is found. |
| Hard-coded password | Security — Low | 5 | A password was stored directly in the source code, exposing a potentially sensitive value. | Removed the unused hard-coded password constant. |
| Missing module and function docstrings | Maintainability | 1, 8, 12, 19, 27, 34 | The module and functions lacked documentation describing their purpose. | Added a module docstring and docstrings to the functions. |
| Invalid function naming convention | Code quality | 8 | `addDue` did not follow Python's recommended `snake_case` naming convention. | Renamed the function to `add_due` and updated its calls. |
| Broad exception handling | Code quality / Reliability | 22 | Catching `Exception` broadly could hide unexpected errors. | Removed the broad exception handler along with the unsafe `eval()` implementation. |
| Comparison with `None` using `!=` | Style / Code quality | 29 | The expression `rows != None` did not follow the recommended Python identity-comparison style. | Simplified the function to return the list produced by the query directly. |
| Lines exceeding the permitted length | Formatting | 4, 13, 15 | Several statements exceeded Flake8's 79-character line limit. | Split long statements across multiple lines. |
| Incorrect blank-line spacing | Formatting | 12 | A top-level function did not have the required blank-line spacing before its definition. | Added the required blank lines between top-level definitions. |

## Verification

- Pylint after fixes: **10.00/10**
- Bandit after fixes: **No issues identified**
- Flake8 after fixes: **No reported violations**

The original reports were retained separately from the after-fix reports to show the findings before and after the changes.