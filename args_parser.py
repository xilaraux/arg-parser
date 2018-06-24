from re import match as match_re
from re import findall as findall_re
from hashable_list import List


# Organizing user-defined Exceptions
# https://stackoverflow.com/questions/4181708/python-organization-of-user-defined-exceptions-in-a-complete-project
class ParseError(TypeError):
    pass


class ArgsParser:
    def __init__(self, template: str):
        self.schema = self.parse_template(template)

    @staticmethod
    def parse_template(template: str) -> dict:
        key_pattern = '\\(\S*\|\S*\\)'
        value_pattern = '(boolean|string|numeric)'

        template_pattern = f'{key_pattern}:{value_pattern}'
        match = match_re(template_pattern, template)

        if match is None:
            raise ParseError('Incorrect template.')

        # hint how to loop through reg_exp
        # https://stackoverflow.com/questions/12870178/looping-through-python-regex-matches
        keys = List()
        for key in findall_re(key_pattern, template):
            short, long = key.strip('()').split('|')
            l = List((short, long))
            print(l)
            keys.append(l)

        values = findall_re(value_pattern, template)

        return dict(zip(keys, values))
