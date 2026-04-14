def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(current, target):
        if current > target:
            print("Harvest time!")
            return
        print(f"Day {current}")
        helper(current + 1, target)

    helper(1, days)
