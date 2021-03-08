def data_type_calculator(data_type, text):
    result_str = ""
    result_num = 0

    if data_type == "int":
        result_num = int(text) * 2
        print(result_num)
    elif data_type == "real":
        result_num = float(text) * 1.5
        print(f"{result_num:.2f}")
    elif data_type == "string":
        result_str = "$" + text + "$"
        print(result_str)

data_type_input = input()
text_input = input()
data_type_calculator(data_type_input, text_input)