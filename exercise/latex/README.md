# Hướng dẫn chạy LaTeX

Tài liệu này hướng dẫn build file [main.tex](main.tex) theo đúng cấu hình hiện tại trong VS Code.

## Cấu hình hiện tại

- Build chạy từ thư mục chứa file tex (tương đương cd %DIR%).
- Dùng latexmk tại đường dẫn tuyệt đối: /Library/TeX/texbin/latexmk.
- Output nằm trong thư mục [out](out/).

## Yêu cầu

- macOS
- Đã cài MacTeX hoặc BasicTeX
- Có lệnh sau trên máy:
  - /Library/TeX/texbin/latexmk
  - /Library/TeX/texbin/pdflatex
  - /Library/TeX/texbin/bibtex

## Cách chạy trong VS Code

1. Mở file [main.tex](main.tex).
2. Bấm Cmd + Option + B để build recipe latexmk (clean + pdf).
3. Mở PDF trong tab preview của LaTeX Workshop (nếu chưa tự mở).

## Chạy bằng Terminal (tương đương logic UI)

Tại thư mục [exercise/latex](.):

/Library/TeX/texbin/latexmk -C -outdir=out main.tex
/Library/TeX/texbin/latexmk -g -synctex=1 -interaction=nonstopmode -file-line-error -pdf -outdir=out main.tex

## File kết quả

- PDF chính: [out/main.pdf](out/main.pdf)
- Các file trung gian: thư mục [out](out/)

## Lỗi thường gặp

- Không tìm thấy latexmk:
  - Kiểm tra đường dẫn /Library/TeX/texbin/latexmk có tồn tại.
- Build từ sai thư mục:
  - Luôn chạy lệnh tại thư mục [exercise/latex](.) hoặc dùng cấu hình VS Code hiện tại.
- BibTeX/citation chưa cập nhật:
  - Chạy lại lệnh latexmk thêm 1 lần để đồng bộ tham chiếu.
