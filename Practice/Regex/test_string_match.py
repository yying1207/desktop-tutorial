import re

class TestRegexMatch:
    def __init__(self, string=None, pattern=None):
        self.string = string
        self.pattern = pattern

    def validate_string(self) -> bool:
        """
        验证字符串是否匹配正则表达式模式
        
        :return: 字符串是否匹配模式
        :rtype: bool
        """
        if self.string is None:
            raise ValueError("String must be provided")
        if not (1 <= len(self.string) <= 20 and all(char.isalnum() for char in self.string)):
            raise ValueError("String must be 1-20 characters long and contain only alphanumeric characters")
        
        return True

    
    def validate_pattern(self) -> bool:
        """
        验证正则表达式模式是否有效
        
        :return: 模式是否有效
        :rtype: bool
        """
        if self.pattern is None:
            raise ValueError("Pattern must be provided")
        
        if not (1<=len(self.pattern) <= 20 and all(char.isalnum() or char in ['.', '*'] for char in self.pattern)):
            raise ValueError("Pattern must be 1-20 characters long and contain only alphanumeric characters, '.' and '*'")
       
        return True
        

def test_regex_match(string, pattern) -> bool:
    regex_match = TestRegexMatch(string, pattern)
    assert regex_match.validate_string()
    assert regex_match.validate_pattern()

    for s_char, p_char in zip(string, pattern):
        if p_char in ['.', '*']:
            continue
        elif s_char != p_char:
            return False
        
    return True