import imgkit
import os

# ระบุโฟลเดอร์ที่มีไฟล์ HTML ที่ต้องการแปลง
input_folder = 'plots TLR10'  # เปลี่ยนเป็นโฟลเดอร์ที่คุณใช้

# ระบุโฟลเดอร์ที่จะบันทึกไฟล์ PNG
output_folder = 'output_folder'  # เปลี่ยนเป็นโฟลเดอร์ที่คุณต้องการ

# ตรวจสอบว่าโฟลเดอร์ปลายทางมีอยู่หรือไม่ และสร้างหากไม่มี
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ลูปผ่านไฟล์ HTML ในโฟลเดอร์ input_folder
for filename in os.listdir(input_folder):
    if filename.endswith('.html'):
        html_file = os.path.join(input_folder, filename)
        png_file = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.png')

        # กำหนดตัวเลือกสำหรับการแปลง
        options = {
            'format': 'png',
            'width': 1024,
            'height': 768,
        }

        # ทำการแปลง HTML เป็น PNG
        imgkit.from_file(html_file, png_file, options=options)

        print(f'ไฟล์ PNG ได้ถูกสร้างที่: {png_file}')
