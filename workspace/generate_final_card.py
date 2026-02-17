from PIL import Image, ImageDraw, ImageFont
import os

def create_sophisticated_card():
    # 1. Canvas Settings (High Quality Portrait)
    width, height = 1200, 1800
    bg_color = (248, 245, 240)  # Premium paper ivory
    card = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(card)

    # 2. Paths & Fonts
    font_path = "/home/lfant/.openclaw/workspace/fonts/NanumGothic.ttf"
    
    try:
        title_font = ImageFont.truetype(font_path, 50)
        body_font = ImageFont.truetype(font_path, 32)
        sig_font = ImageFont.truetype(font_path, 38)
        footer_font = ImageFont.truetype(font_path, 24)
    except Exception as e:
        print(f"Font error: {e}")
        title_font = body_font = sig_font = footer_font = ImageFont.load_default()

    # 3. Artistic Elements - The "Eternal Horizon"
    # Subtle Mountain Range (Minimalist triangles)
    draw.polygon([(0, 1800), (300, 1500), (600, 1800)], fill=(235, 235, 235))
    draw.polygon([(400, 1800), (800, 1400), (1200, 1800)], fill=(230, 230, 230))
    
    # Crimson Sun (Rising, slightly offset for dynamic balance)
    draw.ellipse([700, 150, 950, 400], fill=(214, 48, 49, 180)) # Deep Red

    # 4. Text Content (The corrected version)
    title = "조승환 부장님, 여승주 부장님!!"
    lines = [
        "2026년 병오년 새해 복 많이 받으십시오.",
        "새해에는 하시는 일 모두 건승하시길 진심으로 기원합니다.",
        "",
        "건강과 가족이 무엇보다도 제일 중요하니,",
        "항상 건강하시고 가정에 화목이 깃들길 기원합니다.",
        "",
        "조만간 다시 다 같이 일할 수 있는 기회가 생기면 좋겠습니다!"
    ]
    signature = "박찬주 배상"

    # Draw Title (Center Aligned)
    title_w = draw.textlength(title, font=title_font)
    draw.text(((width-title_w)/2, 600), title, fill=(45, 52, 54), font=title_font)

    # Draw Body (Refined Spacing)
    y_cursor = 780
    for line in lines:
        if line:
            line_w = draw.textlength(line, font=body_font)
            draw.text(((width-line_w)/2, y_cursor), line, fill=(45, 52, 54), font=body_font)
        y_cursor += 75

    # Draw Signature
    sig_w = draw.textlength(signature, font=sig_font)
    draw.text(((width-sig_w)/2, 1350), signature, fill=(45, 52, 54), font=sig_font)

    # 5. Corporate Logos (Clinical, precise layout at bottom)
    logos = ["CSWind", "Microsoft", "aws", "Azure", "Gemini"]
    total_logo_width = 1000
    start_x = (width - total_logo_width) / 2
    for i, logo in enumerate(logos):
        lx = start_x + (i * 210)
        draw.text((lx, 1600), logo, fill=(99, 110, 114), font=footer_font)

    # 6. Save Final Masterpiece
    output_path = "/home/lfant/.openclaw/workspace/final_new_year_card.png"
    card.save(output_path)
    return output_path

path = create_sophisticated_card()
print(f"Masterpiece saved to {path}")
