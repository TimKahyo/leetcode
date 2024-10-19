class Solution:
    def romanToInt(self, s: str) -> int:
        valid_roman_numerals = ["IV", "IX", "XL","XC", "CD", "CM"]
        roman_to_integer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        new_string_list = []
        output = 0

        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in valid_roman_numerals:
                new_string_list.append(s[i:i+2])
                output += roman_to_integer[s[i:i+2]]
                i += 2
            else:
                new_string_list.append(s[i])
                output += roman_to_integer[s[i]]
                i += 1
            
        return output
