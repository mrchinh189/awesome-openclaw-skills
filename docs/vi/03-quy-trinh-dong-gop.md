# Quy trình đóng góp end-to-end

> Tài liệu này mô tả flow đầy đủ giữa **contributor** và **maintainer**, kèm tiêu chí ra quyết định ở từng bước.

---

## 1. Sơ đồ swimlane tổng quát

```mermaid
flowchart TB
    subgraph C[" Contributor "]
        c1[Phát hiện skill thiếu] --> c2[Verify trên openclaw/skills]
        c2 --> c3[Fork + branch]
        c3 --> c4[Sửa README.md]
        c4 --> c5[Push + Mở PR]
        c5 -.- c8[Phản hồi review]
        c8 --> c9[Push commit mới]
    end

    subgraph M[" Maintainer "]
        m1[Nhận thông báo PR] --> m2{Đạt 7 tiêu chí?}
        m2 -- Không --> m3[Request changes<br/>+ comment cụ thể]
        m3 -.- c8
        m2 -- Có --> m4[Approve + Merge]
        m4 --> m5[Đóng PR / cảm ơn]
    end

    c5 --> m1
    c9 --> m1

    style m2 fill:#fde68a,stroke:#92400e
    style m4 fill:#86efac,stroke:#15803d
    style m3 fill:#fca5a5,stroke:#991b1b
```

---

## 2. 7 tiêu chí maintainer dùng để duyệt PR

| # | Tiêu chí | Cách kiểm | Hành động nếu fail |
|---|---|---|---|
| 1 | Link `SKILL.md` trả 200 | Click thử hoặc `curl -I` | Request changes + chỉ đúng link |
| 2 | Slug trùng folder trong openclaw/skills | Visual compare | Request changes |
| 3 | Đúng category | Đối chiếu mô tả ↔ bảng category | Đề xuất category khác |
| 4 | Mô tả ≤ 10 từ, không quảng cáo | Đếm từ | Request rút gọn |
| 5 | Không trùng entry đã có | `grep -F "/<slug>/SKILL.md" README.md` | Đóng PR là duplicate |
| 6 | Không thuộc danh mục cấm | Đọc SKILL.md gốc | Đóng PR + giải thích |
| 7 | Có usage thực tế | Xem star/fork/issue ở openclaw/skills | Đóng PR + đề nghị chờ |

---

## 3. Vòng đời 4 trạng thái của PR

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Open: PR vừa mở
    Open --> Reviewing: Maintainer pick up
    Reviewing --> ChangeRequested: Có vấn đề
    ChangeRequested --> Reviewing: Push commit mới
    Reviewing --> Merged: Pass 7 tiêu chí
    Reviewing --> Closed: Vi phạm tiêu chí cứng
    ChangeRequested --> Stale: Im lặng > 30 ngày
    Stale --> Closed: Auto-close
    Merged --> [*]
    Closed --> [*]
```

---

## 4. Cây quyết định cho maintainer

```mermaid
flowchart TD
    Start([PR mới]) --> Q1{Link 200?}
    Q1 -- ❌ --> R1[Request changes:<br/>fix link]
    Q1 -- ✅ --> Q2{Đã có trên<br/>openclaw/skills?}
    Q2 -- ❌ --> R2[Close: chưa publish]
    Q2 -- ✅ --> Q3{Có usage?<br/>≥ vài tuần}
    Q3 -- ❌ --> R3[Close: too new]
    Q3 -- ✅ --> Q4{Thuộc danh<br/>mục cấm?}
    Q4 -- ✅ --> R4[Close: forbidden topic]
    Q4 -- ❌ --> Q5{Trùng entry?}
    Q5 -- ✅ --> R5[Close: duplicate]
    Q5 -- ❌ --> Q6{Mô tả ≤ 10 từ?}
    Q6 -- ❌ --> R6[Request changes:<br/>shorten desc]
    Q6 -- ✅ --> Q7{Đúng category?}
    Q7 -- ❌ --> R7[Request changes:<br/>move category]
    Q7 -- ✅ --> M[✅ Merge]

    style M fill:#86efac,stroke:#15803d,stroke-width:3px
    style R1 fill:#fde68a
    style R6 fill:#fde68a
    style R7 fill:#fde68a
    style R2 fill:#fca5a5
    style R3 fill:#fca5a5
    style R4 fill:#fca5a5
    style R5 fill:#fca5a5
```

**Quy ước màu:**
- 🟢 Xanh: merge
- 🟡 Vàng: request changes (PR có thể cứu)
- 🔴 Đỏ: close (PR không cứu được)

---

## 5. Vai trò 3 loại người tham gia

### 5.1. Skill Author (tác giả skill)

| Trách nhiệm | Không phải trách nhiệm |
|---|---|
| Publish skill lên openclaw/skills | Maintain repo `awesome-openclaw-skills` |
| Viết SKILL.md đầy đủ | Quyết định category nào "đúng" |
| Cập nhật link khi đổi slug | Review PR người khác |

### 5.2. Contributor (người gửi PR vào repo này)

| Trách nhiệm | Không phải trách nhiệm |
|---|---|
| Tự verify link còn sống | Audit security skill |
| Đặt entry đúng category | Bảo trì code skill upstream |
| Phản hồi review trong 7 ngày | Trả lời các PR khác |
| Tuân thủ format entry | Quyết định category mới |

### 5.3. Maintainer

| Trách nhiệm | Không phải trách nhiệm |
|---|---|
| Áp dụng 7 tiêu chí khi review | Sửa skill cho tác giả |
| Quyết định category mới | Hỗ trợ cài đặt skill cá nhân |
| Định kỳ scan link hỏng | Đảm bảo skill an toàn (chỉ "best effort") |
| Đóng PR vi phạm tiêu chí | Audit security mọi skill được list |

---

## 6. Quy ước nhãn issue/PR (đề xuất)

Repo upstream chưa có label chính thức. Khi cần phân loại, có thể dùng:

| Label đề xuất | Khi nào dùng |
|---|---|
| `add-skill` | PR thêm 1+ skill |
| `fix-link` | PR sửa link hỏng |
| `fix-description` | PR sửa mô tả |
| `category-proposal` | Issue/PR đề xuất category mới |
| `remove-skill` | Issue/PR đề nghị gỡ skill |
| `duplicate` | Đã có entry tương đương |
| `needs-publish-first` | Skill chưa lên openclaw/skills |
| `forbidden-topic` | Crypto/DeFi/blockchain/finance |
| `too-new` | Skill mới publish, chưa có usage |

---

## 7. Bảo trì định kỳ

Vì repo phụ thuộc vào liên kết bên ngoài (openclaw/skills), maintainer nên định kỳ:

```mermaid
gantt
    title Lịch bảo trì đề xuất
    dateFormat YYYY-MM-DD
    section Hàng tháng
    Scan link hỏng         :a1, 2026-01-01, 1d
    Đếm số entry/category   :a2, 2026-01-15, 1d
    section Hàng quý
    Review category lớn quá  :b1, 2026-01-01, 7d
    (>200 entry → tách)
    section 6 tháng
    Audit "forbidden topic" :c1, 2026-03-01, 14d
    sót lại trong list
```

### Script scan link hỏng (tham khảo)

```bash
#!/usr/bin/env bash
# scan-broken-links.sh — liệt kê entry trỏ tới URL không trả 200
set -euo pipefail

grep -oE 'https://github\.com/openclaw/skills[^)]+' README.md \
  | sort -u \
  | while read -r url; do
      code=$(curl -sIL -o /dev/null -w '%{http_code}' --max-time 8 "$url" || echo "ERR")
      if [[ "$code" != "200" ]]; then
        echo "$code $url"
      fi
    done
```

> Chạy: `bash scan-broken-links.sh > broken.txt` — phần lớn entry chạy ~vài phút, có thể song song bằng `xargs -P 16`.

---

## 8. Khi mọi thứ đi sai

| Sự cố | Triage |
|---|---|
| Merge nhầm 1 entry trùng | Mở PR revert ngay, ghi rõ "dedup" |
| Đặt sai category, đã merge | Mở PR sửa nhỏ "Move <slug> to <new category>" |
| Skill upstream bị xoá khỏi openclaw/skills | Mở issue "Remove <slug>" rồi PR gỡ |
| Tác giả đổi slug folder | PR fix link, giữ nguyên vị trí |
| Tranh cãi category | Mở issue thảo luận trước, không revert war |

---

## 9. Tóm tắt 1 dòng cho từng vai trò

```
Skill Author    → "Publish trước. Đợi vài tuần. Mới gửi PR."
Contributor     → "1 dòng đúng format. Đúng category. ≤ 10 từ."
Maintainer      → "Áp 7 tiêu chí. Không review thay tác giả viết SKILL.md."
```

→ Xem tiếp [Bộ mẫu tài liệu](mau/README.md) để có template thực dụng.
