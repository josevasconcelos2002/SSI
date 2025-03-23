import markdown
import pdfkit

with open("./assets/aula2.md", "r", encoding="utf-8") as f:
    md_content = f.read()

html_content = markdown.markdown(md_content)

pdfkit.from_string(html_content, "./assets/aula2.pdf")
