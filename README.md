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

path = "I/want/1 && I/want/1"
extracted = JsonByPath(json=json, path=path)
print( extracted.value )
```
>>> result : this value and this value

#### Exemple 4
- simple example to return one or other, return the first values valid
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

## Built With

* [PYTHON](https://www.python.org/) - Python 3




## version

1.0.0

## Authors

* **Felipe Basilio** - *Initial work* - [FeehGb](https://github.com/FeehGb)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

