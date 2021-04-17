import json
import html
import requests
from bs4 import BeautifulSoup

url = "https://careers.cognizant.com/professionals/widgets"
link = []

category = ["Technology & Engineering"]#,"Digital","Business Processes","IT Infrastructure","Delivery Management","Consulting","Corporate"]

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    
    }
for categorys in category:
    payload = '{"lang":"en_in","deviceType":"desktop","country":"in","pageName":"' + categorys.replace('&','&amp;') +'","ddoKey":"refineSearch","sortBy":"Most recent",' \
              '"subsearch":"","from":0,"jobs":true,"counts":true,' \
              '"all_fields":["category","location","empStatus","industryName","minExp"],' \
              '"pageType":"category","size":50,"clearAll":false,"jdsource":"facets","isSliderEnable":false,"keywords":"","global":true,' \
              '"selected_fields":{"category":["' +categorys + '"]},"sort":{"order":"desc","field":"postedDate"}}'
    response = requests.request("POST", url, data=payload, headers=headers)
    data = response.json()["refineSearch"]["data"]
    # location = data["refineSearch"]["data"]["aggregations"][2]["value"].keys()
    location =[]
    for i in data["aggregations"][2]["value"].keys():
        location.append(i)
    setLocation = []
    for i in location:
        tmp = i.split(', ')
        if i.split(', ')[len(tmp)-1] == "India":
            setLocation.append(i)

    payload = '{"lang":"en_in","deviceType":"desktop","country":"in","pageName":"' + categorys.replace('&','&amp;') +'","ddoKey":"refineSearch","sortBy":"Most recent","subsearch":"","from":0,"jobs":true,"counts":true,"all_fields":["category","location","empStatus","industryName","minExp"],"pageType":"category","size":10,"clearAll":false,"jdsource":"facets","isSliderEnable":false,"keywords":"","global":true,"selected_fields":{"category":["' +categorys + '"],"location":'+str(setLocation)+'},"sort":{"order":"desc","field":"postedDate"}}'
    payload = payload.replace('\'','"')
    response = requests.request("POST", url, data=payload, headers=headers)
    categoryData =response.json()["refineSearch"]["data"]

    for job in categoryData['jobs']:
        href = "https://careers.cognizant.com/professionals/in/en/job/"
        href = href+job["jobId"]+"/"
        title=""
        title = job["title"].replace(".", "")
        title = title.replace("- ", "")
        title = title.replace(" ", "-")
        href = href+title
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
    with open('../Json_data/cognizent/' + categorys +'.json', 'w') as outfile:
        outfile.write(json.dumps(finalData))
    print(categorys)

# baseUrl = "https://careers.cognizant.com/professionals/in/en/"
# href="https://careers.cognizant.com/professionals/in/en/job/00040152242/Sr-Associate-Projects"