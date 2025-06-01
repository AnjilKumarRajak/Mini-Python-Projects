email=input("Enter an email")
k,j,d=0,0,0
if( len(email)>=6):
    if(email[0].isalpha()):
        if(("@"in email) and email.count("@")==1):
            if(email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                 if(i.isspace()):
                    k=1
                    continue
                 if(i.isalpha()and i.isupper()):
                    j=1
                    continue
                 if(i.isdigit()):
                    continue
                 if(i=="_",i==".",i=="@"):
                   continue
                 else:
                    d=1  
                if(k==1 or j==1 or d==1):
                  print("wrong email 5")
                else:
                    print("Right email")   
            else:
                print("wrong email 4")
                        
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")

else:
    print("wrong email 1")