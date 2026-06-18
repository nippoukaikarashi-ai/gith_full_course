import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# 1. 新規ワークブックの作成
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "業務利益管理表"

# 2. データの定義（本来は外部ファイルやデータベースから読み込みます）
data = [
    ["項目", "金額（円）"],
    ["売上高", 1500000],
    ["売上原価", 600000],
    ["（売上総利益）", "=B2-B3"],  # Excelの数式をそのまま挿入可能
    ["販売費・一般管理費", 500000],
    ["業務利益（営業利益）", "=B4-B5"]
]

# 3. データの書き込み
for row in data:
    ws.append(row)

# 4. 見栄えの装飾（自動化の強み）
# ヘッダーの設定
header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
header_font = Font(name="Meiryo UI", size=11, bold=True, color="FFFFFF")
for cell in ws[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center")

# 利益行（計算結果）の強調
highlight_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
bold_font = Font(name="Meiryo UI", size=11, bold=True)
thin_border = Border(bottom=Side(style='thin'), top=Side(style='thin'))
double_border = Border(bottom=Side(style='double'), top=Side(style='thin'))

ws["A4"].font = bold_font; ws["B4"].font = bold_font; ws["A4"].fill = highlight_fill; ws["B4"].fill = highlight_fill
ws["A6"].font = bold_font; ws["B6"].font = bold_font; ws["A6"].border = double_border; ws["B6"].border = double_border

# 数値フォーマットの適用（カンマ区切り）
for row in range(2, 7):
    ws[f"B{row}"].number_format = '#,##0'

# 5. 保存
wb.save("業務利益管理表_自動生成.xlsx")
print("Excelファイルが生成されました。")

