import requests
import csv ## import needed libaries for search and csv
#----------------------------------------------------------------------------------------
# READ ME before use, this puppy needs google custom search API and a custom search engine id to work
#----------------------------------------------------------------------------------------

def google_job_search(query, location, api_key, cse_id, output_file, num_results): ## define variables
    url = "https://www.googleapis.com/customsearch/v1"
    results_per_page = 10
    all_results = []
    total_pages = (num_results // results_per_page) + 1
    for page in range(total_pages):
        start_index = page * results_per_page + 1 ## loop results to get desired amount of searches
        params = {
            'q': f"{query} jobs in {location}",
            'cx': cse_id,
            'key': api_key,
            'start': start_index,
        }
    
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            results = response.json().get('items', [])
            all_results.extend(results)
        else:
            print(f"Failed to retrieve data for page {page + 1}: {response.status_code}") ## error code response
            break
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Snippet', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in all_results:
            title = result.get('title')
            snippet = result.get('snippet')
            link = result.get('link')

            writer.writerow({'Title': title, 'Snippet': snippet, 'Link': link})
            
    print(f"Results have been saved to {output_file}") ## success print response

#----------------------------------------------------------------------------------------

if __name__ == "__main__": ## set name, query, and location
    query = "mechanical engineering coop fall 2024 application startups" ## <---- type in here what you want to search for jobs
    location = "Massachusetts" ## <---------------------------------- type in here the location where you want to search for jobs
    api_key = "AIzaSyCGBJC9CoTMiLgUJczwFfp5FG1oymuzJ1s"  ##  <------- API key goes here
    cse_id = "2313403da5d7a49aa"       ##  <------------------------- custom search engine id goes here (CSEID)
    output_file = "job_search_results.csv" ## <---------------------- output file name (CSV)
    num_results = 50  ## <--------------------------------------------number of results desired
    google_job_search(query, location, api_key, cse_id, output_file, num_results)
