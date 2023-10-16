def length_of_longest_substring(s):
    char_set = set()
    max_length = 0
    left, right = 0, 0

    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1

    return max_length
s=input()
print(length_of_longest_substring(s))
