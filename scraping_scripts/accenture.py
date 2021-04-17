import json
import requests

url = "https://www.accenture.com/api/sitecore/JobSearch/FindJobs"

payload = "{\"f\":1,\"s\":100,\"k\":\"Entry-level ANALYST\",\"lang\":\"en\",\"cs\":\"in-en\",\"df\":\"[{\\\"metadatafieldname\\\":\\\"skill\\\",\\\"items\\\":[{\\\"term\\\":\\\"cloud\\\",\\\"selected\\\":true},{\\\"term\\\":\\\"engineering\\\",\\\"selected\\\":true},{\\\"term\\\":\\\"information technology operations\\\",\\\"selected\\\":true},{\\\"term\\\":\\\"software engineering\\\",\\\"selected\\\":true}]},{\\\"metadatafieldname\\\":\\\"location\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"travelPercentage\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"jobTypeDescription\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"businessArea\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"specialization\\\",\\\"items\\\":[]}]\",\"c\":\"India\",\"sf\":1,\"syn\":false,\"isPk\":false,\"wordDistance\":0,\"userId\":\"\"}\n"
headers = {
    'cache-control': "no-cache",
    'postman-token': "3d1783fe-dea1-04de-b4f4-673a04e930da"
    }

response = requests.request("POST", url, data=payload, headers=headers)
data = response.json()['documents']

finalData = {}
for job in data:
    finalData.update({"accenture-"+job['requisitionId']:job})
with open('../Json_data/accenture/job_data.json', 'w') as outfile:
    # json.dumps(response.json(),outfile)
    outfile.write(json.dumps(finalData))


# print(response.text)