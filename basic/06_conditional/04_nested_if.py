age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not eligible (citizenship required)")
else:
    print("Underage")
