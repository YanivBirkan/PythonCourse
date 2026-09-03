from token import STRING


def get_avg():
    with open("./files/data.txt", "r") as file_local:
        data = file_local.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    return sum(values)

#
# avg = get_avg()
# print(avg)
def square_number():
    number = 5
    result = pow(number, 2)
    return result


print(square_number())