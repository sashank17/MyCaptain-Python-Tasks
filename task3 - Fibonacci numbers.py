num = int(input("Enter the length of the fibonacci sequence required: "))
fn1 = 0
fn2 = 1
i = 0
print(fn1)
print(fn2)
while(i<num-2):
    fn3 = fn1 + fn2
    print(fn3)
    fn1 = fn2
    fn2 = fn3
    i += 1
