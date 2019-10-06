import re
import json


class JsonByPath():
    
    
    def __init__(self, **data):
        
        self._path   = re.sub(r'\s|\t|\r|\n',"",data['path'])
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
        return list(filter(lambda value: value if value else '',values))
        
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
        
        
    def getValue(self, path_splited, initial_value):
        
        value = initial_value
        for index,key in enumerate(path_splited[1:]):
            try:
                key = int(key)
                
        
            except:
                pass
                
            if not isinstance(key, int) and "*" in key[0] :
                
                
                joinChar =  " " if not len(key) > 1 else key[1:]
                if index == len(path_splited) :
                    
                    value =  joinChar.join(map(str, value ))
                    print("passei aqui")
                    
                else :
                    
                    value = self.onlyValidValues([ self.getValue(path_splited[ index +1: ],val) for val in value])
                    
                    return  joinChar.join(map(str, value ))
                    
                
            else :
                value = self.tryPath(value, key)
            
        return value
        
        
    
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
        "aqui" : 1500,
        "quero": {
            "todos": [
                    {"nome":"Felipe"}
                ,   {"teste":"thiago"}
                ,   {"nome":"Helias"}
            ],
            "tudo": [ 
                {"nome":["este-nome", "teste"]}
               ,{"nome":["este-nome"]}
               ,{"nome":["este-nome"]}
               ,{"nome":["este-nome"]}
            ]
        }
    }
    
    path = """quero/todos/*,/nome || quero/tudo/*|/nome/*~"""
    path2 = """aqui"""
    
    a= JsonPath(json=json_data, path=path)
    b= JsonPath(json=json_data, path=path2)
    
    print(a.value + "\n <<<<<<< Aa")
    print(b.value )
    
    
    
    
    
    
    
    
    pass

