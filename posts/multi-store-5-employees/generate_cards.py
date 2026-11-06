import os
from PIL import Image, ImageDraw, ImageFont

POST_DIR = "/Users/kimkyoungil/.gemini/antigravity/scratch/customer-response-cardnews/posts/multi-store-5-employees"
OUTPUT_DIR = os.path.join(POST_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

def get_font(size, weight="regular"):
    indices = {
        "regular": 0,
        "medium": 2,
        "semibold": 4,
        "bold": 6
    }
    idx = indices.get(weight, 0)
    return ImageFont.truetype(FONT_PATH, size=size, index=idx)

WIDTH, HEIGHT = 1080, 1080

# Palette
BG_COLOR = (248, 250, 252)        # Slate 50
TEXT_MAIN = (15, 23, 42)          # Slate 900
TEXT_MUTED = (100, 116, 139)      # Slate 500
PRIMARY_COLOR = (14, 116, 144)    # Cyan 700 / Teal
PRIMARY_LIGHT = (236, 254, 255)   # Cyan 50
PRIMARY_ACCENT = (6, 182, 212)    # Cyan 500
ACCENT_GREEN = (16, 185, 129)     # Emerald 500
ACCENT_RED = (239, 68, 68)        # Red 500
ACCENT_RED_LIGHT = (254, 242, 242)# Red 50
CARD_BG = (255, 255, 255)         # Pure White
BORDER_COLOR = (226, 232, 240)    # Slate 200

def create_base(slide_num, total_slides=7, tag="노무 상식 가이드"):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Top decorative bar
    draw.rectangle([(0, 0), (WIDTH, 12)], fill=PRIMARY_COLOR)
    
    # Header: Tag
    tag_font = get_font(24, "semibold")
    tag_w = draw.textlength(tag, font=tag_font)
    bx, by = 70, 60
    draw.rounded_rectangle([(bx, by), (bx + tag_w + 32, by + 44)], radius=22, fill=PRIMARY_LIGHT, outline=PRIMARY_COLOR, width=1)
    draw.text((bx + 16, by + 9), tag, font=tag_font, fill=PRIMARY_COLOR)
    
    # Slide Indicator
    page_font = get_font(26, "bold")
    page_text = f"{slide_num:02d} / {total_slides:02d}"
    page_w = draw.textlength(page_text, font=page_font)
    draw.text((WIDTH - 70 - page_w, 68), page_text, font=page_font, fill=TEXT_MUTED)
    
    # Bottom Footer
    footer_font = get_font(22, "medium")
    brand_text = "스마트한 매장 관리의 시작 ｜ 알바급여정석"
    draw.line([(70, HEIGHT - 80), (WIDTH - 70, HEIGHT - 80)], fill=BORDER_COLOR, width=1)
    draw.text((70, HEIGHT - 60), brand_text, font=footer_font, fill=TEXT_MUTED)
    
    web_text = "app.albapay.co.kr"
    web_w = draw.textlength(web_text, font=footer_font)
    draw.text((WIDTH - 70 - web_w, HEIGHT - 60), web_text, font=footer_font, fill=PRIMARY_COLOR)
    
    return img, draw

# ==================== SLIDE 1 (COVER) ====================
def draw_slide_1():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (15, 23, 42)) # Slate 900
    draw = ImageDraw.Draw(img)
    
    # Top accent line
    draw.rectangle([(0, 0), (WIDTH, 14)], fill=PRIMARY_ACCENT)
    
    # Tag Badge
    tag_font = get_font(26, "bold")
    draw.rounded_rectangle([(70, 70), (330, 124)], radius=27, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((95, 82), "복수 매장 사장님 필독", font=tag_font, fill=(56, 189, 248))
    
    # Page Indicator
    draw.text((WIDTH - 150, 82), "01 / 07", font=get_font(26, "bold"), fill=(148, 163, 184))
    
    # Question
    draw.text((70, 185), "“카페 2곳에 직원 각 3명씩 총 6명...”", font=get_font(38, "bold"), fill=(203, 213, 225))
    
    # Main Headline
    h1 = get_font(68, "bold")
    draw.text((70, 255), "매장 2곳 직원 총 6명,", font=h1, fill=(255, 255, 255))
    draw.text((70, 345), "상시 5인 이상일까?", font=h1, fill=(56, 189, 248))
    
    # Big Highlight Box
    box_top = 475
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 350)], radius=24, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    draw.text((110, box_top + 40), "❌ “직원 6명이니 당연히 5인 이상이다?”", font=get_font(32, "semibold"), fill=(252, 165, 165))
    draw.text((110, box_top + 95), "절대 그렇게 계산하시면 안 됩니다!", font=get_font(28, "medium"), fill=(226, 232, 240))
    
    draw.line([(110, box_top + 155), (WIDTH - 110, box_top + 155)], fill=(51, 65, 85), width=1)
    
    draw.text((110, box_top + 185), "🔍 사장님이 반드시 확인해야 할 2단계 기준", font=get_font(28, "bold"), fill=(96, 165, 250))
    draw.text((110, box_top + 235), "1단계: 두 매장이 법적으로 '하나의 사업'인가?", font=get_font(26, "regular"), fill=(203, 213, 225))
    draw.text((110, box_top + 280), "2단계: 날짜별 근로자 수와 '1/2 규정'을 충족하는가?", font=get_font(26, "regular"), fill=(203, 213, 225))
    
    # Footer
    draw.text((70, HEIGHT - 70), "알바급여정석 ｜ 복수 매장 사업장 구분 및 1/2 규정 총정리", font=get_font(24, "medium"), fill=(148, 163, 184))
    
    img.save(f"{OUTPUT_DIR}/card_01.png")

# ==================== SLIDE 2 (STEP 1: BUSINESS SCOPE) ====================
def draw_slide_2():
    img, draw = create_base(2, 7, "1단계: 사업장 구분")
    
    title_font = get_font(50, "bold")
    draw.text((70, 135), "두 매장이 장소는 다른데,", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 200), "하나의 사업장으로 합쳐질까?", font=title_font, fill=PRIMARY_COLOR)
    
    sub_font = get_font(25, "medium")
    draw.text((70, 270), "사업자등록증이 2개라고 무조건 독립된 사업장은 아닙니다!", font=sub_font, fill=TEXT_MUTED)
    
    # 5 Criteria Card
    box_top = 325
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 460)], radius=22, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    draw.text((105, box_top + 30), "📋 고용노동부 '사업장 독립성' 판단 기준 5가지", font=get_font(28, "bold"), fill=PRIMARY_COLOR)
    
    points = [
        ("1. 인사·근로조건 결정권", "직원 채용과 시급, 근무조건을 누가 일괄 결정하는가?"),
        ("2. 급여 및 근무표 관리", "급여 정산과 근무 일정을 본사/사장님이 통합 관리하는가?"),
        ("3. 회계 및 경영 독립성", "각 매장이 독자적인 예산과 회계 권한을 가지고 있는가?"),
        ("4. 직원들의 교차 근무(대타)", "필요 시 두 매장을 오가며 대타 근무를 시키는가?"),
        ("5. 지휘·감독 주체", "업무 지시와 승인이 하나의 조직 체계에서 이루어지는가?")
    ]
    
    py = box_top + 85
    for title, desc in points:
        draw.text((105, py), f"• {title}", font=get_font(25, "bold"), fill=TEXT_MAIN)
        draw.text((130, py + 34), desc, font=get_font(22, "regular"), fill=TEXT_MUTED)
        py += 72
        
    draw.text((70, 830), "💡 결론: 독립된 경영·인사권이 없다면 '하나의 사업'으로 합산 검토!", font=get_font(25, "bold"), fill=TEXT_MAIN)
    
    img.save(f"{OUTPUT_DIR}/card_02.png")

# ==================== SLIDE 3 (REGISTERED VS ACTUAL) ====================
def draw_slide_3():
    img, draw = create_base(3, 7, "2단계: 상시근로자 계산")
    
    title_font = get_font(50, "bold")
    draw.text((70, 135), "등록 직원이 총 6명이어도", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 200), "상시 5인 이상이 아닐 수 있습니다", font=title_font, fill=PRIMARY_COLOR)
    
    # Explain Box
    box_top = 285
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 230)], radius=20, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    draw.text((105, box_top + 30), "📌 상시근로자 수의 법적 정의 (근로기준법 시행령 제7조의2)", font=get_font(27, "bold"), fill=TEXT_MAIN)
    
    formula_y = box_top + 80
    draw.rounded_rectangle([(105, formula_y), (WIDTH - 105, formula_y + 65)], radius=12, fill=PRIMARY_LIGHT)
    draw.text((135, formula_y + 18), "상시근로자 수 = 산정기간 연인원(근무자 수 합계) ÷ 가동일수", font=get_font(26, "bold"), fill=PRIMARY_COLOR)
    
    draw.text((105, box_top + 165), "👉 단순히 명부에 등록된 인원이 아니라, '실제 일한 날짜별 인원' 기준!", font=get_font(24, "medium"), fill=TEXT_MAIN)
    
    # Supreme Court Callout
    sc_top = 545
    draw.rounded_rectangle([(70, sc_top), (WIDTH - 70, sc_top + 340)], radius=20, fill=(240, 253, 250), outline=(153, 246, 228), width=2)
    
    draw.text((105, sc_top + 35), "⚖️ 대법원 최신 판결 (2024.1.25 선고 2023다275998)", font=get_font(27, "bold"), fill=(13, 148, 136))
    
    lines = [
        "“근로의무가 없는 휴일에 실제 근무하지 않은 근로자는",
        " 일별 상시근로자 수 산정 인원에 포함하지 않는다.”",
        "",
        "• 주말이나 쉬는 날 출근하지 않은 직원은 그날의 인원에서 제외!",
        "• 따라서 명부상 6명이라도 평일 4명만 일한다면 인원수가 달라집니다."
    ]
    
    ly = sc_top + 95
    for l in lines:
        if "“" in l:
            draw.text((105, ly), l, font=get_font(25, "bold"), fill=TEXT_MAIN)
        else:
            draw.text((105, ly), l, font=get_font(23, "regular"), fill=TEXT_MAIN)
        ly += 36
        
    img.save(f"{OUTPUT_DIR}/card_03.png")

# ==================== SLIDE 4 (CASE A: 1/2 RULE EXCLUSION) ====================
def draw_slide_4():
    img, draw = create_base(4, 7, "충격의 1/2 규정")
    
    title_font = get_font(50, "bold")
    draw.text((70, 135), "사례 A. 평균 5.0명인데도", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 200), "5인 이상이 아닌 경우?!", font=title_font, fill=ACCENT_RED)
    
    sub_font = get_font(25, "medium")
    draw.text((70, 270), "근로기준법 시행령 제7조의2 제2항 '1/2 규정'을 꼭 보세요!", font=sub_font, fill=TEXT_MUTED)
    
    # Calc Box
    box_top = 320
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 260)], radius=20, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    draw.text((105, box_top + 30), "📊 1개월(가동일수 20일) 실제 근무 인원 예시", font=get_font(27, "bold"), fill=TEXT_MAIN)
    
    calcs = [
        "• 10일간: 평일 4명씩 근무 = 40명",
        "• 10일간: 주말 6명씩 근무 = 60명",
        "• 총 연인원: 100명 ÷ 20일 = 평균 5.0명 (5인 이상처럼 보임!)"
    ]
    cy = box_top + 80
    for c in calcs:
        draw.text((105, cy), c, font=get_font(24, "medium"), fill=TEXT_MAIN)
        cy += 38
        
    draw.line([(105, box_top + 205), (WIDTH - 105, box_top + 205)], fill=BORDER_COLOR, width=1)
    draw.text((105, box_top + 220), "👉 평균 계산만으로는 5.0명으로 법 적용 대상 같지만...", font=get_font(23, "semibold"), fill=PRIMARY_COLOR)
    
    # 1/2 Rule Explanation Box
    r_top = 610
    draw.rounded_rectangle([(70, r_top), (WIDTH - 70, r_top + 280)], radius=20, fill=ACCENT_RED_LIGHT, outline=(254, 202, 202), width=2)
    
    draw.text((105, r_top + 30), "🚨 [1/2 규정] 5인 미만인 날이 절반(1/2) 이상인가?", font=get_font(27, "bold"), fill=ACCENT_RED)
    
    r_lines = [
        "• 전체 20일 중 5명 미만(4명) 일한 날 = 10일 (정확히 50%)",
        "• 시행령: '기준에 미달한 날이 가동일수의 절반 이상이면",
        "  평균이 5명이어도 법 적용 사업장으로 보지 않는다!'",
        "",
        "결론: 사례 A는 5인 이상 사업장이 아닙니다!"
    ]
    ry = r_top + 80
    for l in r_lines:
        if "결론:" in l:
            draw.text((105, ry), l, font=get_font(26, "bold"), fill=ACCENT_RED)
        else:
            draw.text((105, ry), l, font=get_font(23, "regular"), fill=TEXT_MAIN)
        ry += 36
        
    img.save(f"{OUTPUT_DIR}/card_04.png")

# ==================== SLIDE 5 (CASE B: 5-PERSON INCLUDED) ====================
def draw_slide_5():
    img, draw = create_base(5, 7, "사례 비교")
    
    title_font = get_font(50, "bold")
    draw.text((70, 135), "사례 B. 같은 직원 6명인데,", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 200), "5인 이상으로 인정되는 경우!", font=title_font, fill=ACCENT_GREEN)
    
    sub_font = get_font(25, "medium")
    draw.text((70, 270), "근무일정(스케줄) 비율만 달라져도 결론이 180도 바뀝니다.", font=sub_font, fill=TEXT_MUTED)
    
    # Calc Box
    box_top = 320
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 260)], radius=20, fill=CARD_BG, outline=BORDER_COLOR, width=2)
    
    draw.text((105, box_top + 30), "📊 근무 일정이 조금 변경된 예시", font=get_font(27, "bold"), fill=TEXT_MAIN)
    
    calcs = [
        "•  8일간: 평일 4명씩 근무 = 32명",
        "• 12일간: 주말/성수기 6명씩 근무 = 72명",
        "• 총 연인원: 104명 ÷ 20일 = 평균 5.2명"
    ]
    cy = box_top + 80
    for c in calcs:
        draw.text((105, cy), c, font=get_font(24, "medium"), fill=TEXT_MAIN)
        cy += 38
        
    draw.line([(105, box_top + 205), (WIDTH - 105, box_top + 205)], fill=BORDER_COLOR, width=1)
    draw.text((105, box_top + 220), "👉 5명 미만인 날(8일)이 전체 20일의 절반(10일)보다 적음!", font=get_font(23, "semibold"), fill=PRIMARY_COLOR)
    
    # Success Box
    s_top = 610
    draw.rounded_rectangle([(70, s_top), (WIDTH - 70, s_top + 280)], radius=20, fill=(240, 253, 244), outline=(187, 247, 208), width=2)
    
    draw.text((105, s_top + 30), "✅ [1/2 규정 충족] 상시 5인 이상 사업장 해당!", font=get_font(27, "bold"), fill=ACCENT_GREEN)
    
    s_lines = [
        "• 평균도 5.2명으로 5명 이상이고,",
        "• 5인 미만 근무일(8일)이 전체 가동일의 절반 미만!",
        "",
        "결론: 같은 직원 6명이어도 일정 배치에 따라",
        "      상시 5인 이상 사업장으로 최종 판정됩니다!"
    ]
    sy = s_top + 80
    for l in s_lines:
        if "결론:" in l:
            draw.text((105, sy), l, font=get_font(25, "bold"), fill=TEXT_MAIN)
        else:
            draw.text((105, sy), l, font=get_font(23, "regular"), fill=TEXT_MAIN)
        sy += 36
        
    img.save(f"{OUTPUT_DIR}/card_05.png")

# ==================== SLIDE 6 (PAYROLL IMPACT) ====================
def draw_slide_6():
    img, draw = create_base(6, 7, "급여와 근로조건")
    
    title_font = get_font(50, "bold")
    draw.text((70, 135), "상시 5인 이상 여부,", font=title_font, fill=TEXT_MAIN)
    draw.text((70, 200), "왜 급여 계산에서 치명적일까요?", font=title_font, fill=PRIMARY_COLOR)
    
    sub_font = get_font(25, "medium")
    draw.text((70, 270), "5인 이상이 되는 순간 사업주가 부담해야 할 법적 의무가 커집니다.", font=sub_font, fill=TEXT_MUTED)
    
    cards = [
        ("⏰ 연장·야간·휴일근로 가산수당 (1.5배)", "통상시급의 50%를 추가 지급해야 합니다. (근로기준법 제56조)\n5인 미만 사업장은 법정 가산수당 규정이 적용되지 않습니다.", (254, 242, 242), ACCENT_RED),
        ("🏖️ 연차유급휴가 규정 적용", "1년간 80% 이상 출근 시 15일의 유급휴가 발생 의무 적용.\n(5인 미만 사업장은 연차휴가 법적 의무 없음)", PRIMARY_LIGHT, PRIMARY_COLOR),
        ("🔄 매월 산정 결과가 바뀔 수 있음!", "원칙적으로 법 적용 사유 발생일 전 1개월 기준으로 산정하므로\n직원 입·퇴사나 스케줄 변경 시 매월 재검토가 필요합니다.", CARD_BG, TEXT_MAIN)
    ]
    
    cy = 325
    for title, desc, bg, accent in cards:
        draw.rounded_rectangle([(70, cy), (WIDTH - 70, cy + 155)], radius=18, fill=bg, outline=BORDER_COLOR, width=2)
        draw.text((105, cy + 25), title, font=get_font(26, "bold"), fill=accent)
        draw.text((105, cy + 75), desc, font=get_font(22, "regular"), fill=TEXT_MAIN, spacing=6)
        cy += 175
        
    img.save(f"{OUTPUT_DIR}/card_06.png")

# ==================== SLIDE 7 (OUTRO & APP) ====================
def draw_slide_7():
    img = Image.new("RGBA", (WIDTH, HEIGHT), (15, 23, 42)) # Slate 900
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([(0, 0), (WIDTH, 14)], fill=PRIMARY_ACCENT)
    
    # Tag
    draw.rounded_rectangle([(70, 70), (310, 124)], radius=27, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((95, 82), "노무 리스크 예방", font=get_font(26, "bold"), fill=(56, 189, 248))
    
    draw.text((WIDTH - 150, 82), "07 / 07", font=get_font(26, "bold"), fill=(148, 163, 184))
    
    # Title
    draw.text((70, 165), "정확한 날짜별 근무기록이", font=get_font(52, "bold"), fill=(255, 255, 255))
    draw.text((70, 235), "노무 분쟁을 막는 핵심입니다.", font=get_font(52, "bold"), fill=(56, 189, 248))
    
    # Summary Box
    box_top = 330
    draw.rounded_rectangle([(70, box_top), (WIDTH - 70, box_top + 460)], radius=24, fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    
    draw.text((110, box_top + 35), "📌 복수 매장 사장님 핵심 체크 3가지", font=get_font(30, "bold"), fill=(255, 255, 255))
    
    checks = [
        "1. 사업장 독립성 점검 (인사·노무·경영이 분리되어 있는가?)",
        "2. 날짜별 실제 사용 근로자 수 기록 (단순 등록 직원 수 X)",
        "3. 시행령 1/2 규정 확인 (미달 일수가 가동일수 절반 이상인가?)"
    ]
    cy = box_top + 95
    for c in checks:
        draw.text((110, cy), c, font=get_font(24, "regular"), fill=(203, 213, 225))
        cy += 40
        
    # App Box
    app_top = box_top + 245
    draw.rounded_rectangle([(110, app_top), (WIDTH - 110, app_top + 175)], radius=18, fill=(15, 23, 42), outline=(6, 182, 212), width=2)
    
    draw.text((140, app_top + 28), "📱 직원별 근무표 & 출퇴근 근태 관리", font=get_font(28, "bold"), fill=(255, 255, 255))
    draw.text((140, app_top + 72), "‘알바급여정석’으로 투명하고 간편하게 관리하세요!", font=get_font(24, "medium"), fill=(148, 163, 184))
    draw.text((140, app_top + 118), "👉 https://app.albapay.co.kr", font=get_font(25, "bold"), fill=(56, 189, 248))
    
    draw.text((70, 840), "💡 주변 다점포 사장님들께도 [공유] & [저장] 해주세요!", font=get_font(26, "bold"), fill=(248, 250, 252))
    draw.text((70, HEIGHT - 70), "Google Play & App Store에서 '알바급여정석'을 만나보세요.", font=get_font(23, "regular"), fill=(148, 163, 184))
    
    img.save(f"{OUTPUT_DIR}/card_07.png")

if __name__ == "__main__":
    print("Generating cards for post 2...")
    draw_slide_1()
    draw_slide_2()
    draw_slide_3()
    draw_slide_4()
    draw_slide_5()
    draw_slide_6()
    draw_slide_7()
    print("All 7 cards successfully generated!")
