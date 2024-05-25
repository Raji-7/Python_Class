def division(a,b):
    try:
        out = a/b
        return out
    except Exception as e:
        print("There is some error",e)

out = division(4,0)
print(out)
