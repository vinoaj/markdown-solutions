import config
import os
from markdown2 import Markdown

md = Markdown(extras=["target-blank-links"])


def traverse_dirs():
    input_dir = config.INPUT_DIR
    for root, dirs, files in os.walk(input_dir):
        # print(root)
        # print(root, dirs, files)

        for f in files:
            md_path = os.path.join(root, f)
            #print(md_path)

            with open(md_path, 'r') as md_file:
                html_output = convert_to_html(md_file.read())

                fn_root, fn_ext = os.path.splitext(f)
                fn_new = fn_root + '.html'

                out_subdir = root.replace(input_dir, '')
                out_path = os.path.join(config.OUTPUT_DIR, out_subdir,
                                        fn_new)
                # print(root, '---->', out_subdir, '---->', out_path)

                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, 'w') as out_file:
                    out_file.write(html_output)


def convert_to_html(content_md):
    out = md.convert(content_md)
    return out


if __name__ == '__main__':
    traverse_dirs()

    """
    f = '/Users/vinoaj/projects/markdown-solutions/inputs/test.md'
    with open(f, "r") as md_file:
        md_file_str = md_file.read()
        o = convert_to_html(md_file_str)
        print(o)
    """
