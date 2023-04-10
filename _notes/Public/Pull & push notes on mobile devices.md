---
title : Pull & push notes on mobile devices
feed: show
permalink: /tao-ghi-chu-dong-bo-voi-git-tren-dien-thoai
date : 10-04-2023
aliases: [Pull & push notes on mobile devices]
---

- 🗓 2023-04-10 06:03
- 🔗 [[Cẩm nang "làm vườn" 4.0]] [[Thiết lập Digital Garden với Jekyll và Github Page]]

- **Problem:** Khó tạo mới ghi chú và đưa lên Digital Garden (Git repo) từ điện thoại.
- **Framing**
	- Có thực sự cần ghi chú bằng điện thoại? Có, khi ý tưởng xuất hiện và mở máy tính không tiện
	- Có thực sự cần commit bằng điện thoại? Đôi khi, đa phần có thể commit sau bằng máy tính. Trong trường hợp này, muốn kiểm chứng khả năng thực hiện toàn bộ quá trình bằng điện thoại.
- **Challenges:** 
	- Ít ứng dụng cho phép làm việc với Git với đầy đủ tính năng trên điện thoại
	- VS Code có thể làm việc với Git nhưng không có ứng dụng chính thức trên điện thoại
	- Obsidian có plugin làm việc với Git nhưng bản mobile không hiệu quả
- **Solution:**
	- Cần làm hoàn toàn bằng điện thoại:
		- Sử dụng Folder Sync ^[folder-sync] để đồng bộ Git Repo về điện thoại, bảo gồm toàn bộ cài đặt Obsidian vault. Lần đầu thực hiện mất thời gian chờ vì repo có rất nhiều file, lên lịch đồng bộ 4h/lần tự động.  
		  [^folder-sync]: ![](/src/Screenshot_20230410_062554_FolderSync.jpg)
		- Soạn thảo ghi chú bằng Obsidian mobile ^[obsidian-mobile], trải nghiệm quen thuộc và đầy đủ tính năng. 
		  [^obsidian-mobile]: ![](/src/Screenshot_20230410_062402_Obsidian.jpg)
		- Mở Github repo bằng vscode.dev ^[vscode-dev] qua Chrome, tạo file mới. Copy/paste nội dung ghi chú từ Obsidian qua. Commit để đẩy nội dung mới lên. 
		  [^vscode-dev]: ![](/src/Screenshot_20230410_060109_Chrome.jpg)
	- Soạn thảo trên điện thoại, commit trên máy tính:
		- Soạn thảo bằng Obsidian, đồng bộ bằng Folder Sync
		- Khi mở máy tính thì commit lên Github. Điểm bất tiện là Onedrive mất thời gian kiểm tra file và đồng bộ khá lâu.



