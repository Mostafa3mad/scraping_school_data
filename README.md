# 🏫 scraping_school_data

A high-performance multithreaded Python scraper that collected over **4,000 verified school contacts** (principals, coaches, athletic directors, etc.) from a dynamic directory website in **under one minute**. The tool handles complex JSONP API responses, ensures data consistency, and outputs a clean CSV for direct use in lead generation, campaign targeting, or enrichment pipelines.

---

## 🚀 Features

- ⚡ **Multithreaded** scraping for fast performance  
- ✅ Handles **JSONP API** and inconsistent fields safely  
- 🧠 Robust parsing for nested keys and optional values  
- 📥 Outputs a **clean, deduplicated CSV file**  
- 📊 Captures: `First Name`, `Last Name`, `Email`, `School`, `Position`  

---

## 🛠️ Tech Stack

- Python 3
- `requests`
- `concurrent.futures.ThreadPoolExecutor`
- `csv`, `json`, `re` modules

---

## 📂 Sample Output

A preview of the CSV output structure:

```csv
First Name,Last Name,Email,School,Position
Jacob,Perlmutter,jacob_perlmutter@charleston.k12.sc.us,Academic Magnet High School,Principal
Raymond,Knauer,raymond_knauer@charleston.k12.sc.us,Academic Magnet High School,Athletic Director
Andrew,Rusciolelli,andrew_rusciolelli@charleston.k12.sc.us,Academic Magnet High School,Baseball
Jeannie,Pressley,jeannie.pressley@sumterschools.net,Alice Drive Middle,Principal
Shane,Fidler,sfidler@lex2.org,Airport High,Football
```

Full dataset: `all_schools_contacts.csv`

---

## 📌 How It Works

1. **Loads school IDs and names** from `schools_with_names.txt`
2. For each school, it sends a request to the JSONP API using custom headers
3. Uses **regular expressions** to clean and extract raw JSON
4. Safely parses fields using a utility function `extract_safe`
5. Exports results to `CSV` using Python’s built-in `csv.DictWriter`
6. Executes the scraping in parallel with `ThreadPoolExecutor`

---

## 💡 Use Cases

- Education CRM data enrichment
- Athletic department outreach
- Principal or coach targeting
- Email marketing segmentation

---

## 🧠 Keywords

`python scraping`, `multithreading`, `json parsing`, `school directory`, `lead generation`, `data extraction`, `csv automation`, `requests`, `python automation`, `email scraping`, `jsonp`

---

## 📸 Output Snapshots

![Preview 1](./Screenshot%202025-05-01%20210957.png)
![Preview 2](./Screenshot%202025-05-01%20211213.png)

---

## 👨‍💻 Author

Built by Mostafa Emad — available for freelance Python scraping & automation projects.

- [LinkedIn](https://www.linkedin.com/in/mostafa--emad?originalSubdomain=eg)
- [GitHub](https://github.com/)
- [X (Twitter)](https://x.com/mostafa___emad)
