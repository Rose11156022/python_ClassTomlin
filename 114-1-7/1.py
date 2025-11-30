def simple_three_sum_from_input():
    input_str = input()
    
    try:
        nums = [
            int(s.strip()) 
            for s in input_str.split(',')
            if s.strip()
        ]
    except ValueError:
        print(0)
        return

    N = len(nums)
    if N < 3:
        print(0) 
        return

    distinct_sums = set()

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                current_sum = nums[i] + nums[j] + nums[k]
                distinct_sums.add(current_sum)

    print(len(distinct_sums))

if __name__ == "__main__":
    simple_three_sum_from_input()