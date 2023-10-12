import json
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urlparse, urljoin


def crawl(url, ignore_ext):
    try:
        # Get site file response.
        response = requests.get(url)
        # Print any HTTP Error occured
        response.raise_for_status()

        # Get parse tree from html response file
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get all <a> elements from HTML and extract their href attributes
        # links = [link.get('href') for link in soup.find_all('a')]
        
        links = list()
    
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if not parsed_url.netloc:
                    continue
                if not parsed_url.path:
                    absolute_url = absolute_url + '/'  # Εάν δεν υπάρχει διαδρομή, προσθέστε "/"
                if not any(absolute_url.endswith(ext) for ext in ignore_ext):
                    links.append(absolute_url)

        # Return a list with the links found
        return links

    except requests.exceptions.RequestException as e:
        print(f"Request failed with status code {response.status_code}: {e}")
        return []

# Συνάρτηση για ανάκτηση του robots.txt αρχείου ενός ιστότοπου
def get_robots_txt(url):
    robots_url = urljoin(url, "/robots.txt")
    try:
        response = requests.get(robots_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return ""
    return response.text

def main():
    # Manage Arguments
    parser = argparse.ArgumentParser(description="Web Crawler CLI")
    parser.add_argument("url", help="URL to crawl and get its links")
    parser.add_argument("-i", "--ignore_ext", nargs='+', help="Ignore CSS files")

    args = parser.parse_args()
    url = args.url
    ignore_ext = args.ignore_ext
    print(ignore_ext)
    
    # Εκτύπωση του robots.txt αρχείου, αν υπάρχει
    robots_txt = get_robots_txt(url)
    if robots_txt:
        print("robots.txt:\n")
        print(robots_txt)

    # Get Links from URL
    links = crawl(url, ignore_ext)

    print("\nFound URLs:")
    for link in links:
        print(link)
    
    export_file = "./links.json"
    # Extract URLs
    print(f"Links are exported to '{export_file}' ")
    with open(export_file, "w") as json_file:
        json.dump(links, json_file)

if __name__ == "__main__":
    main()