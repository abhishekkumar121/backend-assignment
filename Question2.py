import re
import requests
from bs4 import BeautifulSoup

# Taking input website
url = input("Enter website URL: ")

# Making HTTP request to the website
response = requests.get(url)

# Parsing HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting social links
social_links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and ('facebook' in href or 'linkedin' in href):
        social_links.append(href)
print("Social links:")
for link in social_links:
    print(link)

# Extracting emails
email_tag = soup.find('a', href=re.compile(r'^mailto:'))
if email_tag:
    email = email_tag['href'][7:]  # Removing 'mailto:'
    print("Email:", email)
else:
    print("No email found.")


# Extracting contact
contact_tag = soup.find('a', href=re.compile(r'^tel:'))
if contact_tag:
    contact = contact_tag['href'][4:]  # Removing 'tel:'
    print("Contact:", contact)
else:
    print("No contact found.")
