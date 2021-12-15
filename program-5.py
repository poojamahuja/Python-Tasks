s = "in publishing and graphic design"
while s != "":
   slen0 = len(s)
   ch = s[0]
   s = s.replace(ch, "")
   slen1 = len(s)
   if slen1 == slen0-1:
      print ("First unique character is: ",ch)
      break;
   