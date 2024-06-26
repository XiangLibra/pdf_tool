


import PyPDF2
import os

def merge_pdfs(input_pdf_paths, page_ranges):
    """
    將多個 PDF 檔案合併為一個 PDF 檔案，並使用第一個輸入檔案的名稱加上 _merged_out 作為輸出檔案名稱。

    :param input_pdf_paths: 要合併的輸入 PDF 檔案路徑列表。
    :param page_ranges: 對應於每個 PDF 檔案的頁面範圍列表，範圍為 (start_page, end_page)。
    """
    if not input_pdf_paths:
        print("未指定要合併的 PDF 檔案。")
        return
    
    if len(input_pdf_paths) != len(page_ranges):
        print("每個 PDF 檔案必須指定對應的頁面範圍。")
        return
    
    # 使用第一個輸入檔案名稱加上 _merged_out 作為輸出檔案名稱
    base_name = os.path.splitext(os.path.basename(input_pdf_paths[0]))[0]
    output_pdf_path = os.path.join(os.path.dirname(input_pdf_paths[0]), base_name + "_merged_out.pdf")
    
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path, (start_page, end_page) in zip(input_pdf_paths, page_ranges):
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page_count = len(pdf_reader.pages)

            if start_page < 0 or end_page > page_count or start_page >= end_page:
                print(f"無效的頁面範圍: {pdf_path} ({start_page}, {end_page})")
                continue

            for page_num in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"已成功合併 {len(input_pdf_paths)} 個 PDF 檔案到：{output_pdf_path}")

# 指定要合併的輸入 PDF 檔案路徑列表
input_pdf_paths = [
    r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (7).pdf",
    # r"D:\Dataset\CPR\胸痛文件\掃描檔\同意書p136.pdf",
    r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (7).pdf",
]

# 指定對應的頁面範圍 (start_page, end_page)
# 注意：頁面範圍是左閉右開區間，即 [start_page, end_page) 不包含 end_page。
page_ranges = [
    (0, 3),  # 選擇頁面
    # (0, 1),  # 添加第三個 PDF 的第二頁
    (4, 21),  # 添加第三個 PDF 的第二頁
]

# 執行函式以合併指定的 PDF 檔案
merge_pdfs(input_pdf_paths, page_ranges)


