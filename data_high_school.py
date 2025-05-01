import requests
import json
import re
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

def extract_safe(record, key_chain):
    try:
        for key in key_chain:
            if isinstance(record, dict):
                record = record.get(key, "")
            else:
                return ""
        return record if isinstance(record, str) else ""
    except:
        return ""

def fetch_contacts(school_id, school_name):
    url = f"https://us-east-1-renderer-read.knack.com/v1/scenes/scene_59/views/view_106/records"
    params = {
        "callback": "jQueryCallback",
        "format": "both",
        "page": 1,
        "rows_per_page": 100,
        "school-details5_id": school_id,
        "sort_field": "field_55",
        "sort_order": "asc"
    }

    headers = {
        "x-knack-application-id": "60991a70e3ac80001ca1ff5e",
        "x-knack-rest-api-key": "renderer",
        "x-kl-saas-ajax-request": "Ajax_Request",
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Referer": "https://schsl.org"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        match = re.search(r"\(\s*({.*})\s*\);?$", response.text, re.DOTALL)
        if not match:
            print(f"JSON extract failed: {school_name}")
            return []

        data = json.loads(match.group(1))
        records = data.get("records", [])

        contacts = []
        for rec in records:
            if not isinstance(rec, dict):
                continue

            first = extract_safe(rec, ["field_4_raw", "first"])
            last = extract_safe(rec, ["field_4_raw", "last"])
            email = extract_safe(rec, ["field_5_raw", "email"])
            position = rec.get("field_7", "")
            if isinstance(position, list):
                position = ", ".join([str(p) for p in position])
            elif not isinstance(position, str):
                position = ""

            if any([first, last, email]):
                contacts.append({
                    "First Name": first,
                    "Last Name": last,
                    "Email": email,
                    "School": school_name,
                    "Position": position
                })

        print(f"{school_name}: {len(contacts)} contacts")
        return contacts
    except Exception as e:
        print(f"Error for {school_name}: {e}")
        return []

school_list = []
with open("schools_with_names.txt", "r", encoding="utf-8") as f:
    for line in f:
        if ":" in line:
            parts = line.strip().split(":", 1)
            school_list.append({"id": parts[0].strip(), "name": parts[1].strip()})

all_contacts = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_contacts, s["id"], s["name"]) for s in school_list]
    for future in as_completed(futures):
        all_contacts.extend(future.result())

if all_contacts:
    with open("all_schools_contacts2.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["First Name", "Last Name", "Email", "School", "Position"])
        writer.writeheader()
        writer.writerows(all_contacts)
    print(f"Done: {len(all_contacts)} total contacts saved to all_schools_contacts.csv")
else:
    print("No contacts found.")
