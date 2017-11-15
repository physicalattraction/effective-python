if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Single list comprehension
    row_sums = [sum(x) for x in matrix]
    print('row_sums: {}'.format(row_sums))

    # Double list comprehension
    flat = [x for row in matrix for x in row]
    print('flat: {}'.format(flat))

    squared = [[x ** 2 for x in row] for row in matrix]
    print('squared: {}'.format(squared))

    # Filter the matrix such that the only remaining cells are those divisible by 3 in rows that sum to 10 or higher
    filtered = [[x for x in row if x % 3 == 0]
                for row in matrix if sum(row) >= 10]
    print('filtered: {}'.format(filtered))

    # This quickly becomes too complicated. As a good rule of thumb: do not use more than two expressions:
    # 2 loops, 2 filters or 1 loop and 1 filter

    list_of_matrices = [matrix, squared]
    flat = [x for matrix in list_of_matrices for row in matrix for x in row]
    print('flat: {}'.format(flat))

    row_sums = [[sum(x) for x in matrix] for matrix in list_of_matrices]
    print('row_sums: {}'.format(row_sums))
