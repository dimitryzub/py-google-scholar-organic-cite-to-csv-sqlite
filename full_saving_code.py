import pandas as pd
import sqlite3
from google_scholar_organic_results import organic_results
from google_scholar_cite_results import cite_results

# Pandas
print("waiting for organic results to save..")
organic_df = pd.DataFrame(data=organic_results())
organic_df.to_csv("google_scholar_organic_results.csv", encoding="utf-8", index=False)

print("waiting for cite results to save..")
cite_df = pd.DataFrame(data=cite_results())
cite_df.to_csv("google_scholar_citation_results.csv", encoding="utf-8", index=False)

# MySQL
conn = sqlite3.connect("google_scholar_results.db")

conn.execute("""CREATE TABLE google_scholar_organic_results (
                page_number integer,
                position integer,
                result_type text,
                title text,
                link text,
                snippet text,
                result_id text,
                publication_info_summary text,
                cited_by_count integer,
                cited_by_link text,
                cited_by_id text,
                total_versions integer,
                all_versions_link text,
                all_versions_id text,
                file_format text,
                file_title text,
                file_link text)""")
conn.commit()


conn.execute("""CREATE TABLE google_scholar_cite_results (
            organic_results_title text,
            organic_results_link text,
            citation_title text,
            citation_link text)""")
conn.commit()

for item in organic_results():
    conn.execute("""INSERT INTO google_scholar_organic_results
                    VALUES (:page_number,
                            :position,
                            :result_type,
                            :title,
                            :link,
                            :snippet,
                            :result_id,
                            :publication_info_summary,
                            :cited_by_count,
                            :cited_by_link,
                            :cited_by_id,
                            :total_versions,
                            :all_versions_link,
                            :all_versions_id,
                            :file_format,
                            :file_title,
                            :file_link)""",
                 {"page_number": item["page_number"],
                  "position": item["position"],
                  "result_type": item["type"],
                  "title": item["title"],
                  "link": item["link"],
                  "snippet": item["snippet"],
                  "result_id": item["result_id"],
                  "publication_info_summary": item["publication_info_summary"],
                  "cited_by_count": item["cited_by_count"],
                  "cited_by_link": item["cited_by_link"],
                  "cited_by_id": item["cited_by_id"],
                  "total_versions": item["total_versions"],
                  "all_versions_link": item["all_versions_link"],
                  "all_versions_id": item["all_versions_id"],
                  "file_format": item["file_format"],
                  "file_title": item["file_title"],
                  "file_link": item["file_link"]})
conn.commit()


for cite_result in cite_results():
    conn.execute("""INSERT INTO google_scholar_cite_results
                    VALUES (:organic_result_title,
                    :organic_result_link,
                    :citation_title,
                    :citation_snippet)""",
                 {"organic_result_title": cite_result["organic_result_title"],
                  "organic_result_link": cite_result["organic_result_link"],
                  "citation_title": cite_result["citation_title"],
                  "citation_snippet": cite_result["citation_snippet"]})

conn.commit()
conn.close()
print("Saved to SQL Lite database.")
