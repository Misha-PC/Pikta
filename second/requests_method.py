import requests


def get_duty_information(ifns: str, oktmmf: str) -> (int, dict):
    """
    :param ifns:    Код ИФНС
    :param oktmmf:  Муниципальное образование:
    :return: (status_code, result)
    """

    url = "https://service.nalog.ru/addrno-proc.json"

    request_params = {
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        },
        "body": f"c=next&step=1&ifns={ifns}&oktmmf={oktmmf}"
    }

    response = requests.post(url, headers=request_params["headers"], data=request_params["body"], )
    json = response.json()
    return response.status_code, json

