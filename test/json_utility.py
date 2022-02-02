import codecs
from json import load


def read_json_file(file_path: str) -> dict:
    with codecs.open(file_path, encoding='utf8') as fp:
        json_context = load(fp)
    return json_context


def parse_json(json: dict) -> dict:
    def pars_part(json_: dict, item_name: str, target: str) -> dict:
        """
        :param json_: input dictionary
        :param item_name: searching region
        :param target: target field name (dict key)
        :return:
        """
        result = {}
        for dict_ in json_[item_name]:
            properties = dict_['properties']
            x = properties['X']
            if x not in result.keys():
                result.update({x: list()})
            result[x].append(properties[target])
        return result

    result = {}
    raw = {
        'headers': pars_part(json, 'headers', 'QuickInfo'),
        'values': pars_part(json, 'values', 'Text'),
        'Y': pars_part(json, 'values', 'Y')
    }

    for key in raw['headers'].keys():
        sorted_val = {}

        for y_, v_ in zip(raw['Y'][key], raw['values'][key]):
            sorted_val.update({y_: v_})

        result.update({raw['headers'][key][0]: sorted_val})
    return result

