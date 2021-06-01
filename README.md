# Interpolate on structured grids

We interpolate the following data onto structural grids:

```
lon	lat	value
121.39	13.51	1.494
126.19	12.02	1.934
130.27	13.11	2.148
127.42	10.09	9.155
126.14	15.33	2.221
125.96	14	8.1
123.15	10.88	2.039
130.5	11.18	1.916
129.08	15.78	3.729
122.74	15.82	7.137
```

Grid points are: longitude range [121.0, 131.0] with 50 points and latitude range [10.0, 16.0] with 70 points.

We used `scipy.interpolate.griddata` for interpolation with `method='linear'`([1])

It uses triangular tessellation of input points using `qhull` (http://www.qhull.org/), and performs linear barycentric (higher weight for closer grid) interpolation. ([2])

`matplotlib.pyplot` was used for plotting, shown in `interpolated.png`.

Example in [3] was notably consulted.

## References
[1] https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html

[2] https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.LinearNDInterpolator.html

[3] https://earthscience.stackexchange.com/questions/12057/how-to-interpolate-scattered-data-to-a-regular-grid-in-python 
