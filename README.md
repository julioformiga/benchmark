# Benchmark for test Python + CFFI integration

## Compile

```console title="./nbody/$"
python compile.py
```

## Execute

```console title="./$"
python main.py
```
```console
N-Body - Python [your version] with C module
-0.169074954
-0.169300938
Time: 3.6226315519998025

N-Body - Python [your version]
-0.169074954
-0.169300937
Time: 287.7175698539995
```

# References

- https://cffi.readthedocs.io/en/latest/overview.html
- https://sschakraborty.github.io/benchmark/nbody.html
