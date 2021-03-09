
def read_input():
    result = []
    while True:
        comment = input()
        if comment == "end of comments":
            break
        result.append(comment)
    return result

def print_html(title, content, comments):
    result = f"<h1>\n    {title}\n</h1>\n" + f"<article>\n    {content}\n</article>\n" +\
            "\n".join(f'<div>\n    {comment}\n</div>' for comment in comments)
    print(result)


title = input()
content = input()
comments = read_input()
print_html(title, content, comments)