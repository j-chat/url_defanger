'''
This script is to be executed in an IDE such as Spyder, PyCharm, etc. for Python 3

ARGUMENTS:
  url: user will paste the url through console after colon
  
 OUTPUTS:
  a defang url in the form of hxxp[:]//somedomain
  
  '''
  
  url = input("URL please: ")
  url = url.replace(".", "[.]")
  url = url.replace(":", "[:]")
  url = url.replace("http", "hxxp")
  print(url)
  
  #References
  #https://github.com/jamesdietle/Fanger
