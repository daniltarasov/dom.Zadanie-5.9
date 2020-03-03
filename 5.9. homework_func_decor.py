

def time_this(num_runs):
    import time
    def decorator(func):
        def wrapper(*args, **kwargs):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return wrapper

    return decorator


@time_this(100)
def f():
    for j in range(1_000_000):
        pass


f()
