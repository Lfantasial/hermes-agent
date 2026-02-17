from PIL import Image, ImageDraw, ImageFont
import os

def create_card():
    # 1. Canvas Settings
    width, height = 1200, 1800
    bg_color = (249, 246, 242) # Soft cream
    card = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(card)

    # 2. Fonts
    font_path = "/home/lfant/.agents/skills/canvas-design/canvas-fonts/LibreBaskerville-Regular.ttf"
    # Using fallback fonts if specific ones fail
    try:
        title_font = ImageFont.truetype(font_path, 60)
        body_font = ImageFont.truetype(font_path, 36)
        signature_font = ImageFont.truetype(font_path, 42)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        signature_font = ImageFont.load_default()

    # 3. Sun (Top)
    draw.ellipse([450, 50, 750, 350], fill=(235, 77, 75)) # Red Sun

    # 4. Text Content (Corrected)
    title = "조승환 부장님, 여승주 부장님!!"
    body = [
        "2026년 병오년 새해 복 많이 받으시고",
        "새해에는 하시는 일 모두 건승하시길 기원합니다.",
        "",
        "건강과 가족이 무엇보다도 제일 중요하니",
        "항상 건강하시고 가정에 화목이 깃들길 기원합니다.",
        "",
        "조만간 다시 다 같이 일할 수 있는 기회가 생기면 좋겠네요!"
    ]
    signature = "박찬주 배상"

    # Draw Title
    # draw.textcenter is not in old PIL, calculate manually
    title_w = draw.textlength(title, font=title_font)
    draw.text(((width-title_w)/2, 500), title, fill=(30, 39, 46), font=title_font)

    # Draw Body
    y = 650
    for line in body:
        line_w = draw.textlength(line, font=body_font)
        draw.text(((width-line_w)/2, y), line, fill=(30, 39, 46), font=body_font)
        y += 70

    # Draw Signature
    sig_w = draw.textlength(signature, font=signature_font)
    draw.text(((width-sig_w)/2, 1300), signature, fill=(30, 39, 46), font=signature_font)

    # 5. Logos (Simulated)
    logos = ["CSWind", "Microsoft", "aws", "Azure", "Gemini"]
    lx = 100
    for logo in logos:
        draw.text((lx, 1550), logo, fill=(75, 75, 75), font=body_font)
        lx += 220

    # 6. Save
    output_path = "/home/lfant/.openclaw/workspace/new_year_card_2026.png"
    card.save(output_path)
    print(f"Saved to {output_path}")

create_card()
