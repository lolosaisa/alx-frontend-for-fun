#/usr/bin/env python3

import markdown
import os
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md", file=sys.stderr)
        sys.exit(1)
        
input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)
    
try:
    with open(input_file, 'r') as md_file:
        md_content = md_file.read()
        
        html_content = markdown.markdown(md_content)
        
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)
        
except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
    sys.exit(1)
    
if __name__ == "__main__":
    main()
    