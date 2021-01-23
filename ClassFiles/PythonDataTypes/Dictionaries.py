person = {
    "key": "value",
    "name": "Rich",
    "twitter": "@CarlMatson"
}
print(person['twitter'])  # @CarlMatson

print(person)  # {'key': 'value', 'name': 'Rich', 'twitter': '@CarlMatson'}

person['instagram'] = "@coding.for.everybody"

print(person)  # {'key': 'value', 'name': 'Rich', 'twitter': '@CarlMatson', 'instagram': '@coding.for.everybody'}

del person['key']

print(person)  # {'name': 'Rich', 'twitter': '@CarlMatson', 'instagram': '@coding.for.everybody'}


 