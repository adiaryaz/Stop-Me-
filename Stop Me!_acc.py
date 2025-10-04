def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def stop_me_app():
    count = 0
    while True:
        user_input = input().strip()
        if user_input.lower() == "stop":
            break
        print("RUN")
        count += 1
    
    total_runs = factorial(count)
    print(f"Total {total_runs} runs")
stop_me_app()