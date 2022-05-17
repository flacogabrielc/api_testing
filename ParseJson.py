import json

odics = '{"K1":"val1","K2":"val2"}'
json_result = json.loads(odics)
print(json_result['K1'])
print(json_result)