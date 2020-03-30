import unittest
import JsonByPath

class tests(unittest.TestCase):
    def test_01(self):
        json = {
                "I": {
                    "want": "this value in a dict"
                }
            }
        path = "I/want"
        
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'this value in a dict')
        
    #Exemple 2
    #simple example
    def test_02(self):
        
        json = {
            "I": {
                "want": ["this value in a list"]
            }
        }

        path = "I/want/0"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'this value in a list')
        #result: this value in a list

    #Exemple 3
    #simple example to return one value and other value
    def test_03(self):
        
        json = {
            "I": {
                "want": ["this value in a list", "and this value in a list"]
            }
        }

        path = "I/want/0 &&``&& I/want/1"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'this value in a listand this value in a list')
        #result: this value in a listand this value in a list

    #Exemple 4
    #simple example to return one or other, return the first valid value
    def test_04(self):
        
        json = {
            "I": {
                "want": ["this value", "and this value"]
            },
            "or": {"this": False}
        }

        path = "I/want/* || or/this"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'this value and this value')
        #result: this value and this value

    #Exemple 5
    #simple example to return array values in a Interval
    def test_05(self):
        
        json = {
            "I": {
                "want": ["this value", "and this value", "Just this value"]
            }
        }

        path = "I/want/[-1: ]"  # to return last value, or I/want/-1"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'Just this value')
        #result: Just this value

    #Exemple 6
    #simple example to return array values in a Interval with separator
    def test_06(self):
        
        json = {
            "I": {
                "want": ["this value", "and this value", "Maybe this value"]
            }
        }

        # to return values between Keys 0 and 2 with  Pipe as separator
        path = "I/want/[0:2]`|`"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'this value|and this value')
        #result: this value|and this value

    #Exemple 7
    #simple example to return array values in a Interval with separator
    def test_07(self):
        
        json = {
            "I": {
                "want": {"these": ["value1", "value2", "value3"]}
            }
        }

        path = "`My values: ` && I/want/these/[0:2]` | `"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'My values: value1 | value2')
        #result:My values: value1 | value2

    #Exemple 8
    #simple example to return first valid value
    def test_08(self):
        
        json = {
            "this": {
                "path": "exist"
            }
        }

        path = "this/path/doesnotexist || this/path"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, 'exist')
        #result:  exist


    #Exemple 9
    #simple example to return one or other, return the first valid value
    def test_09(self):
        
        json = {
            "I": {
                "want": ["this value", "and this value"]
            },
            "or": {"this": False}
        }
        #                                      |---> path does not exist
        #                        |---> path exists
        #           |---> path does not exist |
        #           |           |            |
        path = "I/wants/* || or/this || or/these"
        extracted = JsonByPath(json=json, path=path)
        self.assertEqual(extracted.value, False)
        #result: False
        
    
    

if __name__ == '__main__':
    unittest.main()