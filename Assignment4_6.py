hours = raw_input("Enter hours:")
hr = float(hours)
rateOfPay = raw_input("Enter rate:")
rat = float(rateOfPay)

def computepay(hrs, rat):
    if hrs > 40:
        totalPayAmt = (40*rat)+((hrs-40)*(rat*1.5))
        return totalPayAmt
    else:
        totalPayAmt = hrs * rat
        return totalPayAmt

totAmt = computepay(hr,rat)
print totAmt