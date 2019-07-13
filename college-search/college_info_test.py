import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

from os.path import dirname, join
current_dir = dirname(__file__)
print(current_dir)

code = 0

url_loop = f"https://www.collegedata.com/en/college-profile/{code}"

r = (requests.get(url_loop))

error = "The page cannot be displayed because an internal server error has occurred."

soup = BeautifulSoup(r.text, 'html.parser')


class College:

    def __init__(self, url):
        self.college_name = [x.text for x in soup.findAll('h1')]
        self.location = [x.text for x in soup.findAll('p')]
        self.website = [x.text for x in soup.findAll('a')]
        self.pub_priv = [x.text for x in soup.findAll('div')]
        self.undergrad_count = [x.text for x in soup.findAll('span')]
        self.acceptance_rate = [x.text for x in soup.findAll('dd')]
        self.early_action = [x.text for x in soup.findAll('dd')]
        self.early_decision = [x.text for x in soup.findAll('dd')]
        self.regular_deadline = [x.text for x in soup.findAll('dd')]
        self.avg_gpa = [x.text for x in soup.findAll('dd')]
        self.sat_math = [x.text for x in soup.findAll('dd')]
        self.sat_ebrw = [x.text for x in soup.findAll('dd')]
        self.act_composite = [x.text for x in soup.findAll('dd')]
        self.attendance_cost = [x.text for x in soup.findAll('dd')]
        self.tuition = [x.text for x in soup.findAll('dd')]
        self.room_board = [x.text for x in soup.findAll('dd')]
        self.url = url
        r = (requests.get(url))

        def update_url():
            k = 0
            self.url = f"https://www.collegedata.com/en/college-profile/{k}"
            k += 1
            return url

        def set_college_name():
            college_name = [x.text for x in soup.findAll('h1')]
            return college_name

        # def update_dict():
           # college = College(update_url())
            # set_college_name()
            # return college_dict.get()

    #   def set_location():


# dic[code] = College()
# dic[code].college_name =


for key in range(6, 9):
    r = requests.get(url_loop)
    soup = BeautifulSoup(r.text, 'html.parser')
    if r.text == error:
        url_loop = f"https://www.collegedata.com/en/college-profile/{key}"
        print('Error')
        print(url_loop)
        key += 1
    else:
        url_loop = f"https://www.collegedata.com/en/college-profile/{key}"
        print(url_loop)
        school = College(url_loop)
        key += 1
        college_interest = []  # list of college data inside a list of colleges
        college_interest.append([school])
        # school.college_name[0] returns just name!
        print(school.college_name[0])


# FIX KEY += 1 ORDER
