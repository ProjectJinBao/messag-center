import re


content = [
  {
    "content": "['']",
    "msgtype": "markdown",
    "name": "string"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "text",
    "name": "vrf"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "text",
    "name": "\u4f60\u597d9439b74a-9ef5-11ea-a46c-0242ac120003"
  },
  {
    "content": "['']",
    "msgtype": "text",
    "name": "name"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d2c0cb65e-9eff-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d492a2884-9eff-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d6be71a4e-9eff-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597daa0488c0-9eff-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d66f6aea2-9f02-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597db593f5a6-9f02-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "text",
    "name": "\u4f60\u597dbd7a6ad4-9f02-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597dbd95a1fa-9f02-11ea-be0b-0242ac120003"
  },
  {
    "content": "['eiji']",
    "msgtype": "text",
    "name": "\u4f60\u597dbda991b0-9f02-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597ddb5128a4-9f02-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "text",
    "name": "\u4f60\u597d219ffd08-9f03-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d54cac528-9f03-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d58855e80-9f03-11ea-be0b-0242ac120003"
  },
  {
    "content": "['hello world\uff01']",
    "msgtype": "markdown",
    "name": "\u4f60\u597d707fe27a-9f27-11ea-be0b-0242ac120003"
  },
  {
    "content": "['jjj:jj']",
    "msgtype": "text",
    "name": "ll"
  },
  {
    "content": "['jjj:jji']",
    "msgtype": "text",
    "name": "llii"
  },
  {
    "content": "['']",
    "msgtype": "text",
    "name": "namwwe"
  }
]

# def _extract_field_with_regex(field,text):
#
#     matched = re.search(field, text)
#     print(matched)
#     print(matched.group())
#
#
# _extract_field_with_regex(r'(?<=msgtype":).*(?=,)',str(content))




# 将匹配的数字乘以 2
def double(matched):
  value = int(matched.group('value'))
  return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))



