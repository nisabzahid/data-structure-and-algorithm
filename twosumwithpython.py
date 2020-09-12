class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        seen ={}
        
        for i, num in enumerate(numbers):
            dif = target_sum - num
            if dif in seen:
                return i, seen[dif]
            seen[num] = i
        return (-1,-1)

print(TwoSum.find_two_sum([1, 3, 5, 7, 9], 12))
