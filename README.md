#=========================================

Hey! I made this because finding a job is not easy these days.
Before use, this puppy needs google custom search API and a custom search engine id to work.

#=========================================

- Import the requests and csv modules.
- (API key) Google cloud console search engine api: https://console.cloud.google.com/apis/library
- (CSEID) Programmable custom search engine id: https://programmablesearchengine.google.com/controlpanel

- Replace "REPLACE ME WITH API" with your generated Google Custom Search API key.
- Replace "REPLACE ME WITH CSEID" with your generated Custom Search Engine ID.
- Replace query with desired search results/job listings
- Replace location with desired location
- (optional) Replace output file name
- Hit run and watch 50 job results pour into a newly made csv file, which can be used in a sheets or something. 

#=========================================

If the API request is successful, the script processes the search results.
It opens a CSV file for writing (creates a new file and will overwrites if it already exists) and writes the results to the CSV file.

The script sets the search query, location, API key, CSE ID, and output file name.
It calls the google_job_search function to perform the search and save the results to the specified CSV file.


