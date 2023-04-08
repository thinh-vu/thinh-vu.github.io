---
title : Thiết lập Digital Garden với Jekyll và Github Page
feed: show
date : 08-04-2023
---
- 🗓 2023-04-08 21:45
- Tags: #tutorial #note-taking
___

Mình đã nghe nói tới việc thiết lập một static site với Github Page và Jekyll nhưng lần nọ loay hoay thử không thành công nên đành tạm bỏ ngang không đụng tới nữa. Cho tới hôm nay xem lại bài viết từng đăng trên Blog về các ứng dụng ghi chú và rồi lại lần mò tìm tới keyword "Digital Garden" thì tìm thấy một nguồn tham khảo khá thú vị và hữu ích với chủ đề [Digital Gardener](https://github.com/MaggieAppleton/digital-gardeners). Bắt tay vào làm thử và thành công ngoài mong đợi vì thực chất các khâu thực hiện không hề phức tạp. Kể ra phần tốn thời gian nhất chính là cài đặt Jekyll, đã thực hiện lần trước.

# Đồ chơi cần thiết
| Tên | Tham chiếu | Mô tả|
| --- | --- | --- |
|Cài đặt Jekyll | https://jekyllrb.com/docs/installation/ | Cài đặt Jekyll phù hợp cho máy tính của bạn. Ở đây mình dùng macOS|
| Jekyll Garden | https://github.com/Jekyll-Garden/jekyll-garden.github.io | Github repo dùng để copy cấu hình cho Digital Garden sử dụng Jekyll theme. Xem phần [How to](https://jekyll-garden.github.io/post/how-to) |
| Github Desktop | https://desktop.github.com/ | Sử dụng để đồng bộ dữ liệu qua lại giữa Github và máy tính cho repo dùng làm Digital Garden |
| Visual Studio Code | https://code.visualstudio.com/download | Cài đặt code editor cơ bản để chỉnh sửa các file trong repo cho thuận tiện |
| Obsidian | https://obsidian.md/ | Cài đặt Obsidian làm ứng dụng ghi chú |

# Thiết lập
## Thiết lập cơ bản
- Xem kỹ phần hướng dẫn nhắc đến ở mục Jekyll Garden
- Có thể xem cách thiết lập của repo từ template hoặc chính repo của github site này tại https://github.com/thinh-vu/thinh-vu.github.io
# Tuỳ chỉnh
### Cấu hình chung
Các thiết lập chung có thể được tuỳ chỉnh trong file `_config.yml`, trong đó có 1 số mục cần quan tâm:
- Mô tả trang & copyright
  ![[../src/Pasted image 20230408220627.png]]

![[../src/Pasted image 20230408220523.png]]
### Thanh menu
Tìm và chỉnh sửa file `Nav.html`, có thể xoá các menu không phù hợp hoặc bổ sung theo ý
![[../src/Pasted image 20230408220418.png]]
# Cài đặt tracking
- Sử dụng Google Tag Manager là công cụ duy nhất để quản lý các công cụ theo dõi hiệu năng website. Mặc định theme Jekyll-Garden không có thẻ `<head></head>` và `<body></body>` nên cần thêm vào để có thể đặt mã theo dõi của GTM theo yêu cầu.
  ![](../src/Pasted%20image%2020230408230543.png)
- Cài đặt Google Analytics vào GTM để theo dõi các thông tin cơ bản về lưu lượng truy cập
# Lưu ý khi sử dụng
Định dạng markdown được hỗ trợ bởi Jekyll sẽ có một số điểm khác biệt so với tuỳ chọn mặc định của Obsidian. Vì vậy, điều quan trọng là nắm được những khác biệt này và thiết lập cấu hình Obsidian để phù hợp với định dạng được hỗ trợ. Cần lưu ý một số điểm sau:
- Sử dụng `Relative path to file` để đảm bảo hình và file đính kèm có thể hiển thị đúng
- Tắt chế độ `Use [[Wikilinks]]` mặc định để đảm bảo file đính kèm sẽ được sử dụng Relative file path
- Table của Jekyll cần sử dụng `|` ở cả đầu và cuối

