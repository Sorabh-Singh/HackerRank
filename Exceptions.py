for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


# except Exception as e:
#     print(e)
#     print("exception type is ", type(e).__name__)
#     c = None

# 3
# 1 0
# 2 $
# 3 1