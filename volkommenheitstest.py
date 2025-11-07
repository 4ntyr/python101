def check(input):
    a = 0
    for i in range(1,input):
        if input % i ==0:
            a += i
    if a == input:
        return("Volkommenheit und Perfektion :)")
    else:
        return("Unvollkommen und fehlerbehaftet") 
    
        
print(check(int(input("Zu überprüfende Zahl:"))))