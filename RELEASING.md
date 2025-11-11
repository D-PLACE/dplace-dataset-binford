# Releasing Carneiro

```shell
cldfbench download cldfbench_binford.py
```

```shell
cldfbench makecldf cldfbench_binford.py --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench cldfviz.map cldf --pacific-centered --format png --width 20 --output map.png --with-ocean --no-legend
```

```shell
cldferd --format compact.svg cldf > erd.svg
```

```shell
cldfbench readme cldfbench_binford.py
cldfbench zenodo --communities dplace cldfbench_binford.py
dplace check cldfbench_binford.py
```
