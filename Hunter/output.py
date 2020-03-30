def output_list(liss, output_format, col_name):
    try:
        if output_format == '' or col_name == '':
            return liss
        output = output_format.format(*col_name) + '\n'
        for i in liss:
            output += ''.join(output_format.format(*i) + '\n')
        return output
    except Exception:
        return 'sth wrong with output'


if __name__ == '__main__':
    lis = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # lis2 = ['Harrier', 'GET', 'POST', 'text', 'json', 'header', 'content']
    col_name = ['a', 'b', 'c']
    output_format = "{0}-{1}-{2}"
    # print(*col_name)
    # print(output_format.format(*col_name))
    print(output_list(lis, output_format, col_name))
