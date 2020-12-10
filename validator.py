import os
import json
from jsonschema import Draft3Validator

for schema in os.listdir('./schema'):
    with open(schema, 'r') as s:
        data_s = json.load(s)

    for file in os.listdir('./event'):
        with open(file, 'r') as f:
            data_f = json.load(f)
            v = Draft3Validator(data_s)
            for error in sorted(v.iter_errors(data_f), key=str):
                TODO = ''
                if 'is a required property' in error.message:
                    TODO = 'Это обязательно к заполнению поле'
                elif 'None is not of type' in error.message:
                    TODO = 'Невозможно оставить поле пустым'
                elif 'is not of type' in error.message:
                    TODO = 'Введите данные в соотвествии с требуемым типом'
                with open('example_file.html', 'a') as out:
                    out.write(
                        f'<table>'
                        f'  <tbody>'
                        f'      <tr>'
                        f'         <td>Невалидный файл: {file}</td>'
                        f'      </tr>'
                        f'      <tr>'
                        f'         <td>Найдена ошибка:  {error.message}<td>'
                        f'      </tr>'
                        f'      <tr>'
                        f'         <td>     Пояснение: {TODO}<td>'
                        f'      </tr>'
                        f'      <tr>'
                        f'         <td>\n<td>'
                        f'      </tr>'
                        f'  </tbody'
                        f'</table>')