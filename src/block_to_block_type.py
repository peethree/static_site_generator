# headings: 1-6 #
# code: ``` at start and end
# quote: start with >
# unordered list: start with * + space
# ordered list: starts with number + dot, 1. 2. 3. etc (must incr by 1)

# if none of above: normal paragraph

def block_to_block_type(markdown_block):
    if markdown_block.startswith("# ") or markdown_block.startswith("## ") or markdown_block.startswith("### ") or markdown_block.startswith("#### ") or markdown_block.startswith("##### ") or markdown_block.startswith("###### "):
        return "heading"
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        return "code"
    if markdown_block.startswith(">"):
        return "quote"
    
    block_lines = markdown_block.split("\n")

    # check to see if every line starts with * + space character
    count = 0

    for line in block_lines:
        if line.startswith("* "):
            count += 1 

    if len(block_lines) == count:
        return "unordered list"

    order_count = 0
    # check to see if every line starts with incrementing number + dot
    for index, line in enumerate(block_lines, 1):
        if line.startswith(f"{index}. "):
            order_count += 1

    if len(block_lines) == order_count:
        return "ordered list"
    
    return "paragraph"


