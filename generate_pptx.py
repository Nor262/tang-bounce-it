import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette
COLOR_BG_DARK = RGBColor(18, 18, 28)
COLOR_CARD_DARK = RGBColor(28, 28, 44)
COLOR_CARD_BORDER = RGBColor(55, 55, 80)
COLOR_GOLD = RGBColor(255, 209, 102)
COLOR_RED_VN = RGBColor(230, 57, 70)
COLOR_BLUE_KR = RGBColor(0, 119, 182)
COLOR_WHITE = RGBColor(245, 245, 250)
COLOR_MUTED = RGBColor(168, 178, 200)
COLOR_CYAN = RGBColor(6, 214, 160)

blank_layout = prs.slide_layouts[6]

def set_slide_background(slide, color):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = color
    bg.line.fill.background()
    return bg

def add_header(slide, tag_text, title_text):
    # Header tag
    tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = tag_text.upper()
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_GOLD

    # Main slide title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE

def add_card(slide, left, top, width, height, bg_color=COLOR_CARD_DARK, border_color=COLOR_CARD_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
    else:
        card.line.fill.background()
    return card

# ==================== SLIDE 1: TRANG BÌA ====================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1, COLOR_BG_DARK)

# Title & Slogan
tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(3.5))
tf1 = tb1.text_frame
tf1.word_wrap = True

p1_comp = tf1.paragraphs[0]
p1_comp.text = "KOREA GAME WEEK 2026 • HỒ SƠ DỰ THI LẬP TRÌNH GAME"
p1_comp.font.size = Pt(13)
p1_comp.font.bold = True
p1_comp.font.color.rgb = COLOR_GOLD
p1_comp.alignment = PP_ALIGN.CENTER

p1_title = tf1.add_paragraph()
p1_title.text = "TÂNG! (BOUNCE IT!)"
p1_title.font.size = Pt(46)
p1_title.font.bold = True
p1_title.font.color.rgb = COLOR_WHITE
p1_title.alignment = PP_ALIGN.CENTER

p1_sub = tf1.add_paragraph()
p1_sub.text = "JEGI-CẦU ODYSSEY: 5 STEPS TO HERITAGE"
p1_sub.font.size = Pt(20)
p1_sub.font.bold = True
p1_sub.font.color.rgb = COLOR_RED_VN
p1_sub.alignment = PP_ALIGN.CENTER

p1_slogan = tf1.add_paragraph()
p1_slogan.text = "\nSự giao thoa hoàn hảo giữa trò chơi Đá Cầu Việt Nam & Jegichagi Hàn Quốc\nThể loại: Hyper-casual / Precision Physics & One-Tap Rage-bait trên Unity"
p1_slogan.font.size = Pt(15)
p1_slogan.font.color.rgb = COLOR_MUTED
p1_slogan.alignment = PP_ALIGN.CENTER

# Metadata Card at bottom
c1 = add_card(s1, Inches(2.5), Inches(5.5), Inches(8.333), Inches(1.2), COLOR_CARD_DARK)
tb_meta = s1.shapes.add_textbox(Inches(2.7), Inches(5.6), Inches(7.9), Inches(1.0))
tf_meta = tb_meta.text_frame
p_meta = tf_meta.paragraphs[0]
p_meta.text = "Ban Tổ Chức: Trung tâm Văn hóa Hàn Quốc tại Việt Nam (KCC) • KOCCA • Đại sứ quán Hàn Quốc\nTiêu đề thư nộp bài: [Dự thi Lập trình game KGW2026] • Hạn chót: 11/11/2026"
p_meta.font.size = Pt(12)
p_meta.font.color.rgb = COLOR_WHITE
p_meta.alignment = PP_ALIGN.CENTER

# ==================== SLIDE 2: THÔNG TIN ĐỘI NHÓM ====================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2, COLOR_BG_DARK)
add_header(s2, "Hồ sơ dự thi", "Slide 02: Thông Tin Nhóm & Phân Công Vai Trò")

card_t1 = add_card(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
tb_t1 = s2.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
tf_t1 = tb_t1.text_frame
tf_t1.word_wrap = True
p_t1_h = tf_t1.paragraphs[0]
p_t1_h.text = "THÀNH VIÊN 01 (TRƯỞNG NHÓM)"
p_t1_h.font.size = Pt(15)
p_t1_h.font.bold = True
p_t1_h.font.color.rgb = COLOR_GOLD

p_t1_c = tf_t1.add_paragraph()
p_t1_c.text = "\n• Họ và tên: [Điền họ tên Trưởng nhóm]\n• Đơn vị: Học sinh THPT / Sinh viên CNTT - ICT\n• Email liên hệ: [Điền email]\n• Số điện thoại: [Điền SĐT]\n\nVai trò trọng tâm:\n- Unity Game Programmer (Lập trình 2D Physics, Vòng lặp Core Loop, Input Handler)\n- Quản lý tích hợp hệ thống âm thanh Web Audio / Unity Audio\n- Đóng gói bản dựng Android APK & Test PC"
p_t1_c.font.size = Pt(13)
p_t1_c.font.color.rgb = COLOR_WHITE

card_t2 = add_card(s2, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
tb_t2 = s2.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.8))
tf_t2 = tb_t2.text_frame
tf_t2.word_wrap = True
p_t2_h = tf_t2.paragraphs[0]
p_t2_h.text = "THÀNH VIÊN 02 (HOẶC CÁ NHÂN)"
p_t2_h.font.size = Pt(15)
p_t2_h.font.bold = True
p_t2_h.font.color.rgb = COLOR_CYAN

p_t2_c = tf_t2.add_paragraph()
p_t2_c.text = "\n• Họ và tên: [Điền họ tên Thành viên 2 hoặc Độc lập]\n• Đơn vị: Học sinh THPT / Sinh viên CNTT - ICT\n• Email liên hệ: [Điền email]\n• Số điện thoại: [Điền SĐT]\n\nVai trò trọng tâm:\n- Game Designer (Cân bằng thông số vật lý 5 cấp độ, Game Design Document)\n- 2D Artist / Sketcher (Vẽ tay phác thảo nhân vật Bé Nam & Ji-ho, quả cầu Jegi)\n- Thiết kế giao diện UI/UX phong cách thẻ giấy Ddakji và Slide PPTX"
p_t2_c.font.size = Pt(13)
p_t2_c.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 3: Ý TƯỞNG & ĐIỂM CHẠM VĂN HÓA ====================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3, COLOR_BG_DARK)
add_header(s3, "Ý tưởng lựa chọn game", "Slide 03: Điểm Chạm Văn Hóa & Triết Lý Giao Thoa Việt – Hàn")

card_cul1 = add_card(s3, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_c1 = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_c1 = tb_c1.text_frame
tf_c1.word_wrap = True
tf_c1.paragraphs[0].text = "1. DI SẢN ĐỒNG DẠNG\nĐÁ CẦU & JEGICHAGI"
tf_c1.paragraphs[0].font.size = Pt(14)
tf_c1.paragraphs[0].font.bold = True
tf_c1.paragraphs[0].font.color.rgb = COLOR_GOLD
p_c1_sub = tf_c1.add_paragraph()
p_c1_sub.text = "\n• Trò chơi dân gian phổ biến bậc nhất dịp Tết Nguyên Đán (VN) và Seollal, Chuseok (HQ).\n• Tên gọi 'Jegichagi' (제기차기) cấu thành từ 'Jegi' (quả cầu) và 'Chagi' (dùng chân đá).\n• Mục tiêu nguyên bản: Dùng cạnh bàn chân tâng giữ quả cầu không rơi xuống đất."
p_c1_sub.font.size = Pt(12)
p_c1_sub.font.color.rgb = COLOR_WHITE

card_cul2 = add_card(s3, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_c2 = s3.shapes.add_textbox(Inches(5.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_c2 = tb_c2.text_frame
tf_c2.word_wrap = True
tf_c2.paragraphs[0].text = "2. KHÍ ĐỘNG HỌC\nCỦA QUẢ CẦU THỦ CÔNG"
tf_c2.paragraphs[0].font.size = Pt(14)
tf_c2.paragraphs[0].font.bold = True
tf_c2.paragraphs[0].font.color.rgb = COLOR_RED_VN
p_c2_sub = tf_c2.add_paragraph()
p_c2_sub.text = "\n• Phần đế: Đồng xu kim loại có lỗ hoặc bọc vải/giấy tạo tâm trọng lực kéo xuống.\n• Phần thân: 20 sợi dây nilon dài 20cm xé nhỏ (hoặc lông vịt/lá chuối) tạo lực cản không khí.\n• Cấu trúc giúp quả cầu luôn rơi thẳng đứng có thể dự đoán được quỹ đạo trong game vật lý."
p_c2_sub.font.size = Pt(12)
p_c2_sub.font.color.rgb = COLOR_WHITE

card_cul3 = add_card(s3, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_c3 = s3.shapes.add_textbox(Inches(9.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_c3 = tb_c3.text_frame
tf_c3.word_wrap = True
tf_c3.paragraphs[0].text = "3. TRIẾT LÝ GAMEPLAY\nVƯỢT 5 CẤP ĐỘ DI SẢN"
tf_c3.paragraphs[0].font.size = Pt(14)
tf_c3.paragraphs[0].font.bold = True
tf_c3.paragraphs[0].font.color.rgb = COLOR_CYAN
p_c3_sub = tf_c3.add_paragraph()
p_c3_sub.text = "\n• Luật chơi truyền thống Jegichagi yêu cầu vượt qua 5 cấp độ kỹ thuật chân.\n• Game chuyển hóa thành hành trình qua 5 danh lam thắng cảnh: Đình Làng -> Hội An -> Hạ Long & Jeju -> Bukchon Hanok -> Cung Gyeongbokgung.\n• Tôn vinh tính kiên trì, rèn luyện sự khéo léo của thanh niên hai nước."
p_c3_sub.font.size = Pt(12)
p_c3_sub.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 4: THỂ LOẠI & USP ====================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4, COLOR_BG_DARK)
add_header(s4, "Phân khúc & Điểm mới lạ", "Slide 04: Thể Loại, Đối Tượng Mục Tiêu & Điểm Khác Biệt (USP)")

c4_l = add_card(s4, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
tb_4l = s4.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
tf_4l = tb_4l.text_frame
tf_4l.word_wrap = True
tf_4l.paragraphs[0].text = "THỂ LOẠI & GAMEPLAY HOOK"
tf_4l.paragraphs[0].font.size = Pt(15)
tf_4l.paragraphs[0].font.bold = True
tf_4l.paragraphs[0].font.color.rgb = COLOR_GOLD

p_4l = tf_4l.add_paragraph()
p_4l.text = "\n• Phân khúc: Hyper-casual / Rhythm Precision (Vật lý 1 chạm kết hợp phản xạ nhịp điệu).\n• Game tham khảo thị trường: Flappy Bird, Timberman, Getting Over It.\n• Đối tượng mục tiêu: Giới trẻ gen Z yêu thích game di động giải trí nhanh (30-60 giây/ván), cộng đồng yêu văn hóa Hàn - Việt, học sinh sinh viên.\n• Zero-tutorial Onboarding: Người chơi hiểu luật ngay trong 3 giây mà không cần đọc hướng dẫn dài dòng."
p_4l.font.size = Pt(13)
p_4l.font.color.rgb = COLOR_WHITE

c4_r = add_card(s4, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
tb_4r = s4.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.8))
tf_4r = tb_4r.text_frame
tf_4r.word_wrap = True
tf_4r.paragraphs[0].text = "ĐIỂM MỚI LẠ ĐỘT PHÁ (UNIQUE SELLING POINTS)"
tf_4r.paragraphs[0].font.size = Pt(15)
tf_4r.paragraphs[0].font.bold = True
tf_4r.paragraphs[0].font.color.rgb = COLOR_CYAN

p_4r = tf_4r.add_paragraph()
p_4r.text = "\n1. Không 'Reskin' Hời Hợt:\nCơ chế gameplay gắn chặt vào vật lý khí động học của quả cầu Jegi thật (trọng tâm đồng xu và lực cản tua rua).\n\n2. 5 Biến Thể Kỹ Thuật Chân:\nKhông đơn điệu một cú đá; nhân vật tự động biểu diễn đá má trong, đá vắt chéo, đá kiểng, và tâng kép Fever Mode.\n\n3. Minigame Chế Tác Cầu Thủ Công:\nNgười chơi tự tay trải nghiệm 5 bước xé 20 sợi nilon buộc đồng xu mở khóa trang bị."
p_4r.font.size = Pt(13)
p_4r.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 5: NHÂN VẬT & BỐI CẢNH ====================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5, COLOR_BG_DARK)
add_header(s5, "Tuyến nhân vật & Bối cảnh", "Slide 05: Nhân Vật Chính, Nhân Vật Phụ & Cốt Truyện Giao Lưu")

c5_1 = add_card(s5, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_51 = s5.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_51 = tb_51.text_frame
tf_51.word_wrap = True
tf_51.paragraphs[0].text = "🇻🇳 BÉ NAM (VIỆT NAM)"
tf_51.paragraphs[0].font.size = Pt(14)
tf_51.paragraphs[0].font.bold = True
tf_51.paragraphs[0].font.color.rgb = COLOR_RED_VN
p_51 = tf_51.add_paragraph()
p_51.text = "\n• Tạo hình: Chibi 3 đầu thân mặc Áo tấc cách tân khăn đóng, đi giày vải họa tiết Trống đồng.\n• Tính cách: Lém lỉnh, nhanh nhẹn, chuyên gia đá cầu kiểng vắt chéo chân.\n• Biểu cảm động: Cười tươi khi cầu an toàn, toát mồ hôi hột khi cầu rơi sát đất, khóc mếu hài hước khi thua."
p_51.font.size = Pt(12)
p_51.font.color.rgb = COLOR_WHITE

c5_2 = add_card(s5, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_52 = s5.shapes.add_textbox(Inches(5.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_52 = tb_52.text_frame
tf_52.word_wrap = True
tf_52.paragraphs[0].text = "🇰🇷 BÉ JI-HO (HÀN QUỐC)"
tf_52.paragraphs[0].font.size = Pt(14)
tf_52.paragraphs[0].font.bold = True
tf_52.paragraphs[0].font.color.rgb = COLOR_BLUE_KR
p_52 = tf_52.add_paragraph()
p_52.text = "\n• Tạo hình: Chibi mặc Hanbok lễ hội (Baji & Jeogori), thắt nơ Goreum, đầu đeo băng đô, đi giày Hwahye.\n• Tính cách: Điềm tĩnh, kiên định, chuyên gia giữ thăng bằng chân trụ Kkangchung.\n• Biểu cảm động: Mắt rực lửa quyết tâm khi vào chuỗi Combo Perfect."
p_52.font.size = Pt(12)
p_52.font.color.rgb = COLOR_WHITE

c5_3 = add_card(s5, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_53 = s5.shapes.add_textbox(Inches(9.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_53 = tb_53.text_frame
tf_53.word_wrap = True
tf_53.paragraphs[0].text = "NPCs & HÀNH TRÌNH BỐI CẢNH"
tf_53.paragraphs[0].font.size = Pt(14)
tf_53.paragraphs[0].font.bold = True
tf_53.paragraphs[0].font.color.rgb = COLOR_GOLD
p_53 = tf_53.add_paragraph()
p_53.text = "\n• Tuyến nhân vật phụ: Ông Tiên Thứ Chỉ gõ trống khẩu; Chú Mèo Vàng VN và Chú Chó Jindo / Hổ Trắng cổ vũ quanh sân.\n• Cốt truyện: Hai bạn nhỏ gặp gỡ tại Hội làng hữu nghị, cùng thử thách tài tâng cầu qua 5 vùng đất nối liền Việt Nam và Hàn Quốc."
p_53.font.size = Pt(12)
p_53.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 6: SKETCH NHÂN VẬT & ĐẠO CỤ ====================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6, COLOR_BG_DARK)
add_header(s6, "Bản vẽ phác thảo (Lợi thế cuộc thi)", "Slide 06: Bản Vẽ Tay Sketch Nhân Vật & Giải Phẫu Quả Cầu Jegi")

c6_l = add_card(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
tb_6l = s6.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
tf_6l = tb_6l.text_frame
tf_6l.word_wrap = True
tf_6l.paragraphs[0].text = "PHÁC THẢO NHÂN VẬT CHIBI TỶ LỆ 3 ĐẦU THÂN"
tf_6l.paragraphs[0].font.size = Pt(14)
tf_6l.paragraphs[0].font.bold = True
tf_6l.paragraphs[0].font.color.rgb = COLOR_GOLD

p_6l = tf_6l.add_paragraph()
p_6l.text = "\n[KHUNG DÀNH CHO ẢNH CHỤP SKETCH TAY A4]\n\n• Bản phác thảo bút chì giữ nguyên các trục đối xứng gióng ngang đầu - vai - hông - bàn chân.\n• Tư thế 01: Đứng trụ 1 chân, co đầu gối, bàn chân nghiêng góc 45 độ đón cầu.\n• Tư thế 02: Xoạc chân sát mặt đất (Diving Save) khi cứu quả cầu rơi ngoài tầm với.\n• Điểm nhấn văn hóa: Chi tiết hoa văn Trống đồng thêu trên giày Bé Nam và đường chỉ may nơ áo Goreum của Bé Ji-ho."
p_6l.font.size = Pt(12)
p_6l.font.color.rgb = COLOR_WHITE

c6_r = add_card(s6, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
tb_6r = s6.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.8))
tf_6r = tb_6r.text_frame
tf_6r.word_wrap = True
tf_6r.paragraphs[0].text = "SƠ ĐỒ TÁCH LỚP (EXPLODED VIEW) QUẢ CẦU JEGI"
tf_6r.paragraphs[0].font.size = Pt(14)
tf_6r.paragraphs[0].font.bold = True
tf_6r.paragraphs[0].font.color.rgb = COLOR_CYAN

p_6r = tf_6r.add_paragraph()
p_6r.text = "\n[KHUNG DÀNH CHO ẢNH SKETCH GIẢI PHẪU ĐẠO CỤ]\n\n1. Phần Đỉnh: 20 sợi dây nilon dài 20cm xé tước nhỏ -> Tạo lực cản khí động học F_drag hướng ngược chiều rơi.\n2. Phần Cổ: Vòng thắt nút bện dây dù cố định trọng tâm.\n3. Phần Đế: Đồng xu kim loại có lỗ bọc lớp nilon bóng -> Tạo trọng tâm hạ thấp (G) và phát tiếng kêu 'Keng' giòn giã khi chạm giày.\n4. Bộ sưu tập 5 Quả Cầu: Cầu Nilon, Cầu Giấy Dó, Cầu Túi Vải Chuseok, Cầu Mây Ngũ Sắc, Cầu Rồng Lạc - Yong."
p_6r.font.size = Pt(12)
p_6r.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 7: SKETCH BỐI CẢNH 5 CẤP ĐỘ ====================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7, COLOR_BG_DARK)
add_header(s7, "Bản vẽ phác thảo bối cảnh", "Slide 07: Bối Cảnh Màn Chơi & Hành Trình 5 Cấp Độ Văn Hóa")

c7_box = add_card(s7, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.2))
tb_7 = s7.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.1), Inches(4.8))
tf_7 = tb_7.text_frame
tf_7.word_wrap = True
tf_7.paragraphs[0].text = "HÀNH TRÌNH 5 MÀN CHƠI BIỂU TƯỢNG VIỆT NAM – HÀN QUỐC (PARALLAX 3 LỚP)"
tf_7.paragraphs[0].font.size = Pt(14)
tf_7.paragraphs[0].font.bold = True
tf_7.paragraphs[0].font.color.rgb = COLOR_GOLD

p_7 = tf_7.add_paragraph()
p_7.text = "\n[Cấp 1: 0 - 15 Điểm] Sân Đình Làng Bắc Bộ: Sân gạch đỏ, cây đa cổ thụ, cổng tam quan; trời nắng dịu, gió lặng.\n[Cấp 2: 16 - 35 Điểm] Phố Cổ Hội An Đêm Đèn Lồng: Đèn lồng lung linh soi bóng sông Hoài; bắt đầu có gió nhẹ từ phải sang trái.\n[Cấp 3: 36 - 60 Điểm] Giao Lộ Hạ Long & Đảo Jeju: Hòn Trống Mái hòa cùng Tượng đá Harubang; gió biển giật đổi chiều ngẫu nhiên.\n[Cấp 4: 61 - 90 Điểm] Làng Cổ Bukchon Hanok Mùa Thu: Mái ngói xám đan xen lá vàng ngân hạnh rơi nhẹ cản tầm nhìn.\n[Cấp 5: > 90 Điểm] Cung Điện Gyeongbokgung Đêm Tuyết: Tuyết trắng rơi dày, sân trơn trượt quán tính; gió bão tuyết thử thách tối thượng."
p_7.font.size = Pt(12)
p_7.font.color.rgb = COLOR_WHITE

p_7_sub = tf_7.add_paragraph()
p_7_sub.text = "\n* Ghi chú kỹ thuật: Thiết kế phân tách rõ 3 lớp Layer: Tiền cảnh (Nút bấm Ddakji) -> Trung cảnh (Nhân vật & Vùng đá cầu Kick-zone) -> Hậu cảnh (Di tích kiến trúc cuộn Parallax mượt mà)."
p_7_sub.font.size = Pt(11)
p_7_sub.font.color.rgb = COLOR_MUTED

# ==================== SLIDE 8: CORE GAMEPLAY MECHANICS ====================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8, COLOR_BG_DARK)
add_header(s8, "Cơ chế lối chơi", "Slide 08: Core Gameplay Loop & Công Thức Vật Lý 2D")

c8_l = add_card(s8, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
tb_8l = s8.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
tf_8l = tb_8l.text_frame
tf_8l.word_wrap = True
tf_8l.paragraphs[0].text = "VÒNG LẶP CỐT LÕI (CORE GAMEPLAY LOOP)"
tf_8l.paragraphs[0].font.size = Pt(14)
tf_8l.paragraphs[0].font.bold = True
tf_8l.paragraphs[0].font.color.rgb = COLOR_GOLD

p_8l = tf_8l.add_paragraph()
p_8l.text = "\n1. Khởi phát (Serve): Nhân vật tung nhẹ quả cầu lên không trung.\n2. Quan sát & Dự đoán (Anticipation): Quả cầu chịu trọng lực rơi xuống; vòng Target Ring hiển thị tầm chân vươn tới.\n3. Thao tác 1 chạm (One-Tap Input): Người chơi chạm vào màn hình đúng khoảnh khắc cầu vào vùng đá.\n4. Phản hồi vật lý (Physics): Quả cầu nảy lên theo vector lực tương ứng điểm chạm.\n5. Thắng/Thua: Giữ cầu tâng liên tục tích lũy điểm; chỉ 1 lần cầu chạm sàn là Game Over tức thì."
p_8l.font.size = Pt(12)
p_8l.font.color.rgb = COLOR_WHITE

c8_r = add_card(s8, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
tb_8r = s8.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.8))
tf_8r = tb_8r.text_frame
tf_8r.word_wrap = True
tf_8r.paragraphs[0].text = "MÔ HÌNH TOÁN HỌC & 3 VÙNG CHẤM ĐIỂM"
tf_8r.paragraphs[0].font.size = Pt(14)
tf_8r.paragraphs[0].font.bold = True
tf_8r.paragraphs[0].font.color.rgb = COLOR_CYAN

p_8r = tf_8r.add_paragraph()
p_8r.text = "\n• Công thức độ lệch tâm: Δx = x_jegi - x_input\n• Vector lực đẩy: F_kick = (Δx * k_x, F_y * k_timing)\n\n3 Phân bậc chấm điểm chuẩn xác:\n1. PERFECT (|Δx| <= 0.15m): Cầu bay thẳng đứng ổn định, nổ hạt sáng vàng kim, +3 điểm, tăng Fever.\n2. GREAT (0.15m < |Δx| <= 0.45m): Cầu bay lệch nhẹ, nhân vật bước dịch chân theo đỡ, +1 điểm.\n3. GRAZE / CỨU CẦU SÁT ĐẤT (|Δx| > 0.45m): Nhân vật xoạc chân hết cỡ, cầu nảy thấp và xoáy mạnh góc omega."
p_8r.font.size = Pt(12)
p_8r.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 9: UI/UX WIREFRAME ====================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9, COLOR_BG_DARK)
add_header(s9, "Thiết kế giao diện", "Slide 09: Kiến Trúc UI/UX Trực Quan & Vùng Ngón Cái (One-Thumb)")

c9_1 = add_card(s9, Inches(0.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_91 = s9.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_91 = tb_91.text_frame
tf_91.word_wrap = True
tf_91.paragraphs[0].text = "TRIẾT LÝ MÀN HÌNH DỌC 9:16"
tf_91.paragraphs[0].font.size = Pt(14)
tf_91.paragraphs[0].font.bold = True
tf_91.paragraphs[0].font.color.rgb = COLOR_GOLD
p_91 = tf_91.add_paragraph()
p_91.text = "\n• Chuẩn công thái học One-Thumb:\nToàn bộ 85% không gian trên dành trọn cho quỹ đạo bay của quả cầu. Thao tác chạm đều nằm ở 1/3 dưới.\n• Đa nền tảng thông minh:\nTrên PC, game hiển thị khung dọc trung tâm, hai bên trang trí hoa văn Trống đồng Đông Sơn và họa tiết Dancheong cung đình Hàn Quốc."
p_91.font.size = Pt(12)
p_91.font.color.rgb = COLOR_WHITE

c9_2 = add_card(s9, Inches(4.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_92 = s9.shapes.add_textbox(Inches(5.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_92 = tb_92.text_frame
tf_92.word_wrap = True
tf_92.paragraphs[0].text = "NÚT BẤM THẺ GIẤY DDAKJI"
tf_92.paragraphs[0].font.size = Pt(14)
tf_92.paragraphs[0].font.bold = True
tf_92.paragraphs[0].font.color.rgb = COLOR_RED_VN
p_92 = tf_92.add_paragraph()
p_92.text = "\n• Ngôn ngữ Diegetic Cultural UI:\nMọi nút bấm (CHƠI NGAY, XƯỞNG CẦU, THỬ LẠI) đều được tạo hình như vẩy đập giấy Ddakji chữ thập nổi khối 3D.\n• Hiệu ứng xúc giác & âm thanh:\nKhi bấm, nút lún xuống kèm tiếng 'Bẹp!' giòn giã mô phỏng cú đập giấy quen thuộc trong tuổi thơ hai nước."
p_92.font.size = Pt(12)
p_92.font.color.rgb = COLOR_WHITE

c9_3 = add_card(s9, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2))
tb_93 = s9.shapes.add_textbox(Inches(9.0), Inches(1.8), Inches(3.3), Inches(4.8))
tf_93 = tb_93.text_frame
tf_93.word_wrap = True
tf_93.paragraphs[0].text = "HỆ THỐNG PHẢN HỒI GAME FEEL"
tf_93.paragraphs[0].font.size = Pt(14)
tf_93.paragraphs[0].font.bold = True
tf_93.paragraphs[0].font.color.rgb = COLOR_CYAN
p_93 = tf_93.add_paragraph()
p_93.text = "\n• Squash & Stretch: Quả cầu hơi dẹt 0.05s khi tiếp xúc bàn chân rồi bung dài theo hướng bay.\n• Camera Shake: Rung lắc màn hình nhẹ khi Perfect hoặc khi Game Over.\n• Trail Renderer: Vẽ dải lụa ngũ sắc uốn lượn theo đuôi nilon của quả cầu.\n• Instant Retry: Vào lại ván mới chỉ sau 0.5s."
p_93.font.size = Pt(12)
p_93.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 10: CÔNG NGHỆ & BẢN QUYỀN ====================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10, COLOR_BG_DARK)
add_header(s10, "Kỹ thuật & Pháp lý", "Slide 10: Kế Hoạch Công Nghệ Trên Unity & Cam Kết Bản Quyền")

c10_l = add_card(s10, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
tb_10l = s10.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.0), Inches(4.8))
tf_10l = tb_10l.text_frame
tf_10l.word_wrap = True
tf_10l.paragraphs[0].text = "KIẾN TRÚC KỸ THUẬT UNITY 2D"
tf_10l.paragraphs[0].font.size = Pt(14)
tf_10l.paragraphs[0].font.bold = True
tf_10l.paragraphs[0].font.color.rgb = COLOR_GOLD

p_10l = tf_10l.add_paragraph()
p_10l.text = "\n• Phiên bản công cụ: Unity Engine 2022 LTS / Unity 6.\n• Cấu trúc Scene duy nhất (Single-scene Architecture) tải tức thì trong 1 giây, hoàn toàn không có độ trễ tải màn.\n• Vật lý 2D: Tối ưu hóa Rigidbody2D + CircleCollider2D, xử lý FixedUpdate đảm bảo 60 FPS ổn định trên mọi dòng máy Android tầm trung.\n• Data Architecture: Quản lý danh mục 5 quả cầu bằng ScriptableObjects sạch sẽ, dễ bảo trì."
p_10l.font.size = Pt(12)
p_10l.font.color.rgb = COLOR_WHITE

c10_r = add_card(s10, Inches(6.9), Inches(1.6), Inches(5.6), Inches(5.2))
tb_10r = s10.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.0), Inches(4.8))
tf_10r = tb_10r.text_frame
tf_10r.word_wrap = True
tf_10r.paragraphs[0].text = "CAM KẾT BẢN QUYỀN (IP COMPLIANCE)"
tf_10r.paragraphs[0].font.size = Pt(14)
tf_10r.paragraphs[0].font.bold = True
tf_10r.paragraphs[0].font.color.rgb = COLOR_CYAN

p_10r = tf_10r.add_paragraph()
p_10r.text = "\n• Đồ họa: 100% tài nguyên nhân vật Bé Nam, Bé Ji-ho và quả cầu được số hóa trực tiếp từ bản vẽ tay phác thảo của nhóm dự thi.\n• Âm thanh: Thu âm tiếng đá cầu thực tế; kết hợp các bản phối nhạc cụ truyền thống dân gian miễn phí bản quyền thương mại (Creative Commons Zero - CC0).\n• Mã nguồn: 100% viết tay độc lập, không vi phạm bản quyền hay sử dụng mã nguồn đóng trái phép."
p_10r.font.size = Pt(12)
p_10r.font.color.rgb = COLOR_WHITE

# ==================== SLIDE 11: LỜI KẾT & DEMO ====================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11, COLOR_BG_DARK)
add_header(s11, "Tổng kết & Demo", "Slide 11: Tầm Nhìn Dự Án, Trải Nghiệm Demo & Lời Cảm Ơn")

c11_box = add_card(s11, Inches(1.5), Inches(1.6), Inches(10.333), Inches(5.2))
tb_11 = s11.shapes.add_textbox(Inches(1.8), Inches(1.8), Inches(9.7), Inches(4.8))
tf_11 = tb_11.text_frame
tf_11.word_wrap = True

tf_11.paragraphs[0].text = "ĐỘC CƯỚC TÂNG CẦU: NHỊP CẦU NỐI LIỀN DI SẢN TRẺ VIỆT – HÀN"
tf_11.paragraphs[0].font.size = Pt(18)
tf_11.paragraphs[0].font.bold = True
tf_11.paragraphs[0].font.color.rgb = COLOR_GOLD
tf_11.paragraphs[0].alignment = PP_ALIGN.CENTER

p_11_body = tf_11.add_paragraph()
p_11_body.text = "\n• Tầm nhìn phát triển: Đưa trò chơi dân gian lên nền tảng số hiện đại, tạo nên một tựa game Hyper-casual có sức lan tỏa tự nhiên trên Google Play Store.\n• Tính khả thi tuyệt đối: Sản phẩm đã có bản Prototype kiểm thử mượt mà, sẵn sàng xuất file APK và video trải nghiệm thực tế.\n\nKÍNH MỜI BAN GIÁM KHẢO TRẢI NGHIỆM BẢN DEMO GAME TRÊN THIẾT BỊ\n\nChân thành cảm ơn Trung tâm Văn hóa Hàn Quốc tại Việt Nam & Hội đồng Giám khảo KGW2026!"
p_11_body.font.size = Pt(14)
p_11_body.font.color.rgb = COLOR_WHITE
p_11_body.alignment = PP_ALIGN.CENTER

output_path = "/home/nor/Storage/Projects/TUẦN LỄ GAME HÀN QUỐC 2026/docs/Du_Thi_Game_KGW2026_Tang_Bounce_It.pptx"
os.makedirs("/home/nor/Storage/Projects/TUẦN LỄ GAME HÀN QUỐC 2026/docs", exist_ok=True)
prs.save(output_path)
prs.save("/home/nor/Storage/Projects/TUẦN LỄ GAME HÀN QUỐC 2026/Du_Thi_Game_KGW2026_Tang_Bounce_It.pptx")
print(f"Presentation successfully saved to: {output_path}")
