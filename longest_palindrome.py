def all_substrings(string):
    substrings=[]
    for i in reversed(range(len(string)+1)):
        ptr_start=0
        ptr_end=i       #ptr_end = ptr_start + i
        while ptr_end <= len(string):
            substring = string[ptr_start:ptr_end]
            ptr_start+=1
            ptr_end+=1
            substrings.append(substring)
    return substrings

def is_palindrome(string):
    if len(string)<=1:
        return True
    else:
        if(string[0]==string[-1]):
            return True and is_palindrome(string[1:-1])
        else:
            return False
def longest_palindrome(string):
    substrings=all_substrings(string)
    for substring in substrings:
        if is_palindrome(substring):
            return substring

def odd_palindrome(string):
    n=len(string)
    palindrome_bool = [0]*n

    start_ptr=0
    end_ptr=0
    palindrome_substring=(start_ptr, end_ptr)
    for i in range(len(string)):
        if i>0 and i<len(string)-1:
            if(string[i-1]==string[i+1]):
                palindrome_bool[i]=1
                if start_ptr==0:
                    start_ptr=i
            else:
                palindrome_bool[i]=0
                if start_ptr!=0:
                    end_ptr=i
                    if palindrome_

if __name__ == '__main__':
    print(longest_palindrome('abbababababaaaaaa'))
