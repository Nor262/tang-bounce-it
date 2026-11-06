# TÂNG! (BOUNCE IT!) — JEGI-CẦU ODYSSEY 🪶🏆

> **Dự Án Tham Gia Cuộc Thi:** Lập trình game Tuần lễ Game Hàn Quốc 2026 (**Korea Game Week 2026 – KGW2026**)  
> **Đơn vị tổ chức & bảo trợ:** Trung tâm Văn hóa Hàn Quốc tại Việt Nam (KCC), KOCCA, Đại sứ quán Hàn Quốc  
> **Chủ đề:** Giao thoa văn hóa truyền thống và hiện đại giữa hai quốc gia Việt Nam – Hàn Quốc  
> **Thể loại:** Hyper-casual / Precision 2D Physics & Rhythm Timing (1-Tap Rage-bait)  
> **Nền tảng:** Android (`.apk`), Web HTML5, Unity Engine (C#)

---

## 📖 1. Giới Thiệu & Điểm Chạm Văn Hóa Việt – Hàn

**Tâng! (Bounce It!)** là tựa game di động tái hiện trọn vẹn nét đẹp văn hóa dân gian của hai dân tộc: trò chơi **Đá Cầu** (Việt Nam) và **Jegichagi (제기차기)** (Hàn Quốc) vốn quen thuộc trong mỗi dịp Tết Nguyên Đán, Tết Trung Thu, Seollal và Chuseok.

* **Khí động học quả cầu:** Cả hai quốc gia đều có cách chế tác quả cầu độc đáo: phần đế nặng bằng đồng xu kim loại bọc vải để hạ thấp trọng tâm, phần thân trên là 20 sợi dây nilon dài 20cm xé nhỏ (hoặc lông chim) để tạo lực cản không khí giúp quả cầu luôn rơi thẳng đứng.
* **Cơ chế 5 cấp độ di sản:** Game mô phỏng thử thách vượt 5 cấp độ kỹ thuật chân truyền thống của Jegichagi, đưa người chơi qua 5 danh lam thắng cảnh biểu tượng:
  1. **Cấp 1 (0 – 15 điểm):** Sân Đình Làng Bắc Bộ (Gió lặng, nắng ấm).
  2. **Cấp 2 (16 – 35 điểm):** Phố Cổ Hội An Đêm Đèn Lồng (Gió nhẹ ven sông Hoài).
  3. **Cấp 3 (36 – 60 điểm):** Giao Lộ Biển Đảo Hạ Long & Jeju (Gió biển đổi chiều ngẫu nhiên).
  4. **Cấp 4 (61 – 90 điểm):** Làng Cổ Bukchon Hanok Mùa Thu (Lá ngân hạnh vàng rơi cản tầm nhìn).
  5. **Cấp 5 (Trên 90 điểm):** Hoàng Cung Gyeongbokgung Đêm Tuyết (Tuyết rơi dày, trơn trượt quán tính).

---

## 🎮 2. Lối Chơi Cốt Lõi (Core Gameplay)

* **Điều khiển 1 chạm (One-Tap Control):** Chạm vào màn hình điện thoại (hoặc nhấn phím **Space / Chuột trái** trên PC) khi quả cầu rơi xuống ngang tầm mắt cá chân của nhân vật.
* **Quy tắc thời điểm:**
  * Đá quá sớm: Nhân vật vung chân vào không khí (Whiff) $\rightarrow$ Cầu rơi chạm đất $\rightarrow$ **THUA**.
  * Đá quá trễ: Quả cầu chạm mặt sân $\rightarrow$ **THUA NGAY**.
  * Đá chuẩn xác: Quả cầu nảy bốc lên cao theo vector góc chạm $\Delta x = x_{\text{jegi}} - x_{\text{input}}$.
* **3 Phân bậc chấm điểm:**
  * **PERFECT:** Chạm đúng tâm mắt cá chân, nổ hạt sáng vàng kim, $+3$ điểm và tích lũy Fever.
  * **GREAT:** Chạm hơi lệch, nhân vật bước dịch chân đỡ cầu, $+2$ điểm.
  * **GRAZE (Cứu cầu sát đất):** Nhân vật xoạc chân cứu bóng ngoạn mục, $+1$ điểm.
* **Fever Mode:** Đạt chuỗi Combo liên tiếp sẽ kích hoạt chế độ nhân đôi điểm số x2!

---

## 📂 3. Cấu Trúc Mã Nguồn & Dự Án

```
├── Tang_Bounce_It.apk                 <-- File cài đặt trực tiếp trên điện thoại Android
├── Du_Thi_Game_KGW2026_Tang_Bounce_It.pptx <-- File Slide thuyết trình 11 trang chuẩn BTC
├── README.md                          <-- Tài liệu dự án
│
├── web_game/                          <-- Bản game chơi trực tiếp trên Web / Trình duyệt
│   └── index.html
│
├── unity_project/                     <-- Mã nguồn dự án Unity Engine (C#)
│   └── Assets/
│       └── Scripts/
│           ├── JegiGameManager.cs     (Vòng lặp game, tính điểm, gió mùa, 5 cấp độ)
│           ├── JegiShuttlecock.cs     (Vật lý 2D, lực cản khí động học, vector nảy)
│           ├── JegiPlayerController.cs (Điều khiển 1 chạm, chân so le, biểu cảm Chibi)
│           ├── JegiSkinData.cs        (ScriptableObject 5 loại cầu di sản)
│           ├── JegiUIManager.cs       (Giao diện nút bấm giấy Ddakji 3D, HUD điểm)
│           └── JegiAudioManager.cs    (Âm thanh đá keng, tiếng cồng chiêng, tiếng gió)
│
├── android_project/                   <-- Mã nguồn dự án Native Android
│   ├── AndroidManifest.xml
│   ├── src/com/kgw2026/tangbounceit/MainActivity.java
│   └── res/
│
└── docs/                              <-- Tài liệu thiết kế Game & Hồ sơ dự thi
    ├── GAME_DESIGN_DOCUMENT.md        (Bản Game Design Document hoàn chỉnh)
    └── Du_Thi_Game_KGW2026_Tang_Bounce_It.pptx
```

---

## 🚀 4. Hướng Dẫn Cài Đặt & Trải Nghiệm

### Cách 1: Cài đặt tệp `.apk` trên điện thoại Android
1. Chuyển tệp `Tang_Bounce_It.apk` sang điện thoại Android của bạn (qua cáp USB, Zalo, Google Drive hoặc `adb install Tang_Bounce_It.apk`).
2. Mở tệp `.apk` trên điện thoại và chọn **Cài đặt (Install)**.
3. Mở game và bắt đầu tâng cầu với 60 FPS mượt mà!

### Cách 2: Chơi trực tiếp trên Trình duyệt Máy tính
1. Mở tệp `web_game/index.html` bằng bất kỳ trình duyệt nào (Chrome, Firefox, Edge, Brave).
2. Hoặc khởi chạy máy chủ cục bộ:
   ```bash
   python3 -m http.server 8080 --directory web_game
   ```
   Sau đó truy cập: `http://localhost:8080`.

### Cách 3: Nhập mã nguồn vào Unity Editor
1. Tạo một dự án **Unity 2D** mới (khuyên dùng phiên bản Unity 2022 LTS hoặc mới hơn).
2. Sao chép toàn bộ thư mục `unity_project/Assets/Scripts/` vào thư mục `Assets/Scripts/` của dự án Unity.
3. Gắn các Component vào GameObject và tận hưởng vòng lặp vật lý 2D mượt mà.

---

## 🏆 5. Hồ Sơ Nộp Bài Cuộc Thi KGW2026

* **Địa chỉ gửi email:** `btc.koreagameweek@gmail.com`
* **Tiêu đề email bắt buộc:** `[Dự thi Lập trình game KGW2026]`
* **Tệp đính kèm theo quy chế:**
  1. File PowerPoint ý tưởng: `Du_Thi_Game_KGW2026_Tang_Bounce_It.pptx` (đã chuẩn bị sẵn 11 slide).
  2. Bản cài đặt chạy thực tế: `Tang_Bounce_It.apk` (đã ký số và kiểm thử).
  3. Đường link mã nguồn dự án: `https://github.com/Nor262/tang-bounce-it`
  4. Video demo chơi thử (quay 30–60 giây từ điện thoại hoặc màn hình web).

---
*Chúc đội thi đạt giải cao nhất tại Tuần lễ Game Hàn Quốc 2026!*
