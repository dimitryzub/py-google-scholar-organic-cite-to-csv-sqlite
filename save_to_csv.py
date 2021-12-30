import pandas as pd
from google_scholar_organic_results import organic_results
from google_scholar_cite_results import cite_results

print("waiting for organic results to save..")
pd.DataFrame(data=organic_results()) \
    .to_csv("google_scholar_organic_results.csv", encoding="utf-8", index=False)

print("waiting for cite results to save..")
pd.DataFrame(data=cite_results()) \
    .to_csv("google_scholar_citation_results.csv", encoding="utf-8", index=False)
