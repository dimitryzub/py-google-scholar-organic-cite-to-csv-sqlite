# https://www.youtube.com/watch?v=pd-0G0MigUA
# https://docs.python.org/3/library/sqlite3.html
# https://stackoverflow.com/questions/8442147/how-to-delete-or-add-column-in-sqlite/66399224#66399224
# https://www.sqlite.org/datatype3.html

# Other useful commands:
# conn.execute("DELETE FROM google_scholar_organic_results")
# conn.execute("DROP TABLE google_scholar_organic_results")
# conn.execute("ALTER TABLE google_scholar_organic_results DROP COLUMN authors")
# conn.execute("ALTER TABLE google_scholar_organic_results ADD COLUMN snippet text")

import sqlite3
import pandas as pd
from google_scholar_organic_results import organic_results
from google_scholar_cite_results import cite_results

conn = sqlite3.connect("google_scholar_results.db")

# Save to SQLite using Pandas
pd.DataFrame(organic_results()).to_sql(name="google_scholar_organic_results",
                                       con=conn,
                                       if_exists="append",
                                       index=False)

pd.DataFrame(cite_results()).to_sql(name="google_scholar_cite_results",
                                    con=conn,
                                    if_exists="append",
                                    index=False)

# Save to database using SQLite
# conn.execute("""CREATE TABLE google_scholar_organic_results (
#                 page_number integer,
#                 position integer,
#                 result_type text,
#                 title text,
#                 link text,
#                 snippet text,
#                 result_id text,
#                 publication_info_summary text,
#                 cited_by_count integer,
#                 cited_by_link text,
#                 cited_by_id text,
#                 total_versions integer,
#                 all_versions_link text,
#                 all_versions_id text,
#                 file_format text,
#                 file_title text,
#                 file_link text)""")

# conn.execute("""CREATE TABLE google_scholar_cite_results (
#             organic_results_title text,
#             organic_results_link text,
#             citation_title text,
#             citation_link text)""")


# for item in organic_results():
#     conn.execute("""INSERT INTO google_scholar_organic_results
#                     VALUES (:page_number,
#                             :position,
#                             :result_type,
#                             :title,
#                             :link,
#                             :snippet,
#                             :result_id,
#                             :publication_info_summary,
#                             :cited_by_count,
#                             :cited_by_link,
#                             :cited_by_id,
#                             :total_versions,
#                             :all_versions_link,
#                             :all_versions_id,
#                             :file_format,
#                             :file_title,
#                             :file_link)""",
#                  {"page_number": item["page_number"],
#                   "position": item["position"],
#                   "result_type": item["type"],
#                   "title": item["title"],
#                   "link": item["link"],
#                   "snippet": item["snippet"],
#                   "result_id": item["result_id"],
#                   "publication_info_summary": item["publication_info_summary"],
#                   "cited_by_count": item["cited_by_count"],
#                   "cited_by_link": item["cited_by_link"],
#                   "cited_by_id": item["cited_by_id"],
#                   "total_versions": item["total_versions"],
#                   "all_versions_link": item["all_versions_link"],
#                   "all_versions_id": item["all_versions_id"],
#                   "file_format": item["file_format"],
#                   "file_title": item["file_title"],
#                   "file_link": item["file_link"]})


# OR YOU CAN DO THE SAME THING LIKE SO:

# for item in organic_results():
#     conn.execute("""INSERT INTO google_scholar_organic_results
#                 (page_number,
#                 position,
#                 result_type,
#                 title,
#                 link,
#                 result_id,
#                 publication_info_summary,
#                 cited_by_count,
#                 cited_by_link,
#                 cited_by_id,
#                 total_versions,
#                 all_versions_link,
#                 all_versions_id,
#                 file_format,
#                 file_title,
#                 file_link)
#                 VALUES (:page_number,
#                         :position,
#                         :result_type,
#                         :title,
#                         :link,
#                         :result_id,
#                         :publication_info_summary,
#                         :cited_by_count,
#                         :cited_by_link,
#                         :cited_by_id,
#                         :total_versions,
#                         :all_versions_link,
#                         :all_versions_id,
#                         :file_format,
#                         :file_title,
#                         :file_link)""",
#                  {"page_number": item["page_number"],
#                   "position": item["position"],
#                   "result_type": item["type"],
#                   "title": item["title"],
#                   "link": item["link"],
#                   "result_id": item["result_id"],
#                   "publication_info_summary": item["publication_info_summary"],
#                   "cited_by_count": item["cited_by_count"],
#                   "cited_by_link": item["cited_by_link"],
#                   "cited_by_id": item["cited_by_id"],
#                   "total_versions": item["total_versions"],
#                   "all_versions_link": item["all_versions_link"],
#                   "file_format": item["file_format"],
#                   "file_title": item["file_title"],
#                   "file_link": item["file_link"]})


# for cite_result in cite_results():
#     conn.execute("""INSERT INTO google_scholar_cite_results
#                     VALUES (:organic_result_title,
#                     :organic_result_link,
#                     :citation_title,
#                     :citation_snippet)""",
#                  {"organic_result_title": cite_result["organic_result_title"],
#                   "organic_result_link": cite_result["organic_result_link"],
#                   "citation_title": cite_result["citation_title"],
#                   "citation_snippet": cite_result["citation_snippet"]})


conn.commit()
conn.close()
print("Saved to SQL Lite database.")
