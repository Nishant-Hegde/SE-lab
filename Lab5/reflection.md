# Reflection on Static Code Analysis

## 1. What did you learn from using Pylint, Bandit, and Flake8?

I learned that static code analysis tools examine source code to identify potential problems without executing the program. Pylint helped identify code quality and maintainability issues, Bandit detected security risks, and Flake8 identified formatting violations. Using all three provided a more complete assessment of the program.

## 2. Which issues were the most important to fix, and why?

The most important issues were the SQL injection risk and the use of `eval()`, because they could introduce security vulnerabilities. I replaced the interpolated SQL statement with a parameterized query and replaced `eval()` with direct arithmetic. I also removed the hard-coded password and corrected the mutable default argument.

## 3. What challenges did you face while fixing the issues?

One challenge was understanding that some warnings required changes to the program's logic rather than simple formatting corrections. For example, replacing `eval()` required changing the penalty function to accept numeric inputs. I also had to improve function naming, return behavior, documentation, and line formatting without changing the program's intended functionality.

## 4. How will static code analysis help you in future software development?

I will use static analysis tools during development to detect issues early, improve readability, reduce security risks, and maintain consistent coding standards. Running these tools before committing changes can help identify problems before they reach testing or production. Using multiple tools is useful because each focuses on different aspects of code quality.