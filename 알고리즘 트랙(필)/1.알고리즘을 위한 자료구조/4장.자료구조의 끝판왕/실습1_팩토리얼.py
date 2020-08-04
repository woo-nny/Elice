def factorial(num):
	if num ==0:
		return 1
	return factorial(num-1)*num
    
    # x=1
    # for each range(1,num+1):
    #     x = x*each
    # return x
	
	

def main():
    print(factorial(5)) # should return 120

if __name__ == "__main__":
    main()