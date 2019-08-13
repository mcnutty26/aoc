set of int: xpoints;
set of int: ypoints;
set of int: zpoints;
set of int: rpoints;
set of int: nbots;

array[nbots] of xpoints: x;
array[nbots] of ypoints: y;
array[nbots] of zpoints: z;
array[nbots] of rpoints: r;

var xpoints: fx;
var ypoints: fy;
var zpoints: fz;

predicate covers(int: i, var int: xp, var int: yp, var int: zp) = ((abs(x[i] - xp) + abs(y[i] - yp) + abs(z[i] - zp)) <= r[i]);

constraint fx >= x[865] -r[865];
constraint fx <= x[865] +r[865];
constraint fy >= y[865] -r[865];
constraint fy <= y[865] +r[865];
constraint fz >= z[865] -r[865];
constraint fz <= z[865] +r[865];

solve maximize sum(i in nbots)(bool2int(covers(i, fx, fy, fz)));

%output [ "Optimal position:\n" ];
%output [ "Point " ++ show(fx) ++ "," ++ show(fy) ++ "," ++ show(fz) ];
