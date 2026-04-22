
def is_palindrome(text):
    reversed_text = ''.join(reversed(text))
    return text == reversed_text


print(is_palindrome("saippuakivikauppias"))
