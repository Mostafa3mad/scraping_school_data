import json
import re
import csv
import requests

headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://us-east-1-renderer-read.knack.com/api/xdc.html?xdm_e=https%3A%2F%2Fschsl.org&xdm_c=default8513&xdm_p=1',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-storage-access': 'active',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-kl-saas-ajax-request': 'Ajax_Request',
    'x-knack-application-id': '60991a70e3ac80001ca1ff5e',
    'x-knack-new-builder': 'true',
    'x-knack-rest-api-key': 'renderer',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'callback': 'jQuery17201451492935884271_1746118226685',
    'format': 'both',
    'page': '1',
    'rows_per_page': '1000',
    'sort_field': 'field_1',
    'sort_order': 'asc',
    '_': '1746118279750',
}

response = requests.get(
    'https://us-east-1-renderer-read.knack.com/v1/scenes/scene_20/views/view_104/records',
    params=params,
    headers=headers,
)

match = re.search(r'\(\s*({.*})\s*\);?$', response.text, re.DOTALL)
if not match:
    raise ValueError("error json ")

json_str = match.group(1)
data = json.loads(json_str)

records = data.get("records", [])
school_list = []

for record in records:
    school_id = record.get("id")
    school_name = record.get("field_1", "").strip()
    if school_id and school_name:
        school_list.append((school_id, school_name))

print(f"✅ Found {len(school_list)} schools")
for s in school_list[:10]:
    print(f"{s[0]} - {s[1]}")

with open("schools_with_names.txt", "w", encoding="utf-8") as f:
    for school_id, school_name in school_list:
        f.write(f"{school_id}:{school_name}\n")

print("💾 Saved to schools_with_names.txt")
