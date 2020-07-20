def clock_angle_problem(hr: int, min: int) -> float:

    delta = abs(.5 * (60 * hr - 11 * min))
    return 360 - delta if delta > 180 else delta


if __name__ == "__main__":
    print(clock_angle_problem(2,20))
    print(clock_angle_problem(10,16))
    print(clock_angle_problem(5,45))


