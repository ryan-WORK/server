from rest_framework.renderers import JSONRenderer
import re


def underscore_to_camel(match):
    return match.group()[0] + match.group()[2].upper()


def camel_ize(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = re.sub(r"[a-z]_[a-z]", underscore_to_camel, key)
            new_dict[new_key] = camel_ize(value)
        return new_dict
    if isinstance(data, (list, tuple)):
        for i in range(len(data)):
            data[i] = camel_ize(data[i])
        return data
    return data


class CamelCaseJSONRenderer(JSONRenderer):

    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(camel_ize(data), *args, **kwargs)