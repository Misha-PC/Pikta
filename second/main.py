from requests_method import get_duty_information
# from selenium_method import get_duty_information

color_ok = "\033[92m"
color_err = "\033[91m"

if __name__ == '__main__':
    code, json = get_duty_information('7840', '40913000')
    print(code)
    print(json)

    if code == 200:
        print(color_ok + "Status code: 200\n\tSuccess!")
    else:
        print(color_err + f"Status code: {code}\n\tError!")


