def prepare_string(string):
    # remove all spaces
    result = string.replace(' ', '')
    # unite all signs (using math rule)
    while ('--' in result or '++' in result
           or '-+' in result or '+-' in result):
        result = result.replace('--', '+')
        result = result.replace('++', '+')
        result = result.replace('-+', '-')
        result = result.replace('+-', '-')
    # add space before sign (convert binary operators to unary)
    result = result.replace('-', ' - ').replace('+', ' + ').replace('/', ' / ').replace('*', ' * ').replace('^', ' ^ ') \
        .replace('(', ' ( ').replace(')', ' ) ')
    result = [int(x) if x.isdigit() else str(x) for x in result.split()]
    for i in range(len(result) - 1):
        if (result[i] in ['*', '/'] and result[i + 1] in ['*', '/']) or result[-1] in ['+', '-', '*', '/', '^', '(']:
            return 'Invalid expression'
    for i, value in enumerate(result):
        if type(value) == str and value not in ['+', '-', '*', '/', '^', '(', ')']:
            try:
                result[i] = int(const[value])
            except (ValueError, TypeError):
                return 'Unknown variable'
    return result


def calc(input_string):
    if input_string and input_string[0] == '/' and input_string[1:] != 'help':
        return f'/Unknown command'
    elif input_string == '/help':
        return """The program calculates string with addition '+' and "
"subtraction '-' operators. It support both unary and "
"binary minus operators."""
    else:
        prep_str = prepare_string(input_string)
        if prep_str in ['Unknown variable', 'Invalid expression']:
            return prep_str
        queue = []
        stac = []
        for i in prep_str:
            if type(i) == int:
                queue.append(i)
            if i in ['+', '-', '*', '/']:
                if stac == [] or stac[-1] == '(':
                    stac.append(i)
                else:
                    if (i == '*' and (stac == [] or stac[-1] in ['-', '+'])) or (i == '/' and (stac == [] or
                                                                                               stac[-1] in ['-', '+'])):
                        stac.append(i)
                    else:
                        if i in ['*', '/']:
                            while len(stac) != 0 and stac[-1] not in ['-', '+', '(']:
                                queue.append(stac.pop())
                            stac.append(i)
                        else:
                            while len(stac) != 0 and stac[-1] != '(':
                                queue.append(stac.pop())
                            stac.append(i)
            if i == '(':
                stac.append(i)
            if i == ')':
                if '(' not in stac:
                    return 'Invalid expression'
                while stac[-1] != '(':
                    queue.append(stac.pop())
                stac.pop()
        while stac:
            queue.append(stac.pop())
    return queue


def en_cod(stack):
    if type(stack) != list:
        return stack
    answer = []
    try:
        for i in stack:
            if type(i) == int:
                answer.append(i)
            else:
                a = answer.pop()
                b = answer.pop()
                answer.append(eval(f'{b}{i}{a}'))
    except SyntaxError:
        return 'Invalid expression'
    return int(answer[-1])


def assigning_variable(input_string):
    input_string = input_string.replace(' ', '')
    left_str, right_str = input_string.split('=', 1)
    if not left_str.isalpha() or left_str == '':
        return "Invalid identifier"
    if not (right_str.isdigit() or right_str.isalpha()) or right_str == '':
        return 'Invalid assignment'
    if right_str.isalpha() and right_str in const.keys():
        const[left_str] = const[right_str]
    elif right_str.isalpha():
        return 'Unknown variable'
    else:
        const[left_str] = right_str


const = {}
input_string = input('')
while input_string != '/exit':
    if not input_string:
        input_string = input('')
        continue
    elif '=' in input_string:
        ans = assigning_variable(input_string)
        if ans != None:
            print(ans)
    elif len(input_string.split()) == 1 and input_string.split()[0].isalpha():
        if input_string in const.keys():
            print(const[input_string])
        else:
            print('Unknown variable')
    else:
        print(en_cod(calc(input_string)))
    input_string = input('')
print("Bye!")
exit()
