
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

# 指定輸入和輸出 PDF 檔案路徑
# input_pdf_path = r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (2).pdf"
# output_pdf_path = os.path.splitext(input_pdf_path)[0] + "_compressed.pdf"

# # 執行壓縮
# compress_pdf(input_pdf_path, output_pdf_path)

import fitz  # PyMuPDF
import pikepdf
from PIL import Image
import io
import os

def compress_pdf(input_pdf_path, output_pdf_path, image_quality=50):
    # 打開輸入的 PDF 文件
    pdf_document = fitz.open(input_pdf_path)
    
    # 遍歷每一頁
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        
        # 遍歷頁面的每個圖像
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # 獲取原始圖像格式
            
            if image_ext.lower() != "png":
                # 如果圖像不是 JPEG 格式，則進行轉換和壓縮
                image = Image.open(io.BytesIO(image_bytes))
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='png', quality=image_quality)
                compressed_image = img_byte_arr.getvalue()
            else:
                # 如果圖像已經是 JPEG 格式，只進行壓縮
                image = Image.open(io.BytesIO(image_bytes))
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='png', quality=image_quality)
                compressed_image = img_byte_arr.getvalue()
            
            # 替換圖像
            img_rect = page.get_image_rects(xref)
            for rect in img_rect:
                page.insert_image(rect, stream=compressed_image)
    
    # 保存壓縮後的 PDF 文件
    temp_output_pdf_path = os.path.splitext(output_pdf_path)[0] + "_temp.pdf"
    pdf_document.save(temp_output_pdf_path)
    pdf_document.close()

    # 使用 pikepdf 進一步優化 PDF 結構
    with pikepdf.open(temp_output_pdf_path, allow_overwriting_input=True) as pdf:
        pdf.save(output_pdf_path, compress_streams=True)
    
    # 刪除臨時文件
    os.remove(temp_output_pdf_path)
    
    print(f"PDF 文件已成功壓縮並保存到：{output_pdf_path}")

# 指定輸入和輸出 PDF 檔案路徑
input_pdf_path = r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (2).pdf"
output_pdf_path = os.path.splitext(input_pdf_path)[0] + "_compressed.pdf"

# 執行壓縮
compress_pdf(input_pdf_path, output_pdf_path)

# import aspose.pdf as ap
# import os

# # 加載PDF文件
# compressPdfDocument = ap.Document(r"D:\Dataset\CPR\胸痛文件\掃描檔\人體同意書簽名檔 (2).pdf")

# # 創建 OptimizationOptions 類的對象
# pdfoptimizeOptions = ap.optimization.OptimizationOptions()

# # 啟用圖像壓縮
# pdfoptimizeOptions.image_compression_options.compress_images = True

# # 設置圖像質量
# pdfoptimizeOptions.image_compression_options.image_quality = 50

# # 壓縮PDF
# compressPdfDocument.optimize_resources(pdfoptimizeOptions)

# # output_pdf_path = os.path.splitext(compressPdfDocument)[0] + "_compressed.pdf"

# # 保存壓縮的 PDF
# compressPdfDocument.save("output_pdf_path.pdf")

