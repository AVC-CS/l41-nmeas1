def main():

    N = int(input('Enter the number N: '))
    X = range(N+1)
    result = []

    for i in X:
        powered = pow(2, i)
        print(powered)
        result.append(powered)
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
