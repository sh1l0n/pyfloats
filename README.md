## PyFloat Lib

Python Library for doings sums, subs, multiplications and divisions without losing precission

## How to use

```
>> import pyfloat

>> PyFloat(2.1234e-12)
'0.0000000000021234'
>> PyFloat(-2.1234e+12)
'-2123400000000'
>> PyFloat(0.1452)
'0.1452'
>> PyFloat(PyFloat(152.455))
'152.455'
>> a = PyFloat("123451.1234551230000000004444445551122000000011")
>> b = PyFloat(-8123994.000002234100000001323400000001232112221)
>> a + b
'-8000542.8765471111000000008789554448890321122199'
>> a - b
'8247445.1234573571000000017678445551134321122221'
>> a * b
'-1002916186242.9543234169148643344158458369442274183843912848765430855693663896461975553234431'
>> a == b
'False'
>> a != b
'True'
>> a > b
'True'
>>> PyFloat(0.00239419391).round(10)
'0.0023941939'
>>> PyFloat(0.00239419391).round(7)
'0.0023942'
>>> PyFloat(0.00239419391).round(4)
'0.0024'
>>> PyFloat(-1234.5678).abs()
'1234.5678'
```

## Test

```
python pytfloat_test.py
```