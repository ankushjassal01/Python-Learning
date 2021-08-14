# params
# keyword or positional params
# (var, name=var)
# var-positional
# (*args)
# var-keyword
# (**kwargs)
# keyword only: that can defined as keyword or *, it must be call with its defined keyword
# like if k or p then call it with k or p
# positional only  :: that can be supplied only by position
# VAR-POSITIONAL and positional only & keyword only and var-keyword only
# var are parameters which start from * or **.. it must comes after positional or keywords arguments if those used
# positional only are the params which used in high level of coding in C func
# keyword only
# variable defined after var-positional params must be keyword only  it includes var-keywords args
# sequence is :
# positional Or keyword arguments --VAR-POSITIONAL -- keyword only -- var-keyword only
a=['math','car']


def func(p1, p2, *args,p,k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{} {}".format(p,k))
    print("var-keyword:.............{}".format(kwargs))


# here 1,2 are positional and then (3,4,5,9) are var-positional then keyword only k=6 and then var-keyword key1,key2
func(1, 2, 3, 4, 5, 9, k=1, key1=7, key2=8,p=6)
# here keyword used first but value of a will be pass as positional and then empty tuple as var-positional and then
# keyword k=6 and then var-keyword name, kwy1,key2
print()
func(name=1, *(a), p=6,k=1, key1=7, key2=8)
# only positional and keyword only args
print()
func(1,2,p=8,k=2)

