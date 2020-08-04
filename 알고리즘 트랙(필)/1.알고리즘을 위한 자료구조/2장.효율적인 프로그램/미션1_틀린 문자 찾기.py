def findDifference(str1, str2):
    str1_list=list(str1)
    str2_list=list(str2)
    str1_list.sort()
    str2_list.sort()
    for i in str1_list:
        if i in str2_list:
            str2_list.remove(i)
    return str2_list[0]

def main():
    print(findDifference("apple", "azlppe"))
    

if __name__ == "__main__":
    main()
