import os
import re
import subprocess
import markdown
import fnmatch
import shutil
from bs4 import BeautifulSoup

# Identify the directories hosting ontology modules: they are starting in this repo with a the keyword ontology
def find_directories_with_ontology():
    current_directory = os.getcwd()
    matching_dirs = []
    
    for root, dirs, files in os.walk(current_directory):
        for dir_name in dirs:
            if 'Ontology' in dir_name:  # updated pattern to match directories containing 'Ontology'
                matching_dirs.append(os.path.join(root, dir_name))
    
    return matching_dirs

def remove_toc_and_pylode_from_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    pylode_div = soup.find('div', id='pylode')
    if pylode_div:
        pylode_div.extract()
    
    cleaned_content = str(soup)
    return cleaned_content

def process_html_file(content):
    return remove_toc_and_pylode_from_html(content)

# Enables to add the diagram to a specific section given a title
def insert_image_in_section(content, image_path, section_title):
    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find('h2', string=section_title)
    if section:
        img_tag = soup.new_tag('img', src=image_path, alt=section_title)
        section.insert_after(img_tag)
    return str(soup)

def style_markdown_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.find_all(['h1', 'h2', 'h3']):
        tag['style'] = "color: #21618C; text-decoration: underline;"
    return str(soup)

def extract_module_name(directory):
    match = re.search(r'^(.*)Ontology', os.path.basename(directory))
    if match:
        return match.group(1)
    return None

# Paths to navigate or where to produce files
script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(script_directory)
docs_directory = os.path.join(parent_directory, 'docs')

os.makedirs(docs_directory, exist_ok=True)

# Process directories containing 'Ontology'
try:
    directories = find_directories_with_ontology()
    for directory in directories:
        try:
            print(f"Processing directory: {directory}")
            module_name = extract_module_name(directory)
            if not module_name:
                print(f"Could not extract module name from directory {directory}")
                continue

            readme_path = os.path.join(directory, 'README.md')
            if os.path.exists(readme_path):
                with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
                    tempMd = f.read()
                tempHtml = markdown.markdown(tempMd, extensions=['extra', 'tables'])
                tempHtml = style_markdown_html(tempHtml)

                # Copy PNG image to docs directory
                image_path = None
                for file in os.listdir(directory):
                    if file.endswith('.png'):
                        src_image_path = os.path.join(directory, file)
                        image_path = os.path.join(docs_directory, file)
                        if not os.path.exists(image_path):
                            shutil.copy(src_image_path, image_path)
                        break
                if image_path:
                    tempHtml = insert_image_in_section(tempHtml, os.path.basename(image_path), 'OWL Description')
            else:
                tempHtml = "<p>No README.md found</p>"

            readme_html_path = os.path.join(docs_directory, f"{module_name}.html")
            ontology_html_path = os.path.join(docs_directory, f"{module_name}Ontology.html")
            
            with open(readme_html_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.write('<html><head></head><body>')
                f.write(tempHtml)
                f.write('</body></html>')

            with open(ontology_html_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.write('<html><head></head><body>')

            for root, dirs, files in os.walk(directory):
                for file in files:
                    if fnmatch.fnmatch(file, '*Ontology*.ttl'):
                        print(f"Processing file: {file}")
                        ttl_file = os.path.join(root, file)
                        result = subprocess.run(['pylode', ttl_file], capture_output=True, text=True)
                        cleaned_html_content = process_html_file(result.stdout)
                        with open(ontology_html_path, 'a', encoding='utf-8', errors='ignore') as f:
                            f.write(cleaned_html_content)
                
                with open(ontology_html_path, 'a', encoding='utf-8', errors='ignore') as f:
                    f.write('</body></html>')

        except Exception as e:
            print(f"An error occurred while processing directory {directory}: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
