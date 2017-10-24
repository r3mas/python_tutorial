#n[012].{app,fe}[01].{admin,api,core}.thw.gbr

a = ["n0","n1","n2"]
b = [".app",".fe"]
c = ["0.","1."]
d = ["admin","api","core"]
e = ".thw.gbr"

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            for l in range(len(d)):
                print a[i] + b [j] + c[k] + d[l] + e,
