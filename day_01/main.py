def clean_numbers():
     with open("day_01/data.txt") as file:
        nums = file.readlines()
        clean_nums = []
        for num in nums:
            stripped_num = num.strip("\n")
            clean_nums.append(int(stripped_num))
        return clean_nums 


def solve():
    nums = clean_numbers()
    target_nums= []
    print(nums)
    for num in nums: 
        if num in target_nums:
            print(":D")
            partner = 2020 - num
            print(num*partner)
            break
        else:
            target_nums.append(2020 - num)

   


if __name__ == "__main__":
    solve()