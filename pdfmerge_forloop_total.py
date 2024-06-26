

import PyPDF2
import os

def merge_pdfs(input_pdf_paths, page_ranges, num_name):
    """
    將多個 PDF 檔案合併為一個 PDF 檔案，並使用第一個輸入檔案的名稱加上 num_name 和 _merged_out 作為輸出檔案名稱。

    :param input_pdf_paths: 要合併的輸入 PDF 檔案路徑列表。
    :param page_ranges: 對應於每個 PDF 檔案的頁面範圍列表，範圍為 (start_page, end_page)。
    :param num_name: 用於生成輸出檔案名稱的數字。
    :return: 輸出 PDF 檔案的路徑。
    """
    if not input_pdf_paths:
        print("未指定要合併的 PDF 檔案。")
        return
    
    if len(input_pdf_paths) != len(page_ranges):
        print("每個 PDF 檔案必須指定對應的頁面範圍。")
        return
    
    base_name = os.path.splitext(os.path.basename(input_pdf_paths[0]))[0]
    output_pdf_path = os.path.join(os.path.dirname(input_pdf_paths[0]), f"{base_name}_{num_name}_merged_out.pdf")
    
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
    return output_pdf_path

def merge_multiple_pdfs(input_pdf_paths, final_output_path):
    """
    將多個 PDF 檔案合併為一個最終的 PDF 檔案。

    :param input_pdf_paths: 要合併的輸入 PDF 檔案路徑列表。
    :param final_output_path: 最終合併的 PDF 檔案路徑。
    """
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path in input_pdf_paths:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(final_output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"已成功合併所有 PDF 檔案到：{final_output_path}")

# 指定要合併的輸入 PDF 檔案路徑列表
input_pdf_paths = [
    r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (7).pdf",
    r"D:\Dataset\CPR\胸痛文件\掃描檔\同意書中間內容.pdf",
    r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (7).pdf",
]

# 儲存每個合併結果的檔案路徑
merged_files = []

# 第一個 PDF 檔案，頁面範圍動態生成
pdf_path = input_pdf_paths[0]
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page_count = len(pdf_reader.pages)
    for i in range(0, page_count, 2):
        page_ranges = [
            (i, i+1),  # 只添加第一個 PDF 的第一頁
            (0, 4),  # 添加第二個 PDF 的第 1 到第 2 頁
            (i+1, i+2),  # 添加第三個 PDF 的第二頁
        ]

        # 執行函式以合併指定的 PDF 檔案
        merged_file = merge_pdfs(input_pdf_paths, page_ranges, i//2 + 1)
        merged_files.append(merged_file)

# 最終合併所有生成的 PDF 檔案
base_name = os.path.splitext(os.path.basename(input_pdf_paths[0]))[0]
final_output_path = os.path.join(os.path.dirname(input_pdf_paths[0]), f"{base_name}_final.pdf")
# final_output_path = r"D:\Dataset\CPR\胸痛文件\掃描檔\最終合併檔案.pdf"
merge_multiple_pdfs(merged_files, final_output_path)


# 刪除包含 num_name 的暫存檔案
for merged_file in merged_files:
    os.remove(merged_file)
    print(f"已刪除暫存檔案：{merged_file}")



# import fitz  # PyMuPDF
# import pikepdf
# from PIL import Image
# import io
# import os

# def compress_pdf(input_pdf_path, output_pdf_path, image_quality=85):
#     # 打開輸入的 PDF 文件
#     pdf_document = fitz.open(input_pdf_path)
    
#     # 遍歷每一頁
#     for page_num in range(len(pdf_document)):
#         page = pdf_document.load_page(page_num)
#         image_list = page.get_images(full=True)
        
#         # 遍歷頁面的每個圖像
#         for image_index, img in enumerate(image_list):
#             xref = img[0]
#             base_image = pdf_document.extract_image(xref)
#             image_bytes = base_image["image"]
            
#             image = Image.open(io.BytesIO(image_bytes))
            
#             # 壓縮圖像
#             img_byte_arr = io.BytesIO()
#             image.save(img_byte_arr, format='JPEG', quality=image_quality)
#             compressed_image = img_byte_arr.getvalue()
            
#             # 替換圖像
#             img_rect = page.get_image_rects(xref)
#             for rect in img_rect:
#                 page.insert_image(rect, stream=compressed_image)
    
#     # 保存壓縮後的 PDF 文件
#     pdf_document.save(output_pdf_path)
#     pdf_document.close()
#     print(f"PDF 文件已成功壓縮並保存到：{output_pdf_path}")

# # 指定輸入和輸出 PDF 檔案路徑
# input_pdf_path = r"D:\Dataset\CPR\榮總人體試驗資料表\掃描檔\人體同意書全_part1_merged_out_merged_out.pdf"
# output_pdf_path = os.path.splitext(input_pdf_path)[0] + "_compressed.pdf"

# # 執行壓縮
# compress_pdf(input_pdf_path, output_pdf_path)
