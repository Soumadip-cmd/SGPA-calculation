# sgpa calculator---->>>...

n=int(input("\n\tHow Many Subject you have: "))
sub_l=[]
credit_l=[]
num_l=[]
total=0
s=0
want=(input("\n\tDo You want Shortcut Calculation:[Enter 'y' else 'n']: "))

for i in range(n):
    if want=='y':
        credit_score=float(input("\n\tEnter Credit-point: "))
        num=int(input("\n\tHow Much Point You Got(sgpa-format(5-10)): "))
        credit_l.append(credit_score)
        num_l.append(num)
        s+=(credit_score*num)
        total+=(credit_score*10)
    else:
        sub=(input("\n\tEnter Subject Name: "))
        credit_score=float(input("\n\tEnter Credit-point: "))
        num=int(input("\n\tHow Much Point You Got(sgpa-format(5-10)): "))
        sub_l.append(sub)
        credit_l.append(credit_score)
        num_l.append(num)
        s+=(credit_score*num)
        total+=(credit_score*10)
if want=='y':
    for j in range(n):
        print("\n\t(credit-score)-({}) You got:{}".format(credit_l[j],num_l[j]))
else:
    for j in range(n):
        print("\n\t{}:- (credit-score)-({}) You got:{}".format(sub_l[j].capitalize(),credit_l[j],num_l[j]))
sgpa=0
sgpa=(s/total)*10
print('\n\tYour Sgpa is- ',sgpa)
