import json
import html
import requests
from bs4 import BeautifulSoup

url = "https://careers.cognizant.com/studentandinterns/widgets"
link = []

# category = ["Technology & Engineering"]#,"Digital","Business Processes","IT Infrastructure","Delivery Management","Consulting","Corporate"]

payload = "{\"lang\":\"en_global\",\"deviceType\":\"desktop\",\"country\":\"global\",\"pageName\":\"Undergraduates Jobs\",\"ddoKey\":\"eagerLoadRefineSearch\",\"sortBy\":\"Most recent\",\"subsearch\":\"\",\"from\":0,\"jobs\":true,\"counts\":true,\"all_fields\":[\"category\",\"location\",\"empStatus\",\"industryName\",\"minExp\"],\"pageType\":\"landingPage\",\"size\":50,\"rk\":\"l-undergraduates-jobs\",\"clearAll\":false,\"jdsource\":\"facets\",\"isSliderEnable\":false,\"keywords\":\"\",\"global\":true,\"selected_fields\":{\"minExp\":[\"0\",\"1\",\"2\"],\"requiredQualification\":[\"student-undergrad\"]},\"sort\":{\"order\":\"desc\",\"field\":\"postedDate\"},\"rkstatus\":true,\"s\":\"1\"}\n"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "8584058f-693a-0a50-7a49-97f7a71cfdb1"
    }

response = requests.request("POST", url, data=payload, headers=headers)

categoryData = response.json()["eagerLoadRefineSearch"]["data"]

for job in categoryData['jobs']:
    href = "https://careers.cognizant.com/studentandinterns/global/en/job/"
    href = href + job["jobId"] + "/"
    title = ""
    title = job["title"].replace(".", "")
    title = title.replace("- ", "")
    title = title.replace(" ", "-")
    href = href + title
    link.append(href)
    job.update({'urlLink': href})
    response = requests.request(url=href, method='GET')
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find_all('script')
    parsedData = json.loads(soup.find_all('script')[1].contents[0])
    # parsedData['description']
    job.update({'description1': parsedData['description']})
    str = html.unescape(parsedData['description'])
    strSoup = BeautifulSoup(str, 'html.parser')
    job.update({'Qualification': strSoup.find("div").contents[2]})

    print(href)

    # print(href)
finalData = {}
for job in categoryData['jobs']:
    finalData.update({'cognizent-' + job['jobId']: job})
#
with open('../Json_data/freshers/cognizent.json', 'w') as outfile:
    outfile.write(json.dumps(finalData))
# print(categorys)

# baseUrl = "https://careers.cognizant.com/professionals/in/en/"
# href="https://careers.cognizant.com/professionals/in/en/job/00040152242/Sr-Associate-Projects"