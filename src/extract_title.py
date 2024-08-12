from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):    
    blocks = markdown_to_blocks(markdown)

    # title = heading 1
    for block in blocks:
        if block.startswith("# "):
            title = block.strip("# ")  
            return title.strip("")                            
    raise Exception("no title found")


