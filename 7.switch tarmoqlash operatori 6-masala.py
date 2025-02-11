a=input("uzunlikni qaysi birlikda kiritmoqchisiz(for ex:dm, km, m, mm, cm): ")
b=int(input("qancha birlik:"))
def uzunlik(a):
    match a:
        case "dm":
            return(b/10)
        case "km":
            return(b*1000)
        case "m":
            return(b)
        case "mm":
            return(b/1000)
        case "cm":
            return(b/100)

print(uzunlik(a))
