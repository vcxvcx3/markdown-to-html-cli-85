import argparse
import sys
import os

try:
    import markdown
except ImportError:
    print("Error: The 'markdown' library is required. Install it using 'pip install markdown'.")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to HTML.')
    parser.add_argument('input', help='Input markdown file path')
    parser.add_argument('-o', '--output', help='Output HTML file path (default: input with .html extension)')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File '{args.input}' not found.")
        sys.exit(1)

    output_file = args.output if args.output else os.path.splitext(args.input)[0] + '.html'

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_output = markdown.markdown(md_content)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n</head>\n<body>\n')
            f.write(html_output)
            f.write('\n</body>\n</html>')

        print(f"Successfully converted '{args.input}' to '{output_file}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()