## Agg.py

This is a quick python script that takes CSV cidr blocks at STDIN and aggregates them. 

## Usage

Example.csv contains three prefixes:

```
10.1.0.0/24,  
10.1.1.0/24,
10.1.2.0/24
```

agg.py uses the python `fileinput` module, so can either be give a file name as input or it can read from STDIN

```angular2html
./agg.py example.csv
10.1.0.0/23,  
10.1.2.0/24

Input 3 lines
Output 2 lines
```


or from STDIN
```
cat example.csv | ./agg.py           
10.1.0.0/23
10.1.2.0/24

Input 3 lines
Output 2 lines
```




