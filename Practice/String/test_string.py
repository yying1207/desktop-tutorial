class TestString:
    def switch_case(self, s: str) -> str:
        """
        Hello World -> hELLO wORLD
        """
        return ''.join(char.lower() if char.isupper() else char.upper() for char in s)
    
    def switch_order(self, s: str) -> str:
        """
        Hello World -> World Hello
        """
        return ' '.join(s.split()[::-1])
    

def test_switch_case_and_order():    
    test_string = TestString()
    switch_case_string = test_string.switch_case("Hello World")
    switch_order_string = test_string.switch_order(switch_case_string)

    assert switch_order_string == "hELLO wORLD"