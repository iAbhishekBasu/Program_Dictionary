def to_roman(val):
    if type(val) is int:
        string = ''
        val = int(val)
        nums = {'M': 1000, 'CM': 900, 'D': 500, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
                'IV': 4, 'I': 1}
        while val > 0:
            for rnum in nums:
                if val >= nums[rnum]:
                    val -= nums[rnum]
                    string += rnum
                    break

        return string
    else:
        return "Please input an integer."


def from_roman(roman_num):
    if type(roman_num) is str:
        sum = 0
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i, s in enumerate(roman_num):
            if s in nums:
                if i < len(roman_num) - 1:
                    if nums[s] < nums[roman_num[i + 1]]:
                        sum += nums[roman_num[i + 1]] - nums[s]
                    else:
                        sum += nums[s]
                else:
                    if len(roman_num) > 2:
                        sum += nums[s]
                    else:
                        if len(roman_num) == 1:
                            return nums[s]
            else:
                return "The input is not a Roman Numeral."

        return sum
    return "Please input a string."
