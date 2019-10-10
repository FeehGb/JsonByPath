# JsonByPath
Acessar dados de um Json definido por um caminho

## Getting Started

To use copy this file in you repositorie
import JsonByPath from JsonByPath


### How to use

#### Exemple 1
- simple example 
```python

json = {
  "I": {
    "want" : "this value"
  }
}

path = "I/want"
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : this value

#### Exemple 2
- simple example 
```python

json = {
  "I": {
    "want" : ["this value"]
  }
}

path = "I/want/0"
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : this value


#### Exemple 3
- simple example to return one value and other value 
```python

json = {
  "I": {
    "want" : ["this value", "and this value"]
  }
}

path = "I/want/0 && I/want/1"
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : this value and this value

#### Exemple 4
- simple example to return one or other, return the first valid value
```python

json = {
  "I": {
    "want" : ["this value", "and this value"]
  },
  "or": { "this":"this value" }
}

path = "I/want/* || or/this"
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : this value and this value

#### Exemple 5
- simple example to return array values in a Interval 
```python

json = {
  "I": {
    "want" : ["this value", "and this value", "Just this value" ]
  }
}

path = "I/want/[-1: ]" # to return last value 
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : Just this value


#### Exemple 6
- simple example to return array values in a Interval with separator
```python

json = {
  "I": {
    "want" : ["this value", "and this value", "Maybe this value" ]
  }
}

path = "I/want/[0:2]'|'" # to return values between Keys 0 and 2 with  Pipe as separator 
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : this vale|and this value|Maybe this value


#### Exemple 7
- simple example to return array values in a Interval with separator
```python
    json = {
        "I": {
            "want": {"these" :["value1", "value2", "value3"]}
        }
    }


    # to return values between Keys 0 and 2 with  Pipe as separator
    path = "`My values:` && I/want/these/[0:2]` | `"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    
 ```
 >>> result:  My values:  value1 | value2
 
    
#### Exemple 8

```python
    json = {
        "this": {
            "path": "exist"
        }
    }

    # to return values between Keys 0 and 2 with  Pipe as separator
    path = "this/path/notExist || this/path"
    extracted = JsonByPath(json=json, path=path)
    print(extracted.value)
    
```
>>>result:  exist

## Built With

* [PYTHON](https://www.python.org/) - Python 3




## version

1.0.2

## Authors

* **Felipe Basilio** - *Initial work* - [FeehGb](https://github.com/FeehGb)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

