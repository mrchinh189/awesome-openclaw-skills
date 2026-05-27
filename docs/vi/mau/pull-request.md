# Mẫu — Pull Request

> Copy nội dung phần phù hợp vào ô PR description trên GitHub. Title PR theo quy ước `CONTRIBUTING.md`.

---

## 1. PR thêm skill mới

### Title

```
Add skill: <author>/<slug>
```

### Body

```markdown
## Loại PR
- [x] Thêm skill mới
- [ ] Sửa entry cũ
- [ ] Đề xuất category mới

## Skill được thêm
- **Slug:** `<slug>`
- **Tác giả:** `<author>`
- **Category:** `<Tên category>`
- **Link upstream:** https://github.com/openclaw/skills/tree/main/skills/<author>/<slug>/SKILL.md

## Entry đã thêm
```
- [<slug>](https://github.com/openclaw/skills/tree/main/skills/<author>/<slug>/SKILL.md) - <Mô tả ≤ 10 từ>.
```

## Checklist
- [x] Skill đã publish trên `openclaw/skills` (link 200)
- [x] Slug trùng tên folder upstream
- [x] Mô tả ≤ 10 từ, tiếng Anh, không quảng cáo
- [x] Đặt cuối block `<details>` của category đúng
- [x] Đã grep `README.md` không thấy entry trùng
- [x] Skill không thuộc danh mục cấm (crypto/blockchain/DeFi/finance)
- [x] Skill có usage thực tế (≥ vài tuần publish)

## Ghi chú thêm
<Nếu có thông tin cần maintainer biết, ví dụ: lý do chọn category này, mối quan hệ với entry hiện có…>
```

---

## 2. PR sửa entry (fix link / mô tả)

### Title

```
Fix: <slug> <broken link | description | typo>
```

Ví dụ:
- `Fix: smtp-send broken link`
- `Fix: ggshield-scanner description shortened`

### Body

```markdown
## Loại PR
- [ ] Thêm skill mới
- [x] Sửa entry cũ
- [ ] Đề xuất category mới

## Vấn đề
<Mô tả ngắn: link 404? mô tả sai? slug đổi?>

## Trước
```
- [<slug>](URL_CŨ) - Mô tả cũ.
```

## Sau
```
- [<slug>](URL_MỚI) - Mô tả mới.
```

## Verify
- [x] URL mới trả HTTP 200
- [x] Slug vẫn khớp với folder upstream
- [x] Mô tả mới ≤ 10 từ
```

---

## 3. PR đề xuất category mới (sau khi issue đã được ack)

### Title

```
Add category: <Tên Category>
```

### Body

```markdown
## Loại PR
- [ ] Thêm skill mới
- [ ] Sửa entry cũ
- [x] Đề xuất category mới

## Tham chiếu
Closes #<số issue đã được ack>

## Thay đổi đã làm
1. Thêm mục trong Table of Contents:
   ```
   - [<Tên Category>](#<anchor>) (<số entry>)
   ```
2. Thêm block `<details>` mới ở vị trí <…> với <N> entry khởi tạo.

## Danh sách entry khởi tạo (≥ 5 entry để justify category)
<liệt kê N entry với link và mô tả>

## Phân tích trùng lặp
- Đã rà soát các category liên quan: <category A>, <category B>
- Không có entry nào trùng với category mới này.
```

---

## 4. PR gỡ skill

### Title

```
Remove: <slug>
```

### Body

```markdown
## Lý do gỡ
- [ ] Skill bị xoá khỏi `openclaw/skills` upstream
- [ ] Skill thuộc danh mục cấm (lý do: …)
- [ ] Tác giả yêu cầu gỡ
- [ ] Skill là spam / sinh hàng loạt
- [ ] Khác: <ghi rõ>

## Tham chiếu
- Issue gốc: #<số issue>
- Link skill (nếu còn): https://github.com/openclaw/skills/...

## Entry bị xoá
```
- [<slug>](URL) - Mô tả.
```

## Ảnh hưởng
<Có entry nào khác trỏ tới cùng tác giả/category không? — thường là không, nhưng ghi cho rõ.>
```

---

## 5. Hướng dẫn xử lý review comment

Khi maintainer comment trên PR:

| Loại comment | Hành động |
|---|---|
| "Please shorten description" | Sửa entry, `git commit --amend` HOẶC commit mới rồi push |
| "Wrong category, move to X" | Cut entry khỏi category cũ, paste vào cuối X, push |
| "Duplicate of #NNN" | Comment thừa nhận, đóng PR |
| "Skill not published yet" | Đóng PR, publish lên openclaw/skills, đợi vài tuần, mở PR mới |
| "Forbidden topic" | Đóng PR, không tranh luận |
| "Looks good, just one nit" | Sửa nit, push, ping maintainer 1 lần |

> **Quy tắc vàng:** không tranh cãi 7 tiêu chí cứng. Tranh luận chỉ có ích cho:
> (a) chọn category, (b) wording mô tả, (c) cách gom skill cùng tác giả.

---

## 6. Mẫu commit message

```
Add skill: <author>/<slug>
Fix: <slug> broken link
Fix: <slug> description shortened to 9 words
Move: <slug> to <new-category>
Remove: <slug> (deleted from upstream)
Add category: <Tên Category>
```

**Đừng** dùng:
- `Update README.md` (quá chung)
- `fix` (không nói gì)
- `WIP` (không bao giờ merge WIP)
- Emoji thuần (`✨ skill`) — giữ plain text cho repo Anglo-Saxon style awesome list.
