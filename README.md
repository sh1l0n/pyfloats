## pyFloat

Python Library for doings sums, subs, multiplications and divisions without losing precission. All operations are using strings for computing the result

## How to use

```
>> import pyfloat

>> a = "123451.1234551230000000004444445551122000000011"
>> b = "-8123994.000002234100000001323400000001232112221"
>> sum = pyfloat.sum(a, b)
'-8000542.8765471111000000008789554448890321122199'
>> sub = pyfloat.sub(a, b)
'8247445.1234573571000000017678445551134321122221'
>> mul = pyfloat.mul(a, b)
'-100291618624295432341691486433441584583694422741838.4391284876543085569366389646197555323443'
```

## Test

```
python pytfloat_test.py
```