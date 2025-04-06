class Solution(object):
    def fizzBuzz(self,n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0: 
                output.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                output.append("Fizz")
            elif (i+1) % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i+1))

        return output
    
def main(args=None):
    pass

if __name__=="__main__":
    main()