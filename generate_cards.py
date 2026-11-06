import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = "/Users/kimkyoungil/.gemini/antigravity/scratch/customer-response-cardnews/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

def get_font(size, weight="regular"):
    # 0: Regular, 2: Medium, 4: SemiBold, 6: Bold
    indices = {
        "regular": 0,
        "medium": 2,
        "semibold": 4,
        "bold": 6
    }
    idx = indices.get(weight, 0)
    return ImageFont.truetype(FONT_PATH, size=size, index=idx)

WIDTH, HEIGHT = 1080, 1080

# Color Palette
BG_COLOR = (248, 250, 252)        # Slate 50
TEXT_MAIN = (15, 23, 42)          # Slate 900
TEXT_MUTED = (100, 116, 139)      # Slate 500
PRIMARY_BLUE = (37, 99, 235)      # Blue 600
PRIMARY_LIGHT = (239, 246, 255)   # Blue 50
PRIMARY_DARK = (29, 78, 216)      # Blue 700
ACCENT_RED = (239, 68, 68)        # Red 500
ACCENT_RED_LIGHT = (254, 242, 242)# Red 50
ACCENT_ORANGE = (245, 158, 11)    # Amber 500
CARD_BG = (255, 255, 255)         # Pure White
BORDER_COLOR = (226, 232, 240)    # Slate 200

def create_base(slide_num, total_slides=7, tag="사장님 노무 가이드"):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Top decorative line
    draw.rectangle([(0, 0), (WIDTH, 12)], fill=PRIMARY_BLUE)
    
    # Top Header: Tag & Slide Indicator
    # Tag Badge
    tag_font = get_font(24, "semibold")
    tag_w = draw.textlength(tag, font=tag_font)
    badge_x, badge_y = 70, 60
    draw.rounded_rectangle(
        [(badge_x, badge_y), (badge_x + tag_w + 32, badge_y + 44)],
        radius=22,
        fill=PRIMARY_LIGHT,
        outline=PRIMARY_BLUE,
        width=1
    )
    draw.text((badge_x + 16, badge_y + 9), tag, font=tag_font, fill=PRIMARY_BLUE)
    
    # Slide Number
    page_font = get_font(26, "bold")
    page_text = f"{slide_num:02d} / {total_slides:02d}"
    page_w = draw.textlength(page_text, font=page_font)
    draw.text((WIDTH - 70 - page_w, 68), page_text, font=page_font, fill=TEXT_MUTED)
    
    # Bottom Footer: Brand Info
    footer_font = get_font(22, "medium")
    brand_text = "스마트한 매장 관리의 시작 ｜ 알바급여정석"
    draw.line([(70, HEIGHT - 80), (WIDTH - 70, HEIGHT - 80)], fill=BORDER_COLOR, width=1)
    draw.text((70, HEIGHT - 60), brand_text, font=footer_font, fill=TEXT_MUTED)
    
    web_text = "app.albapay.co.kr"
    web_w = draw.textlength(web_text, font=footer_font)
    draw.text((WIDTH - 70 - web_w, HEIGHT - 60), web_text, font=footer_font, fill=PRIMARY_BLUE)
    
    return img, draw

# ==================== SLIDE 1 (COVER) ====================
def draw_slide_1():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (15, 23, 42)) # Deep Navy Background
    draw = ImageDraw.Draw(img)
    
    # Top accent line
    draw.rectangle([(0, 0), (WIDTH, 14)], fill=ACCENT_RED)
    
    # Badge
    tag_font = get_font(26, "bold")
    draw.rounded_rectangle([(70, 70), (280, 124)], radius=27, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((95, 82), "긴급 노무 가이드", font=tag_font, fill=(248, 113, 113))
    
    # Page Indicator
    page_font = get_font(26, "bold")
    draw.text((WIDTH - 150, 82), "01 / 07", font=page_font, fill=(148, 163, 184))
    
    # Warning Question
    q_font = get_font(42, "bold")
    draw.text((70, 190), "“손님이 알바에게 욕설을 했습니다.”", font=q_font, fill=(203, 213, 225))
    
    # Main Headline
    h1_font = get_font(72, "bold")
    draw.text((70, 260), "손님이 알바에게", font=h1_font, fill=(255, 255, 255))
    draw.text((70, 350), "욕설·폭언했다면?", font=h1_font, fill=(248, 113, 113))
    
    # Callout Box
    box_top = 480
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 340)], radius=24, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    # Quote in box
    c_sub = get_font(32, "semibold")
    draw.text((110, box_top + 45), "❌ “손님이니까 네가 조금만 참아”", font=c_sub, fill=(252, 165, 165))
    
    c_desc = get_font(28, "medium")
    draw.text((110, box_top + 105), "그냥 넘겼다간 사장님이 법적 책임을 질 수 있습니다!", font=c_desc, fill=(226, 232, 240))
    
    # Divider in box
    draw.line([(110, box_top + 165), (WIDTH - 110, box_top + 165)], fill=(51, 65, 85), width=1)
    
    # Bottom key takeaway in box
    k_font = get_font(30, "bold")
    draw.text((110, box_top + 195), "💡 산업안전보건법 제41조", font=k_font, fill=(96, 165, 250))
    
    k_desc = get_font(27, "regular")
    draw.text((110, box_top + 245), "사업주는 고객응대근로자의 건강장해를 예방하고", font=k_desc, fill=(203, 213, 225))
    draw.text((110, box_top + 285), "폭언 발생 시 즉각적인 보호조치를 해야 할 의무가 있습니다.", font=k_desc, fill=(203, 213, 225))
    
    # Footer
    f_font = get_font(24, "medium")
    draw.text((70, HEIGHT - 70), "알바급여정석 ｜ 사장님이 꼭 알아야 할 필수 대응 매뉴얼", font=f_font, fill=(148, 163, 184))
    
    img.save(f"{OUTPUT_DIR}/card_01.png")

# ==================== SLIDE 2 (CASE STUDY) ====================
def draw_slide_2():
    img, draw = create_base(2, 7, "실제 발생 사례")
    
    # Main Title
    title_font = get_font(50, "bold")
    draw.text((70, 140), "“이것도 제대로 못 해?”", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 205), "폭언에 손 떨며 울어버린 알바생", font=title_font, fill=PRIMARY_BLUE)
    
    # Situation Card
    box_top = 290
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 250)], radius=20, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    s_title = get_font(28, "bold")
    draw.text((105, box_top + 30), "📍 카페에서 일어난 가상 사례", font=s_title, fill=PRIMARY_BLUE)
    
    s_body = get_font(25, "regular")
    lines = [
        "• 음료 제조가 조금 늦어졌다는 이유로 손님이 고성과 욕설 시작",
        "• 직원이 거듭 사과했으나 모욕적인 폭언이 계속 이어짐",
        "• 직원은 충격으로 손을 떨고 더 이상 고객 응대가 불가능한 상태",
        "• 사장님: “손님 달래야 하니 조금만 참아봐...” (위험한 대처!)"
    ]
    y_off = box_top + 80
    for l in lines:
        draw.text((105, y_off), l, font=s_body, fill=TEXT_MAIN)
        y_off += 38
        
    # Warning Callout
    w_top = 570
    draw.rounded_rectangle([(70, w_top), (WIDTH - 70, w_top + 360)], radius=20, fill=ACCENT_RED_LIGHT, outline=(254, 202, 202), width=2)
    
    w_title = get_font(30, "bold")
    draw.text((105, w_top + 35), "⚠️ 직원의 안전과 건강이 최우선입니다", font=w_title, fill=ACCENT_RED)
    
    w_body = get_font(26, "regular")
    w_lines = [
        "고객의 모든 불만 제기가 법적 폭언은 아닙니다.",
        "하지만 욕설, 위협, 모욕 등으로 직원에게 신체적·정신적",
        "건강장해가 발생하거나 발생할 현저한 우려가 있다면,",
        "",
        "사업주에게 즉각적인 법적 ‘보호조치 의무’가 발생합니다!"
    ]
    wy = w_top + 90
    for l in w_lines:
        if l == w_lines[-1]:
            draw.text((105, wy), l, font=get_font(26, "bold"), fill=TEXT_MAIN)
        else:
            draw.text((105, wy), l, font=w_body, fill=TEXT_MAIN)
        wy += 38
        
    img.save(f"{OUTPUT_DIR}/card_02.png")

# ==================== SLIDE 3 (LEGAL OBLIGATION) ====================
def draw_slide_3():
    img, draw = create_base(3, 7, "법적 근거")
    
    title_font = get_font(50, "bold")
    draw.text((70, 140), "고객응대근로자 보호,", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 205), "법으로 정해진 사장님의 ‘의무’입니다", font=title_font, fill=PRIMARY_BLUE)
    
    # Subtitle
    sub_font = get_font(26, "medium")
    draw.text((70, 280), "산업안전보건법 제41조 (고객의 폭언 등으로 인한 건강장해 예방)", font=sub_font, fill=TEXT_MUTED)
    
    # 3 Preventive Measures
    box_top = 340
    boxes = [
        ("1. 폭언 방지 안내문 게시 / 음성 안내", "매장 계산대나 입구 등에 고객 폭언 금지 안내문 비치", "📢"),
        ("2. 고객응대업무 대응 매뉴얼 마련", "폭언 발생 시 응대 중단 및 관리자 호출 절차 수립", "📋"),
        ("3. 건강장해 예방 및 대응 교육 실시", "직원이 혼자 감당하지 않고 매뉴얼대로 행동하도록 교육", "🧑‍🏫")
    ]
    
    by = box_top
    for title, desc, icon in boxes:
        draw.rounded_rectangle([(70, by), (WIDTH - 70, by + 145)], radius=18, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        # Left color bar
        draw.rounded_rectangle([(70, by), (82, by + 145)], radius=6, fill=PRIMARY_BLUE)
        
        # Icon & Title
        draw.text((105, by + 28), f"{icon}  {title}", font=get_font(28, "bold"), fill=TEXT_MAIN)
        draw.text((105, by + 82), desc, font=get_font(24, "regular"), fill=TEXT_MUTED)
        by += 165
        
    # Note at bottom
    note_font = get_font(24, "semibold")
    draw.text((70, 855), "※ 단순히 안내문 하나 붙였다고 모든 예방 의무가 끝난 것은 아닙니다!", font=note_font, fill=ACCENT_RED)
    draw.text((70, 895), "   평소 매뉴얼과 절차를 마련해 두는 사전 조치가 필수입니다.", font=get_font(22, "regular"), fill=TEXT_MUTED)
    
    img.save(f"{OUTPUT_DIR}/card_03.png")

# ==================== SLIDE 4 (ACTION STEPS) ====================
def draw_slide_4():
    img, draw = create_base(4, 7, "현장 대응 가이드")
    
    title_font = get_font(50, "bold")
    draw.text((70, 140), "폭언 발생 시", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 205), "사장님이 즉시 해야 할 4대 보호조치", font=title_font, fill=PRIMARY_BLUE)
    
    sub_font = get_font(25, "medium")
    draw.text((70, 280), "산업안전보건법 시행령 제41조에서 규정한 필수 조치입니다.", font=sub_font, fill=TEXT_MUTED)
    
    # 2x2 Grid of Actions
    grid_data = [
        ("① 업무 일시 중단 & 전환", "직원을 현장에서 즉시 분리하고\n사장님 또는 관리자가 직접 인계", PRIMARY_LIGHT, PRIMARY_BLUE),
        ("② 휴게시간 연장 보장", "놀란 직원의 안정을 위해\n충분한 휴식 시간 추가 제공", CARD_BG, (16, 185, 129)),
        ("③ 치료 및 심리상담 지원", "신체적·정신적 피해 발생 시\n병원 치료 및 전문 상담 지원 검토", CARD_BG, (139, 92, 246)),
        ("④ 법적 대응 지원", "폭행·협박 지속 시 경찰 신고 및\n고소·손해배상 등 법적 조치 협력", ACCENT_RED_LIGHT, ACCENT_RED)
    ]
    
    # Grid coordinates
    cols = [(70, 520), (560, WIDTH - 70)]
    rows = [(340, 580), (610, 850)]
    
    idx = 0
    for r_top, r_bot in rows:
        for c_left, c_right in cols:
            title, desc, bg, accent = grid_data[idx]
            draw.rounded_rectangle([(c_left, r_top), (c_right, r_bot)], radius=20, fill=bg, outline=BORDER_COLOR, width=2)
            
            # Badge / Title
            draw.text((c_left + 25, r_top + 30), title, font=get_font(26, "bold"), fill=accent)
            
            # Desc
            draw.text((c_left + 25, r_top + 90), desc, font=get_font(23, "regular"), fill=TEXT_MAIN, spacing=10)
            idx += 1
            
    # Bottom emphasize
    draw.text((70, 880), "💡 핵심: “직원 혼자 감당하게 두지 않고 즉시 분리·보호하는 것”", font=get_font(25, "bold"), fill=TEXT_MAIN)
    
    img.save(f"{OUTPUT_DIR}/card_04.png")

# ==================== SLIDE 5 (5-PERSON & RETALIATION) ====================
def draw_slide_5():
    img, draw = create_base(5, 7, "주의사항 & Q&A")
    
    title_font = get_font(50, "bold")
    draw.text((70, 140), "“우리 매장은 5인 미만인데도", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 205), "보호조치를 꼭 해야 하나요?”", font=title_font, fill=PRIMARY_BLUE)
    
    # Big Answer Box
    a_top = 290
    draw.rounded_rectangle([(70, a_top), (WIDTH - 70, a_top + 260)], radius=22, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    draw.text((105, a_top + 35), "Q. 직원이 1~2명뿐인 작은 매장도 적용되나요?", font=get_font(28, "bold"), fill=TEXT_MAIN)
    
    ans_box_y = a_top + 85
    draw.rounded_rectangle([(105, ans_box_y), (WIDTH - 105, ans_box_y + 140)], radius=14, fill=PRIMARY_LIGHT)
    draw.text((130, ans_box_y + 20), "A. 네! 적용될 수 있습니다.", font=get_font(28, "bold"), fill=PRIMARY_BLUE)
    draw.text((130, ans_box_y + 65), "산업안전보건법은 근로기준법과 적용 체계가 다릅니다.\n상시근로자 5인 미만이라는 이유만으로 당연 제외되지 않습니다.", font=get_font(23, "regular"), fill=TEXT_MAIN, spacing=6)
    
    # Retaliation Warning Box
    ret_top = 580
    draw.rounded_rectangle([(70, ret_top), (WIDTH - 70, ret_top + 340)], radius=22, fill=(254, 242, 242), outline=(252, 165, 165), width=2)
    
    draw.text((105, ret_top + 35), "🚨 사장님이 가장 주의해야 할 법적 처벌 조항!", font=get_font(28, "bold"), fill=ACCENT_RED)
    
    r_lines = [
        "• 산업안전보건법 제41조 제3항 (불리한 처우 금지)",
        "• 직원이 폭언으로 인해 업무 중단이나 보호조치를 요구했다는 이유로",
        "  해고, 징계, 근로시간 단축 등 '불이익'을 주어서는 절대 안 됩니다.",
        "",
        "⚠️ 위반 시 1년 이하의 징역 또는 1천만원 이하의 벌금에 처해질 수 있습니다."
    ]
    
    ry = ret_top + 95
    for l in r_lines:
        if "⚠️" in l:
            draw.text((105, ry), l, font=get_font(24, "bold"), fill=ACCENT_RED)
        elif "•" in l and "제41조" in l:
            draw.text((105, ry), l, font=get_font(25, "bold"), fill=TEXT_MAIN)
        else:
            draw.text((105, ry), l, font=get_font(24, "regular"), fill=TEXT_MAIN)
        ry += 38
        
    img.save(f"{OUTPUT_DIR}/card_05.png")

# ==================== SLIDE 6 (CHECKLIST) ====================
def draw_slide_6():
    img, draw = create_base(6, 7, "실천 체크리스트")
    
    title_font = get_font(50, "bold")
    draw.text((70, 140), "고객 폭언 대비", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 205), "사장님 필수 점검 체크리스트 5", font=title_font, fill=PRIMARY_BLUE)
    
    sub_font = get_font(25, "medium")
    draw.text((70, 275), "지금 우리 매장에는 준비가 되어 있는지 확인해보세요!", font=sub_font, fill=TEXT_MUTED)
    
    checks = [
        ("1. 고객 폭언 예방 안내문 게시", "계산대, 키오스크, 출입구 등에 배려 요청 문구 부착"),
        ("2. 비상상황 고객응대 매뉴얼 수립", "폭언 시작 시 1차 경고 후 관리자 인계 원칙 공유"),
        ("3. 직원 교육 및 대응 절차 숙지", "혼자 참지 않고 즉시 요청할 수 있는 분위기 조성"),
        ("4. 사건 발생 시 즉각적인 보호조치", "업무 분리, 휴게시간 연장, 심리적 안정 조치 실행"),
        ("5. 사건 경위 및 근무기록 증빙 보관", "발생 시각, 당시 근무자, 대응 조치 일지 기록")
    ]
    
    cy = 330
    for title, desc in checks:
        draw.rounded_rectangle([(70, cy), (WIDTH - 70, cy + 98)], radius=16, fill=CARD_BG, outline=BORDER_COLOR, width=2)
        
        # Checkbox square
        draw.rounded_rectangle([(95, cy + 24), (145, cy + 74)], radius=10, fill=PRIMARY_LIGHT, outline=PRIMARY_BLUE, width=2)
        draw.text((108, cy + 27), "✓", font=get_font(32, "bold"), fill=PRIMARY_BLUE)
        
        # Text
        draw.text((170, cy + 20), title, font=get_font(26, "bold"), fill=TEXT_MAIN)
        draw.text((170, cy + 56), desc, font=get_font(22, "regular"), fill=TEXT_MUTED)
        cy += 114
        
    img.save(f"{OUTPUT_DIR}/card_06.png")

# ==================== SLIDE 7 (OUTRO & APP PROMOTION) ====================
def draw_slide_7():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (15, 23, 42)) # Deep Navy Background
    draw = ImageDraw.Draw(img)
    
    # Top accent line
    draw.rectangle([(0, 0), (WIDTH, 14)], fill=PRIMARY_BLUE)
    
    # Badge
    tag_font = get_font(26, "bold")
    draw.rounded_rectangle([(70, 70), (280, 124)], radius=27, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((95, 82), "매장 관리 솔루션", font=tag_font, fill=(96, 165, 250))
    
    # Page Indicator
    page_font = get_font(26, "bold")
    draw.text((WIDTH - 150, 82), "07 / 07", font=page_font, fill=(148, 163, 184))
    
    # Headline
    h1_font = get_font(52, "bold")
    draw.text((70, 170), "소중한 직원을 지키는 것이", font=h1_font, fill=(255, 255, 255))
    draw.text((70, 240), "안전한 매장을 만드는 시작입니다.", font=h1_font, fill=(96, 165, 250))
    
    # Info Card
    box_top = 340
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 450)], radius=24, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    c_title = get_font(32, "bold")
    draw.text((110, box_top + 40), "📌 사건 발생 당시, 누가 근무 중이었을까요?", font=c_title, fill=(255, 255, 255))
    
    c_desc = get_font(26, "regular")
    lines = [
        "고객과의 분쟁이나 사건 발생 시,",
        "정확한 사실관계 파악을 위해 당시 근무자와",
        "근무시간을 입증할 수 있는 출퇴근 기록이 매우 중요합니다."
    ]
    ly = box_top + 100
    for l in lines:
        draw.text((110, ly), l, font=c_desc, fill=(203, 213, 225))
        ly += 38
        
    # App Highlight Box
    app_top = box_top + 240
    draw.rounded_rectangle([(110, app_top), (WIDTH - 110, app_top + 170)], radius=18, fill=(15, 23, 42), outline=(59, 130, 246), width=2)
    
    draw.text((140, app_top + 28), "📱 직원별 근무일정 & 출퇴근기록 관리", font=get_font(28, "bold"), fill=(255, 255, 255))
    draw.text((140, app_top + 72), "‘알바급여정석’으로 간편하게 관리하세요!", font=get_font(25, "medium"), fill=(148, 163, 184))
    draw.text((140, app_top + 115), "👉 https://app.albapay.co.kr", font=get_font(25, "bold"), fill=(96, 165, 250))
    
    # Save & Share prompt
    f_font = get_font(26, "bold")
    draw.text((70, 840), "💡 나중에 다시 보려면 지금 [저장] & [공유] 해두세요!", font=f_font, fill=(248, 250, 252))
    
    # Footer
    draw.text((70, HEIGHT - 70), "Google Play & App Store에서 '알바급여정석'을 검색해보세요.", font=get_font(23, "regular"), fill=(148, 163, 184))
    
    img.save(f"{OUTPUT_DIR}/card_07.png")

if __name__ == "__main__":
    print("Generating cards...")
    draw_slide_1()
    draw_slide_2()
    draw_slide_3()
    draw_slide_4()
    draw_slide_5()
    draw_slide_6()
    draw_slide_7()
    print("All 7 cards successfully generated!")
