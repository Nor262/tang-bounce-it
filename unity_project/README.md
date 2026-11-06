# HƯỚNG DẪN MỞ & CHẠY DỰ ÁN TRÊN UNITY EDITOR 🎮

Dự án này được thiết kế theo chuẩn **Unity 2D (khuyên dùng Unity 2022.3 LTS hoặc Unity 6)**. Toàn bộ mã nguồn, cấu hình Tags/Layers và tài nguyên đồ họa mẫu đã được tạo sẵn.

---

## 1. Cách Mở Dự Án Bằng Unity Hub

1. Mở **Unity Hub** trên máy tính của bạn.
2. Bấm nút **Add** (Thêm dự án từ đĩa) $\rightarrow$ Chọn thư mục:
   ```
   TUẦN LỄ GAME HÀN QUỐC 2026/unity_project
   ```
3. Chọn phiên bản Unity (bất kỳ bản Unity 2022.3 LTS hoặc Unity 2023 / Unity 6 đều tương thích 100%).
4. Bấm vào tên dự án để mở Unity Editor.

---

## 2. Thiết Lập Scene Nhanh Trong 3 Phút

### Bước 1: Cấu hình Camera
* Chọn `Main Camera`:
  * **Projection:** `Orthographic`
  * **Size:** `5.0`
  * **Background:** Chọn màu xanh tím hoàng hôn (`#1A1A24`).

### Bước 2: Tạo Mặt Sân (Ground)
* Tạo 1 GameObject 2D: Đặt tên là `Ground`.
* Kéo Sprite `Assets/Sprites/Ground_Courtyard.png` vào `SpriteRenderer`.
* Đặt vị trí: $X = 0, Y = -4.2, Z = 0$.
* Thêm component `BoxCollider2D`.
* Đặt **Tag:** `Ground` (Tag này đã được khai báo sẵn trong `TagManager.asset`).

### Bước 3: Tạo Nhân Vật (Player)
* Tạo 1 GameObject: Đặt tên là `Player`.
* Đặt vị trí: $X = -0.5, Y = -2.8, Z = 0$.
* Thêm `SpriteRenderer`: Kéo `Assets/Sprites/Player_Nam.png` (hoặc `Player_Jiho.png`).
* Thêm script: `JegiPlayerController.cs`.
* Tạo một GameObject con dưới Player tên là `FootKickPoint`: Đặt vị trí $X = 0.5, Y = -0.8$ rồi kéo vào ô `FootKickTransform` trên Inspector.

### Bước 4: Tạo Quả Cầu (Shuttlecock)
* Tạo 1 GameObject: Đặt tên là `Shuttlecock`.
* Đặt vị trí: $X = 0, Y = 1.8, Z = 0$.
* Thêm `SpriteRenderer`: Kéo `Assets/Sprites/Shuttlecock_Jegi.png`.
* Thêm `Rigidbody2D`:
  * **Mass:** `1.0`
  * **Gravity Scale:** `2.4`
  * **Collision Detection:** `Continuous`
* Thêm `CircleCollider2D` (vừa khít phần đế đồng xu).
* Thêm `TrailRenderer` (để tạo vệt lụa bay theo sau).
* Thêm script: `JegiShuttlecock.cs`.

### Bước 5: Tạo GameManager & UI
* Tạo 1 GameObject rỗng đặt tên là `GameManager`.
* Gắn script `JegiGameManager.cs`, `JegiUIManager.cs`, `JegiAudioManager.cs`.
* Kéo tham chiếu `Player` và `Shuttlecock` vào các trường tương ứng trên Inspector.

---

## 3. Chạy Thử & Xuất Bản Build (Android APK)

* **Chạy thử trên máy tính:** Bấm nút **Play (▶️)** ở đỉnh Unity Editor $\rightarrow$ Bấm chuột trái hoặc phím **Space** để tâng cầu.
* **Build ra file APK:**
  1. Vào menu `File` $\rightarrow$ `Build Settings...`.
  2. Chọn nền tảng **Android** $\rightarrow$ Bấm **Switch Platform**.
  3. Bấm **Build** $\rightarrow$ Chọn nơi lưu file `Tang_Bounce_It.apk`.
