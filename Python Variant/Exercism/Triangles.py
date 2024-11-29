def equilateral(sides):
    sideA, sideB, sideC = sorted(sides)
    return 0 < sideA == sideC


def isosceles(sides):
    sideA, sideB, sideC = sorted(sides)
    return 0 < sideA and sideC < sideA + sideB and sideB in (sideA, sideC)


def scalene(sides):
    sideA, sideB, sideC = sorted(sides)
    return 0 < sideA < sideB < sideC < sideA + sideB