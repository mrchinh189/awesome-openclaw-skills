# Mẫu — Issue báo lỗi entry

> Dùng khi: link hỏng (404), mô tả sai chức năng, lỗi format, sai category. Tự sửa được thì gửi PR luôn theo [pull-request.md](pull-request.md); chỉ mở issue khi không tự sửa được hoặc muốn thảo luận trước.

---

## Title

```
[Bug] <slug>: <mô tả ngắn lỗi>
```

Ví dụ:
- `[Bug] smtp-send: link returns 404`
- `[Bug] ggshield-scanner: description says "Detec" — typo`
- `[Bug] webapp-testing: listed in wrong category`

---

## Body

```markdown
## Loại lỗi
- [ ] Link hỏng (HTTP 4xx/5xx)
- [ ] Mô tả sai chức năng
- [ ] Mô tả vượt 10 từ
- [ ] Slug không khớp folder upstream
- [ ] Sai category
- [ ] Trùng entry khác
- [ ] Lỗi format markdown
- [ ] Khác: <ghi rõ>

## Entry liên quan
- **Slug:** `<slug>`
- **Category hiện tại:** `<tên category>`
- **Dòng trong README.md (nếu biết):** ~<số dòng>

## Quan sát
<Dán entry hiện có vào đây>
```
- [<slug>](URL) - Mô tả hiện tại.
```

## Kỳ vọng
<Mô tả lỗi gì + entry nên trông như thế nào>

## Bằng chứng (nếu có)
- HTTP status: `<output của curl -I URL>`
- Folder upstream thực tế: <URL openclaw/skills/...>
- Screenshot: <kéo thả ảnh vào ô GitHub nếu cần>

## Đề xuất sửa
<Bạn có muốn tự gửi PR sửa không? Có/Không. Nếu có, ghi nhận để maintainer assign issue cho bạn.>
```

---

## Ví dụ hoàn chỉnh

### Title

```
[Bug] smtp-send: link returns 404
```

### Body

```markdown
## Loại lỗi
- [x] Link hỏng (HTTP 4xx/5xx)

## Entry liên quan
- **Slug:** `smtp-send`
- **Category hiện tại:** Web & Frontend Development
- **Dòng trong README.md:** ~147

## Quan sát
- [smtp-send](https://github.com/openclaw/skills/tree/main/skills/xiwan/smtp-send/SKILL.md) - Send emails via SMTP with support for plain text, HTML.

## Kỳ vọng
Link trả 404. Có vẻ tác giả đã đổi slug thành `smtp-mailer` ở upstream.

## Bằng chứng
- HTTP status: `404`
- Folder upstream thực tế: https://github.com/openclaw/skills/tree/main/skills/xiwan/smtp-mailer

## Đề xuất sửa
Có. Tôi sẽ mở PR đổi link sang slug mới.
```

---

## Bảng kiểm trước khi gửi issue

```
☐ Đã verify lỗi tồn tại tại commit HEAD của main
☐ Đã grep issue cũ — không trùng issue đang mở
☐ Đã chỉ rõ slug + category + dòng
☐ Đã đính kèm bằng chứng (HTTP code, screenshot…)
☐ Đã nêu rõ có/không tự gửi PR sửa
```
