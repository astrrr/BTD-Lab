print("*** Converting hh.mm.ss to seconds ***")
raw = input("Enter hh mm ss : ")
raw0 = int(raw.split()[0])
raw1 = int(raw.split()[1])
raw2 = int(raw.split()[2])
#print(raw)
hours = ((int(raw.split()[0]) * 60)*60)
seconds = (int(raw.split()[2]))
minutes = (int(raw.split()[1]) * 60)
sumsec = hours+minutes+seconds

if raw1 > 59 or raw1 < 0 :
    print("mm({}) is invalid!".format(raw1))
  

elif raw2 > 59 or raw2 < 0 :
     print("ss({}) is invalid!".format(raw2))
   
else:
    
    print('{:02d}:{:02d}:{:02d} = {:,} seconds'.format(raw0 ,raw1 ,raw2 ,sumsec))

