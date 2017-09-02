#!/usr/bin/python3.4
import sys, os.path, os, random, string

if len(sys.argv) == 1:
  sys.exit("Enter domain!")

#vars
csrconfigTemplate = "[req]\ndistinguished_name = req_distinguished_name\nprompt = no\n\n[req_distinguished_name]\nC={}\nST={}\nL={}\nO={}\nOU={}\nCN={}\n"
cmdTemplate = "openssl req -new -sha256 -newkey rsa:2048 -nodes -config {} -keyout {} -out {}"
sslPath = "/home/staff/xxx/ssl"
domain = sys.argv[1]
csrconfig = sslPath + "/"+domain + ".csr-config"
csr = sslPath + "/" + domain + ".csr"
key= sslPath + "/" + domain + ".key"

if os.path.isfile(csrconfig):
  replace_csr = input("csr-config exists, replace? (y,n):")
  if replace_csr == "y":
    print("Ok")
  else:
    sys.exit("Exit")

country = input("Enter country[RU]: ")
state = input("Enter state[Moscow]: ")
city = input("Enter city[Moscow]: ")
organization = input("Enter organization[Vector]: ")
unit = input("Enter organization unit[Head]: ")

if country == "":
  country = "RU"
if state == "":
  state = "Moscow"
if city == "":
  city = "Moscow"
if organization == "":
  organization = "Vector"
if unit == "":
  unit = "Head"

csrConfig = open(csrconfig,'w+')
csrConfig.write(csrconfigTemplate.format(country,state,city,organization,unit,domain))
csrConfig.close()
os.system(cmdTemplate.format(csrconfig,key,csr))

if os.path.isfile(csr):
  os.system("cat " + key)
  print()
  os.system("cat " + csr)
  print("csr saved to " + csr + "; key saved to " + key)
else:
  print("Something wrong, try again")
