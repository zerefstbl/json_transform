import ast
import json as j


class JsonTransform:
    def __init__(self):
        with open('input1.txt', 'r') as file:
            old_json = file.read()
            self.json = ast.literal_eval(old_json)

    def main(self):
        self.new_json(self.json)

    def new_json(self, json: dict) -> dict:
        teste2 = {}

        for k, v in json.items():
            if len(v.keys()) > 1:
                for key in v.keys():
                    value = v.get(key)
                    if isinstance(value, list):
                        items = enumerate(value)
                        for i, item in items:
                            teste2[f'{k}/{key}/{i}'] = item
                    else:
                        teste2[f'{k}/{key}'] = value
                continue

            item, value = v.popitem()

            if isinstance(value, dict):
                sub_item, sub_value = value.popitem()
                teste2[f'{k}/{item}/{sub_item}'] = sub_value

        with open('new_json.txt', 'w') as file:
            j.dump(teste2, file, indent=4)


if __name__ == '__main__':
    json_transform = JsonTransform()
    json_transform.main()
