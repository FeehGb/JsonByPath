import re, json
class JsonByPath():

    def __init__(self, **data):

        self.path = re.sub(
            r'[\s\t\r\n](?=(\`[^\`]*\`|[^\`])*$)', "", data['path']
        )
        self.jsonIn = data['json']
        self.value = list()
        self.error_path = list()

        self.process()
        
        self.current_path = ''
        # print(self.value)

    def __repr__(self):
        return self.value

    def process(self):
        self.all = self.explode(self.path, "||")
        _filter = self.onlyValidValues(self.all)
        if len(_filter):
            self.value = _filter[0]
        else:
            self.value = ''

    def explode(self, str_to_split, separator):
        paths = str_to_split.split(separator)
        return list(map(self.execute, paths))

    def onlyValidValues(self, values):
        """ 
            Metodo para retornar valores verdadeiros
        """
        #flt = list(filter(lambda value: value is not None and value != 0, values))

        return [value for value in values if value or value == 0]

    def execute(self, path):
        # save path to show log.
        self.current_path = path
        value = ''
        try:
            if "&&" in path:
                plus = self.explode(path, "&&")
                _filter = self.onlyValidValues(plus)
                value = " ".join(map(str, plus)) if len(
                    plus) == len(_filter) else ''
            else:
                value = self.goThroughPath(path)

        except ValueError as error:
            print("error: " + error)
        return value

    def goThroughPath(self, path):

        has_quote = re.findall(r'\`(.*?)\`', path)
        if not "/" in path and len(has_quote):
            return has_quote[0]

        path_splited = path.split("/")
        current_value = self.tryPath(self.jsonIn, path_splited[0])

        # if  not isinstance(current_value, dict) and not isinstance(current_value, list):
        #    current_value = current_value

        # else:
        return self.getValue(path_splited, current_value)

        # return current_value

    def isnumber(self, value):
        try:
            float(value)
        except ValueError:
            return False
        return True

    def getValue(self, path_splited, initial_value):

        value = initial_value
        for index, key in enumerate(path_splited[1:]):
            try:
                key = int(key)

            except:
                pass

            if ( key != '' and not isinstance(key, int) and ("*" in key[0] or ("[" in key and "]" in key))) and index != len(path_splited):

                _charToJoin = re.findall(r"\`(.*?)\`", key)
                _charToJoin = _charToJoin[0] if _charToJoin else " "

                key1 = None
                key2 = None

                keyS = re.findall(r'\[(.*?)\]', key)
                if keyS:
                    keyS = keyS[0].split(":")
                    key1, key2 = self.tryInt(keyS[0]), self.tryInt(keyS[1])

                value = self.onlyValidValues(
                    [self.getValue(path_splited[index + 1:], val) for val in value])
                return _charToJoin.join(map(str, value[key1:  key2]))

            else:
                value = self.tryPath(value, key)

        return value

    def tryInt(self, value):
        try:
            return int(value)
        except:
            return None

    def tryPath(self, arr, key):
        try:
            return arr[key]
        except:

            self.error_path.append(f"PATH:{self.current_path} - KEY: {key or None}")

            """print(
            ###### path pode estar errado #######
                PATH : {path}
                KEY  : {key}
            .format(path=self.current_path, key=key))"""

            return ''


if __name__ == "__main__":

    #Exemple 1
    #simple example
    json = {
        "I": {
            "want": "this value in a dict"
        }
    }

    path = "I/want"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result: this value

    #Exemple 2
    #simple example
    json = {
        "I": {
            "want": ["this value in a list"]
        }
    }

    path = "I/want/0"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result: this value

    #Exemple 3
    #simple example to return one value and other value
    json = {
        "I": {
            "want": ["this value in a list", "and this value in a list"]
        }
    }

    path = "I/want/0 && I/want/1"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result: this value and this value

    #Exemple 4
    #simple example to return one or other, return the first valid value
    json = {
        "I": {
            "want": ["this value", "and this value"]
        },
        "or": {"this": "this value"}
    }

    path = "I/want/* || or/this"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result: this value and this value

    #Exemple 5
    #simple example to return array values in a Interval
    json = {
        "I": {
            "want": ["this value", "and this value", "Just this value"]
        }
    }

    path = "I/want/[-1: ]"  # to return last value
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result: Just this value

    #Exemple 6
    #simple example to return array values in a Interval with separator
    json = {
        "I": {
            "want": ["this value", "and this value", "Maybe this value"]
        }
    }

    # to return values between Keys 0 and 2 with  Pipe as separator
    path = "I/want/[0:2]`|`"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result: this vale | and this value | Maybe this value

    #Exemple 7
    #simple example to return array values in a Interval with separator
    json = {
        "I": {
            "want": {"these": ["value1", "value2", "value3"]}
        }
    }

    path = "`My values:` && I/want/these/[0:2]` | `"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result:  My values:  value1 | value2

    #Exemple 8
    #simple example to return first valid value
    json = {
        "this": {
            "path": "exist"
        }
    }

    path = "this/path/notExist || this/path"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    #result:  exist
    
    


pass
