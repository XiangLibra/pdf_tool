
# import PyPDF2
# import os

# def reduce_pdf_pages(input_pdf_path, start_page, end_page):
#     output_pdf_path = os.path.splitext(input_pdf_path)[0] + "_out.pdf"
    
#     # 打開輸入的 PDF 檔案
#     with open(input_pdf_path, 'rb') as input_file:
#         pdf_reader = PyPDF2.PdfReader(input_file)
#         page_count = len(pdf_reader.pages)

#         # 檢查頁面範圍是否有效
#         if start_page < 0 or start_page >= page_count or end_page <= start_page or end_page > page_count:
#             print("Invalid page range specified.")
#             return

#         # 創建新的 PDF 寫入器
#         pdf_writer = PyPDF2.PdfWriter()

#         # 逐頁將指定範圍內的內容添加到新的 PDF 寫入器
#         for page_num in range(start_page, end_page):
#             pdf_writer.add_page(pdf_reader.pages[page_num])

#         # 寫入新的 PDF 檔案
#         with open(output_pdf_path, 'wb') as output_file:
#             pdf_writer.write(output_file)

#     print(f"PDF 頁面範圍 {start_page} 到 {end_page} 已成功提取，請查看輸出檔案：{output_pdf_path}")

# # 指定輸入 PDF 檔案路徑以及要提取的頁面範圍
# input_pdf_path = r"D:\Dataset\2205.13281v2.pdf"
# start_page = 1  # 起始頁面（從0開始計算）
# end_page = 10   # 結束頁面（包含）

# # 執行函式以提取指定範圍的 PDF 頁面
# reduce_pdf_pages(input_pdf_path, start_page, end_page)

import PyPDF2
import os

def split_pdf(input_pdf_path, page_ranges):
    """
    將指定頁面範圍的內容從輸入 PDF 中提取並保存到獨立的 PDF 文件中。
    
    :param input_pdf_path: 輸入 PDF 檔案的路徑。
    :param page_ranges: 一個包含多個元組的列表，每個元組表示一個頁面範圍（start_page, end_page）或單個頁面（start_page,）。
    """
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        page_count = len(pdf_reader.pages)

        for idx, page_range in enumerate(page_ranges):
            if isinstance(page_range, tuple):
                if len(page_range) == 1:
                    start_page = page_range[0]
                    end_page = start_page
                elif len(page_range) == 2:
                    start_page, end_page = page_range
                else:
                    print(f"Invalid page range specified: {page_range}.")
                    continue
            else:
                print(f"Invalid page range specified: {page_range}.")
                continue

            # 檢查頁面範圍是否有效
            if start_page < 0 or start_page > page_count or end_page < start_page or end_page > page_count:
                print(f"Invalid page range specified: ({start_page}, {end_page}).")
                continue

            output_pdf_path = os.path.splitext(input_pdf_path)[0] + f"_part{idx+1}.pdf"

            # 創建新的 PDF 寫入器
            pdf_writer = PyPDF2.PdfWriter()

            # 逐頁將指定範圍內的內容添加到新的 PDF 寫入器
            
            for page_num in range(start_page-1, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])


            # 寫入新的 PDF 檔案
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"PDF 頁面範圍 {start_page} 到 {end_page} 已成功提取，請查看輸出檔案：{output_pdf_path}")

# 指定輸入 PDF 檔案路徑以及要提取的頁面範圍
input_pdf_path = r"D:\Dataset\CPR\胸痛文件\掃描檔\doc01384420240625084523.pdf"
# page_ranges = [(1,), (10,), (12,),(14,),(16,),(18,),(20,),(22,),(24,),(26,),(28,),(30,),(32,),(34,),(36,),(38,),(40,),(42,),(44,),(46,),]  # 要提取的頁面範圍列表，包含多個 (start_page, end_page) 元組或單個頁面 (start_page,)

page_ranges = [(2,5)]  # 要提取的頁面範圍列表，包含多個 (start_page, end_page) 元組或單個頁面 (start_page,)

# page_ranges = [(1,)]  # 要提取的頁面範圍列表，包含多個 (start_page, end_page) 元組或單個頁面 (start_page,)

# 執行函式以提取指定範圍的 PDF 頁面
split_pdf(input_pdf_path, page_ranges)
