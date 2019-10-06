# JsonByPath
Acessar dados de um Json definido por um caminho

## Getting Started

To use copy this file in you repositorie
import JsonByPath from JsonByPath


### How to use

#### Exemple 1

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
result : this value

## Built With

* [PYTHON](https://www.python.org/) - Python 3




## version

1.0.0

## Authors

* **Felipe Basilio** - *Initial work* - [FeehGb](https://github.com/FeehGb)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

