class TestIPAddress:

    def is_ipv4_address(self, string: str) -> bool:
        """
        is_ipv4_address 的 Docstring
        
        :param string: 0-255 的十进制数字，四个数字之间用点分隔
        :type string: str
        :return: 是否是有效的 IPv4 地址
        :rtype: bool
        """
        digital_list = string.split('.')
        if len(digital_list) != 4:
            return False
        for digital in digital_list:
            if not digital.isdigit():
                return False
            if digital[0] == '0' and len(digital) > 1:
                return False
            if not 0 <= int(digital) <= 255:
                return False
        return True

    def is_ipv6_address(self, string: str) -> bool:
        """
        is_ipv6_address 的 Docstring
        
        :param string: 
            x1:x2:x3:x4:x5:x6:x7:x8
            1 <= xi.length <= 4
            xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
            在 xi 中允许前导零
        """
        hex_list = string.split(':')
        if len(hex_list)!=8:
            return False
        for hex in hex_list:
            if len(hex) < 1 or len(hex) > 4:
                return False
            for char in hex:
                if not (char.isdigit() or 'a' <= char.lower() <= 'f'):
                    return False
        return True

    def test_ip_address(self, string: str) -> str:
        if self.is_ipv4_address(string):
            return "IPv4"
        elif self.is_ipv6_address(string):
            return "IPv6"
        else:
            return "Neither"

