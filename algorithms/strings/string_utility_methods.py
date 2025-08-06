def reverse_string(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

def remove_duplicates(s):
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)

    return ''.join(result)

def test_string_functions():
    """Test all three string utility functions"""
    
    # Test reverse_string
    print("Testing reverse_string...")
    s1 = ['h', 'e', 'l', 'l', 'o']
    reverse_string(s1)
    assert s1 == ['o', 'l', 'l', 'e', 'h'], f"Expected ['o', 'l', 'l', 'e', 'h'], got {s1}"
    
    s2 = ['a', 'b']
    reverse_string(s2)
    assert s2 == ['b', 'a'], f"Expected ['b', 'a'], got {s2}"
    print("   ✅ reverse_string passed")
    
    # Test is_palindrome
    print("Testing is_palindrome...")
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Madam") == True
    print("   ✅ is_palindrome passed")
    
    # Test remove_duplicates
    print("Testing remove_duplicates...")
    assert remove_duplicates("hello") == "helo"
    assert remove_duplicates("aabbcc") == "abc"
    assert remove_duplicates("abcabc") == "abc"
    assert remove_duplicates("") == ""
    assert remove_duplicates("a") == "a"
    print("   ✅ remove_duplicates passed")
    
    print("🎉 All string utility functions working correctly!")

# Run tests after implementing your functions
if __name__ == "__main__":
    test_string_functions()
