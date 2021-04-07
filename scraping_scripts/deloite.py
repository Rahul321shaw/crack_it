import json
import requests
from bs4 import BeautifulSoup


url = "https://jobs2.deloitte.com/widgets"
payload = '{"lang":"en_ui","deviceType":"desktop","country":"ui","pageName":"Experienced-all-jobs","ddoKey":"eagerLoadRefineSearch","sortBy":"Most recent","subsearch":"","from":0,"jobs":true,"counts":true,"all_fields":["city","state","category","type","organizationFunction","country"],"pageType":"landingPage","size":"10","rk":"l-experiencedalljobs","clearAll":false,"jdsource":"facets","isSliderEnable":false,"keywords":"","global":true,"selected_fields":{"type":["Experienced"]},"sort":{"order":"desc","field":"postedDate"},"rkstatus":true,"s":"1"}'
# payload = "{\"lang\":\"en_ui\",\"deviceType\":\"desktop\",\"country\":\"ui\",\"pageName\":\"Experienced-all-jobs\",\"ddoKey\":\"eagerLoadRefineSearch\",\"sortBy\":\"\",\"subsearch\":\"\",\"from\":0,\"jobs\":true,\"counts\":true,\"all_fields\":[\"city\",\"state\",\"category\",\"type\",\"organizationFunction\",\"country\"],\"pageType\":\"landingPage\",\"size\":\"50\",\"rk\":\"l-experiencedalljobs\",\"clearAll\":false,\"jdsource\":\"facets\",\"isSliderEnable\":false,\"keywords\":\"\",\"global\":true,\"selected_fields\":{\"type\":[\"Experienced\"]},\"rkstatus\":true,\"s\":\"1\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "d7752ba1-5d71-c493-69ca-a6af7bcb9b88"
    }

response = requests.request("POST", url, data=payload, headers=headers)
data = response.json()["eagerLoadRefineSearch"]["data"]['jobs']
finalData = {}
for job in data:
    href = "https://jobs2.deloitte.com/ui/en/job/"
    href = href + job['jobSeqNo'] + "/"
    title = ""
    title = job["title"].replace(".", "")
    title = title.replace("- ", "")
    title = title.replace(" ", "-")
    href = href + title
    # link.append(href)
    job.update({'urlLink': href})
    response = requests.request(url=href, method='GET')
    soup = BeautifulSoup(response.text, 'html.parser')
    # parsedData = json.loads(soup.find_all('script')[1].contents[0])
    t = soup.find_all('script')[4].contents[0].split(' phApp.')[1]
    t = json.loads(t[6:len(t)-1])
    actualDescription = BeautifulSoup(t['jobDetail']['data']['job']['actualDescription'], 'html.parser')
    for a in actualDescription.select('a'):
        a.extract()

    job.update({'description1':str(actualDescription)})
    job.update({'qualifications':t['jobDetail']['data']['job']['qualifications']})
    job.update({'actualDescription': t['jobDetail']['data']['job']['structureData']['description']})
    print(href)
    # t = json.loads(soup.find_all('script')[1].contents[0])

    finalData.update({'deloitte-' + job['jobSeqNo']: job})


with open('../Json_data/Deloitte/job_data.json', 'w') as outfile:
    # json.dumps(response.json(),outfile)
    outfile.write(json.dumps(finalData))
# print(response.text)