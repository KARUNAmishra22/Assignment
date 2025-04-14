principal=float (input ("Enter the principle amount:"))
rate=float (input ("Enter the rate of interest(in%):"))
time=float (input ("Enter the time period (in years):"))
simple_interest=(principal*rate*time)/100
print (f"The Simple Interest for a principal of {principal:.2f} at {rate:.2f} % for {time:.2f} years        is: {simple_interest:.2f}")