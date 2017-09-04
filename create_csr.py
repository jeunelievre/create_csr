#!/usr/bin/python3.4
import sys, os.path, os, random, string

if len(sys.argv) == 1:
  sys.exit("Enter domain!")

#vars
csrconfigTemplate = "[req]\ndistinguished_name = req_distinguished_name\nprompt = no\n\n[req_distinguished_name]\nC={}\nST={}\nL={}\nO={}\nOU={}\nCN={}\n"
cmdTemplate = "openssl req -new -sha256 -newkey rsa:2048 -nodes -config {} -keyout {} -out {}"
sslPath = "/home/staff/r_akobzar/ssl"
domain = sys.argv[1]
csrconfig = sslPath + "/"+domain + ".csr-config"
csr = sslPath + "/" + domain + ".csr"
key= sslPath + "/" + domain + ".key"

defaultCountry="RU"
defaultState="Moscow"
defaultCity="Moscow"
defaultOrganization="1Gb.ru"
defaultUnit="Head"

if os.path.isfile(csrconfig):
  replace_csr = input("csr-config exists, replace? (y,n):")
  if replace_csr == "y":
    print("Ok")
  else:
    sys.exit("Exit")

country = input("Enter country ["+defaultCountry+"]: ")
state = input("Enter state ["+defaultState+"]: ")
city = input("Enter city ["+defaultCity+"]: ")
organization = input("Enter organization ["+defaultOrganization+"]: ")
unit = input("Enter organization unit ["+defaultUnit+"]: ")

if country == "":
  country = defaultCountry
if state == "":
  state = defaultState
if city == "":
  city = defaultCity
if organization == "":
  organization = defaultOrganization
if unit == "":
  unit = defaultUnit

csrConfig = open(csrconfig,'w+')
csrConfig.write(csrconfigTemplate.format(country,state,city,organization,unit,domain))
csrConfig.close()
result=os.system(cmdTemplate.format(csrconfig,key,csr))

if result == 0:
  os.system("cat " + key)
  print()
  os.system("cat " + csr)
  print("csr saved to " + csr + "; key saved to " + key)
else:
  print("Something wrong, try again")