import json

import requests

url = "https://www.amazon.jobs/en/search.json"

querystring = {"schedule_type_id[]":"Full-Time","normalized_location[]":"Bengaluru, Karnataka, IND","radius":"24km","facets[]":["location","business_category","category","schedule_type_id","employee_class","normalized_location","job_function_id"],"offset":"0","result_limit":"100","sort":"recent","latitude":"","longitude":"","loc_group_id":"","loc_query":"","base_query":"india","city":"","country":"","region":"","county":"","query_options":""}

payload = "{\"lang\":\"en_ui\",\"deviceType\":\"desktop\",\"country\":\"ui\",\"pageName\":\"Experienced-all-jobs\",\"ddoKey\":\"eagerLoadRefineSearch\",\"sortBy\":\"Most recent\",\"subsearch\":\"\",\"from\":0,\"jobs\":true,\"counts\":true,\"all_fields\":[\"city\",\"state\",\"category\",\"type\",\"organizationFunction\",\"country\"],\"pageType\":\"landingPage\",\"size\":\"50\",\"rk\":\"l-experiencedalljobs\",\"clearAll\":false,\"jdsource\":\"facets\",\"isSliderEnable\":false,\"keywords\":\"\",\"global\":true,\"selected_fields\":{\"type\":[\"Experienced\"]},\"sort\":{\"order\":\"desc\",\"field\":\"postedDate\"},\"rkstatus\":true,\"s\":\"1\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "463d85b2-f47d-8687-01c7-8bab7f3198f4"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
data = response.json()['jobs']
finalData = {}
for job in data:
    finalData.update({"amazon-"+job['id_icims']:job})
with open('../Json_data/amazon/job_data.json', 'w') as outfile:
    # json.dumps(response.json(),outfile)
    outfile.write(json.dumps(finalData))

# print(response.text)