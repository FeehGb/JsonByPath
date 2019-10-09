import re , json, time
class JsonByPath():
    
    
    def __init__(self, **data):
        
        self._path   = re.sub(r'[\s\t\r\n](?=(\[[^\[]*\]|[^\]])*$)',"",data['path'])
        self._json   = data['json']
        self.value   = list()
        
        self.process()
        #print(self.value)

    def __repr__(self):
        return self.value
        
        
    def process(self):
        self.dict   = self.explode(self._path,"||")
        _filter     = self.onlyValidValues(self.dict)
        if len(_filter) :
            self.value = _filter[0]
        else:
            self.value = ''
            
        
    def explode(self, str_to_split, separator) :
        paths = str_to_split.split(separator)
        return list(map(self.execute, paths))
        
    #!deprecated
    def validate(self, value):
        return not isinstance(value, dict) and not isinstance(value, list)
        
        
    def onlyValidValues(self, values) :
        """ 
            Metodo para retornar valores verdadeiros
        """
        #flt = list(filter(lambda value: value is not None and value != 0, values))
        
        return [value for value in values if value  or  value == 0]
        
        
    def execute(self, path):
        value = ''
        try:
            if "&&" in path:
                plus    = self.explode(path,"&&")
                _filter = self.onlyValidValues(plus)
                value   = " ".join(map(str, plus)) if len(plus) == len(_filter) else ''
            else:
                value = self.goThroughPath(path)
            
        except ValueError as error:
            print("error: "+ error)
        return value
        
        
    
    def goThroughPath(self, path):
        path_splited  = path.split("/")
        current_value = self.tryPath(self._json, path_splited[0])
        
        if  not isinstance(current_value, dict) and not isinstance(current_value, list):
            current_value = current_value
            
        else:
            current_value = self.getValue(path_splited, current_value)
            
        return current_value
        
    def isnumber(self, value):
        try:
            float(value)
        except ValueError:
            return False
        return True
    
    
    def getValue(self, path_splited, initial_value):
        
        value = initial_value
        for index,key in enumerate(path_splited[1:]):
            try:
                key = int(key)
                
            
            except:
                pass
                
            if (not isinstance(key, int) and ("*" in key[0] or  ("[" in key and "]" in key))) and index != len(path_splited) :
                
                _charToJoin = re.findall(r"\'(.*?)\'", key)
                _charToJoin =  _charToJoin[0] if  _charToJoin else " "
                
                key1 = None
                key2 = None
                
                keyS = re.findall(r'\[(.*?)\]', key)
                if keyS :
                    keyS = keyS[0].split(":")
                    key1 , key2 = self.tryInt(keyS[0]) , self.tryInt(keyS[1])
                    
                
                
                value = self.onlyValidValues([ self.getValue(path_splited[ index +1: ],val) for val in value])
                return  _charToJoin.join(map(str, value[  key1:  key2 ] ))
                    
                
            
            else :
                value = self.tryPath(value, key)
            
        return value
        
        
    def tryInt(self, value) :
        try:
            return int(value)
        except:
            return None
        
        
    
    
    def tryPath(self, arr, key) :
        try:
            return arr[key]
        except:
            print("""
            ###### path pode estar errado #######
                PATH : {path}
                KEY  : {key}
            """.format(path=arr, key=key))
            
            return ''
            
            

if __name__ == "__main__":
    
    json_data = {
        "want": {
            "all": [
                    {"name":"value1"}
                ,   {"test":"value2"}
                ,   {"name":"value3"}
            ],
            "every": [ 
                {
                    "names":{ "data": ["value1","value2","value3", "value4","value5"] }
                }
                ,{
                    "names":{ "data": ["value1","value2","value3", "value4","value5"] }
                }
            
            ]
        }
    }
    
    path = """want/every/*'-'/names/data/[-1: ]'|'"""
    path2 = """want/all/*/name"""
    ini = time.time()
    a= JsonByPath(json=json_data, path=path)
    b= JsonByPath(json=json_data, path=path2)
    print(time.time() - ini)
    
    
    print(a.value + "\n <<<<<<< Aa")
    print(b.value )
    
    
    
    
    
    
    
    
    pass

