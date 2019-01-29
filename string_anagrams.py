# Validate anagrams

def validate_anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Strings are anagrams")
        return True
    else:
        print("Strings are not anagrams")
        return False

if __name__ ==  '__main__':
    s1 = input()
    s2 = input()
    validate_anagrams(s1, s2)