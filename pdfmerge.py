import PyPDF2
import os

def merge_pdfs(input_pdf_paths):
    """
    將多個 PDF 檔案合併為一個 PDF 檔案，並使用第一個輸入檔案的名稱加上 _merged_out 作為輸出檔案名稱。

    :param input_pdf_paths: 要合併的輸入 PDF 檔案路徑列表。
    """
    if not input_pdf_paths:
        print("未指定要合併的 PDF 檔案。")
        return
    
    # 使用第一個輸入檔案名稱加上 _merged_out 作為輸出檔案名稱
    base_name = os.path.splitext(os.path.basename(input_pdf_paths[0]))[0]
    output_pdf_path = os.path.join(os.path.dirname(input_pdf_paths[0]), base_name + "_merged_out.pdf")
    
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path in input_pdf_paths:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"已成功合併 {len(input_pdf_paths)} 個 PDF 檔案到：{output_pdf_path}")

# 指定要合併的輸入 PDF 檔案路徑列表
# input_pdf_paths = [
#     r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (1).pdf",
#     r"D:\Dataset\CPR\胸痛文件\掃描檔\同意書中間內容.pdf",
#     r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (1).pdf",
    

# ]
# 自動生成包含 1 到 15 的合併路徑\
input_pdf_paths = [f"D:\Dataset\CPR\胸痛文件\掃描檔\\final\\人體同意書簽名檔_part ({i}).pdf" for i in range(1, 16)]

# 執行函式以合併指定的 PDF 檔案
merge_pdfs(input_pdf_paths)




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
