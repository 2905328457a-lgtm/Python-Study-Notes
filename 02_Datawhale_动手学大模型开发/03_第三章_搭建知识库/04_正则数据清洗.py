import os
import re
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader

# 1. 读取环境配置
_ = load_dotenv(find_dotenv())

# 2.1 读取 PDF 文件（拿到数据）
loader = PyMuPDFLoader("../../data_base/knowledge_db/pumkin_book/pumpkin_book.pdf")
pdf_pages = loader.load()
pdf_page = pdf_pages[1]
# 2.2 读取 md 文件（拿到数据）
loader = UnstructuredMarkdownLoader("../../data_base/knowledge_db/prompt_engineering/1. 简介 Introduction.md")
md_pages = loader.load()
md_page = md_pages[0]

print("=== 1. 清洗前的内容（注意看中间会有异常的换行符 \\n） ===")
print(pdf_page.page_content[:300])

# 4. 【数据清洗】：用正则表达式把中文字符之间乱七八糟的 \n 替换掉
pattern = re.compile(r'[^\u4e00-\u9fff](\n)[^\u4e00-\u9fff]', re.DOTALL)
pdf_page.page_content = re.sub(pattern, lambda match: match.group(0).replace('\n', ''), pdf_page.page_content)

print("\n=== 2. 清洗后的内容（断句变通顺、排版变整洁了！） ===")
print(pdf_page.page_content[:300])

# 删除pdf文件中 .和空格
pdf_page.page_content = pdf_page.page_content.replace('•', '')
pdf_page.page_content = pdf_page.page_content.replace(' ', '')
print(pdf_page.page_content)

# 去除md文件每一段中间隔了一个换行符
md_page.page_content = md_page.page_content.replace('\n\n', '\n')
print(md_page.page_content)
