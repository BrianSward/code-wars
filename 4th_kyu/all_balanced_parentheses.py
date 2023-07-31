# https://www.codewars.com/kata/5426d7a2c2c7784365000783/python
# DESCRIPTION:
# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

# Examples
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]


def balanced_parens(n):
    def generate_parentheses(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            generate_parentheses(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            generate_parentheses(current + ")", open_count, close_count + 1)

    result = []
    generate_parentheses("", 0, 0)
    return result
