def myfunction(n):
    
    first_loop_complexity = "O(n)"
    for i in range(0, n+1):
        print("First Loop")

    
    second_loop_complexity = "O(log n)"
    j = 1
    while j <= n+1:
        print("Second Loop", j)
        j = j * 2


    third_loop_complexity = "O(1)"
    for i in range(0, 100):
        print("Third Loop")

   
    print("\nTime Complexities:")
    print("First Loop  :", first_loop_complexity)
    print("Second Loop :", second_loop_complexity)
    print("Third Loop  :", third_loop_complexity)

    print("\nTotal Time Complexity: O(n)")



n = int(input("Enter n: "))
myfunction(n)
