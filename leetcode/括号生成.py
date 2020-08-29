def generateParenthesis(n):
    output = []

    def backtrack(res, left, right, n):
        if left == n and right == n:
            output.append(res)
            return output
        if left < n:
            backtrack(res + '(', left + 1, right, n)
        if right < left:
            backtrack(res + ')', left, right + 1, n)

    backtrack('', 0, 0, n)
    return output