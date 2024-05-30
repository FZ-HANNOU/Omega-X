import os
import subprocess
import markdown
import fnmatch
from bs4 import BeautifulSoup

def find_directories_starting_with_bracket():
    current_directory = os.getcwd()
    matching_dirs = []
    
    for root, dirs, files in os.walk(current_directory):
        for dir_name in dirs:
            if dir_name.startswith('['):
                matching_dirs.append(os.path.join(root, dir_name))
    
    return matching_dirs

def add_left_margin_to_html(content):
    # Define your function to add left margin to HTML content
    return content  # Placeholder, modify as per your requirement

def remove_toc_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    toc_div = soup.find('div', id='toc')
    if toc_div:
        toc_div.extract()
    pylode = soup.find('div', id='pylode')
    if pylode:
        pylode.extract()
    cleaned_content = str(soup)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def process_html_file(file_path):
    # Define your function to process HTML file
    pass

def append_html_to_file(src_file, dest_file):
    if not os.path.exists(src_file):
        print(f"Source file does not exist: {src_file}")
        return

    with open(src_file, 'r', encoding='utf-8', errors='ignore') as sf:
        src_content = sf.read()
    with open(dest_file, 'a', encoding='utf-8', errors='ignore') as df:
        df.write(src_content)

# Determine the paths
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
docs_directory = os.path.join(parent_directory, 'docs')

# Ensure the docs directory exists
os.makedirs(docs_directory, exist_ok=True)

# Process the main README.md file
readme_path = os.path.join(parent_directory, 'README.md')
with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
    tempMd = f.read()
tempHtml = markdown.markdown(tempMd, extensions=['tables'])
index_html_path = os.path.join(docs_directory, 'index.html')
with open(index_html_path, 'w', encoding='utf-8', errors='ignore') as f:
    f.write(tempHtml)

# Process ontology files
for root, dirs, files in os.walk(parent_directory):
    for file_name in files:
        if fnmatch.fnmatch(file_name, '*Ontology*.ttl'):
            print(file_name)
            ttl_file = os.path.join(root, file_name)
            html_file = os.path.join(docs_directory, os.path.splitext(file_name)[0] + ".html")
            subprocess.run(['pylode', ttl_file, '-o', html_file])
            process_html_file(html_file)
            append_html_to_file(html_file, index_html_path)
remove_toc_from_html(index_html_path)

# Process directories starting with brackets
try:
    directories = find_directories_starting_with_bracket()
    for directory in directories:
        try:
            print(directory)
            print('--------------------------------------------------------------------------------------------------------------------------')
            readme_path = os.path.join(directory, 'README.md')
            with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
                tempMd = f.read()
            tempHtml = markdown.markdown(tempMd, extensions=['tables'])
            dir_index_html_path = os.path.join(docs_directory, f"{os.path.basename(directory)}_index.html")
            with open(dir_index_html_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(tempHtml)

            for root, dirs, files in os.walk(directory):
                for file in files:
                    if fnmatch.fnmatch(file, '*Ontology*.ttl'):
                        print(file)
                        ttl_file = os.path.join(root, file)
                        html_file = os.path.join(docs_directory, os.path.splitext(file)[0] + ".html")
                        subprocess.run(['pylode', ttl_file, '-o', html_file])
                        process_html_file(html_file)
                        append_html_to_file(html_file, dir_index_html_path)
            remove_toc_from_html(dir_index_html_path)

        except Exception as e:
            print(f"An error occurred while processing directory {directory}: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
