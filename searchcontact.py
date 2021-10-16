import requests
import re

# retrieves link
link = "https://www.pfw.edu/offices/information-technology-services/about/contact"
f = requests.get(link)


# finds all numbers in xxx-xxx-xxxx format from our link in text form
num = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', f.text)
# deletes duplicate entries from all cell numbers retrieved
num = list(dict.fromkeys(num))                        

# finds all numbers in <username>@<domain_name>.<top_level_domain> format from our link in text form
mail = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', f.text) 
# deletes duplicate entries from all emails retrieved
mail = list(dict.fromkeys(mail))                    


#Prints cell numbers and emails on provided url
print("\n")
print("Cell Numbers On Page: " + str(num))
print("Emails On Page: " + str(mail))
print("\n")


