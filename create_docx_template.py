"""
Script tạo file DOCX mẫu sử dụng thư viện python-docx.

Tạo một file Word (.docx) với các thành phần phổ biến:
- Tiêu đề, heading
- Đoạn văn bản với định dạng (bold, italic, underline)
- Bảng dữ liệu
- Danh sách có đánh số và bullet
- Header / Footer
- Hình ảnh placeholder
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
import os


def create_docx_template(output_path="template.docx"):
    """Tạo file DOCX mẫu với đầy đủ các thành phần."""
    doc = Document()

    # ── Thiết lập trang ──
    section = doc.sections[0]
    section.page_width = Cm(21)       # A4
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(3.17)
    section.right_margin = Cm(3.17)

    # ── Header & Footer ──
    header = section.header
    header_para = header.paragraphs[0]
    header_para.text = "Công ty TNHH ABC"
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_para.style.font.size = Pt(9)
    header_para.style.font.color.rgb = RGBColor(128, 128, 128)

    footer = section.footer
    footer_para = footer.paragraphs[0]
    footer_para.text = "Trang "
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Tiêu đề chính ──
    title = doc.add_heading("BÁO CÁO MẪU", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Thông tin chung ──
    doc.add_heading("1. Thông tin chung", level=1)

    info_table = doc.add_table(rows=4, cols=2)
    info_table.style = "Light Grid Accent 1"
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    info_data = [
        ("Tên dự án:", "[Nhập tên dự án]"),
        ("Người thực hiện:", "[Nhập họ tên]"),
        ("Ngày lập:", "[DD/MM/YYYY]"),
        ("Phiên bản:", "1.0"),
    ]
    for i, (label, value) in enumerate(info_data):
        row = info_table.rows[i]
        row.cells[0].text = label
        row.cells[1].text = value
        # Bold cho cột nhãn
        for paragraph in row.cells[0].paragraphs:
            for run in paragraph.runs:
                run.bold = True

    doc.add_paragraph()  # Khoảng trắng

    # ── Mục lục ──
    doc.add_heading("Mục lục", level=1)
    toc_items = [
        "1. Thông tin chung",
        "2. Giới thiệu",
        "3. Nội dung chi tiết",
        "4. Bảng dữ liệu",
        "5. Kết luận",
    ]
    for item in toc_items:
        p = doc.add_paragraph(item)
        p.paragraph_format.space_after = Pt(2)

    doc.add_page_break()

    # ── Phần giới thiệu ──
    doc.add_heading("2. Giới thiệu", level=1)

    intro = doc.add_paragraph()
    intro.add_run("Đây là file DOCX mẫu ").bold = False
    intro.add_run("được tạo tự động ").bold = True
    intro.add_run("bằng thư viện ").bold = False
    run_italic = intro.add_run("python-docx")
    run_italic.italic = True
    intro.add_run(". Bạn có thể chỉnh sửa nội dung theo nhu cầu.")

    doc.add_paragraph(
        "File này bao gồm nhiều thành phần thường gặp trong một tài liệu Word: "
        "tiêu đề, bảng, danh sách, định dạng văn bản, header/footer, v.v."
    )

    # ── Nội dung chi tiết ──
    doc.add_heading("3. Nội dung chi tiết", level=1)

    # Danh sách bullet
    doc.add_heading("3.1 Danh sách dạng bullet", level=2)
    bullets = [
        "Mục tiêu số 1: Hoàn thành nghiên cứu",
        "Mục tiêu số 2: Phân tích dữ liệu",
        "Mục tiêu số 3: Viết báo cáo tổng kết",
    ]
    for item in bullets:
        doc.add_paragraph(item, style="List Bullet")

    # Danh sách đánh số
    doc.add_heading("3.2 Danh sách đánh số", level=2)
    numbered = [
        "Bước 1: Thu thập dữ liệu từ các nguồn",
        "Bước 2: Xử lý và làm sạch dữ liệu",
        "Bước 3: Phân tích và trực quan hóa",
        "Bước 4: Đưa ra kết luận",
    ]
    for item in numbered:
        doc.add_paragraph(item, style="List Number")

    # Đoạn văn với định dạng đặc biệt
    doc.add_heading("3.3 Định dạng văn bản", level=2)

    p = doc.add_paragraph()
    p.add_run("Chữ đậm (Bold)").bold = True
    p.add_run(" | ")
    run_i = p.add_run("Chữ nghiêng (Italic)")
    run_i.italic = True
    p.add_run(" | ")
    run_u = p.add_run("Chữ gạch chân (Underline)")
    run_u.underline = True

    p2 = doc.add_paragraph()
    run_color = p2.add_run("Chữ màu đỏ")
    run_color.font.color.rgb = RGBColor(255, 0, 0)
    p2.add_run(" | ")
    run_big = p2.add_run("Chữ cỡ lớn (16pt)")
    run_big.font.size = Pt(16)
    p2.add_run(" | ")
    run_small = p2.add_run("Chữ cỡ nhỏ (8pt)")
    run_small.font.size = Pt(8)

    # ── Bảng dữ liệu ──
    doc.add_heading("4. Bảng dữ liệu", level=1)

    table = doc.add_table(rows=1, cols=4)
    table.style = "Medium Shading 1 Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    headers = ["STT", "Hạng mục", "Số lượng", "Đơn giá (VNĐ)"]
    for i, text in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = text
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.bold = True

    # Data rows
    data = [
        ("1", "Thiết bị A", "10", "1,500,000"),
        ("2", "Thiết bị B", "5", "2,300,000"),
        ("3", "Dịch vụ C", "1", "5,000,000"),
        ("4", "Vật tư D", "100", "50,000"),
    ]
    for stt, item, qty, price in data:
        row = table.add_row()
        row.cells[0].text = stt
        row.cells[1].text = item
        row.cells[2].text = qty
        row.cells[3].text = price
        row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[3].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    doc.add_paragraph()

    # ── Trích dẫn / Quote ──
    doc.add_heading("4.1 Ghi chú", level=2)
    quote = doc.add_paragraph(
        "Lưu ý: Tất cả giá trên chưa bao gồm thuế VAT 10%. "
        "Vui lòng liên hệ để được báo giá chính xác."
    )
    quote.style = "Intense Quote"

    # ── Kết luận ──
    doc.add_page_break()
    doc.add_heading("5. Kết luận", level=1)

    doc.add_paragraph(
        "Đây là phần kết luận của báo cáo. Bạn có thể thay thế nội dung này "
        "bằng kết luận thực tế của dự án."
    )

    # Chữ ký
    doc.add_paragraph()
    doc.add_paragraph()

    sig_table = doc.add_table(rows=4, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    sig_table.rows[0].cells[0].text = "Người lập báo cáo"
    sig_table.rows[0].cells[1].text = "Người phê duyệt"
    sig_table.rows[1].cells[0].text = "(Ký, ghi rõ họ tên)"
    sig_table.rows[1].cells[1].text = "(Ký, ghi rõ họ tên)"
    sig_table.rows[3].cells[0].text = "[Họ và tên]"
    sig_table.rows[3].cells[1].text = "[Họ và tên]"

    for cell in sig_table.rows[0].cells:
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.bold = True
    for row_idx in [1, 3]:
        for cell in sig_table.rows[row_idx].cells:
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ── Lưu file ──
    doc.save(output_path)
    print(f"Đã tạo file DOCX mẫu: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    create_docx_template()
