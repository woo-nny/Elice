def isAnagram(str1, str2):
    #첫번쨰 방법(배열)
    # str1List = list(str1)
    # str2List = list(str2)
    # str1List.sort()
    # str2List.sort()
    # if str1List == str2List:
    #     return True
    # return False
    # return (str1List == str2List)
    # 두번째 방법(해쉬)
    dic1 = {}
    for ch in str1:
        dic1[ch] = dic1.get(ch,0) +1
    
    for ch in str2:
        if ch in dic1:
            if dic1[ch] == 0:
                return False
            else:
                dic1[ch] -=1
        else:
            return False
    return True
        


def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
