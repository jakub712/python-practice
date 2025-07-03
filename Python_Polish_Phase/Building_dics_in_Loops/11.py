def collect_even_numbers(nums: list[int]) -> set[int]:
    evens = set()

    for num in nums:
        if num %2 == 0:
            evens.add(num)
    
    print(evens)

print(collect_even_numbers([2, 4, 4, 5, 6, 7, 8, 2]))
# Output: {2, 4, 6, 8}
