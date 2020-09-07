import re
import markdown2

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def get_html(title):
    entry=get_entry(title)
    if entry is not None:
        html_entry=markdown2.markdown(entry)
        return html_entry
    else:
        return None

def exists_entry(title):
    
    flag=False
    listentries=list_entries()
    for entry in listentries:
        if title.lower() == entry:
            flag=True
            break
        elif title.upper() == entry:
            flag=True
            break
        elif title.capitalize() == entry:
            flag=True
            break
    return flag


def contains_str(text):
    listentries=list_entries()
    new_list_entries=list()
    for entry in listentries:
        
        if entry in text.lower() or text.lower() in entry:
            new_list_entries.append(entry)
        elif entry in text.upper() or text.upper() in entry:
            new_list_entries.append(entry)
        elif entry in text.capitalize() or text.capitalize() in entry:
            new_list_entries.append(entry)

    return new_list_entries if len(new_list_entries)>0 else  None  