# Mẫu — Issue đề nghị gỡ skill

> Dùng khi bạn nghĩ một entry **không nên** ở trong list nữa: skill bị xoá upstream, chuyển sang topic cấm, spam, hoặc tác giả yêu cầu gỡ.

---

## Title

```
[Remove] <slug>: <lý do ngắn>
```

Ví dụ:
- `[Remove] crypto-trader: blockchain skill (forbidden topic)`
- `[Remove] foo-bar: deleted from openclaw/skills upstream`
- `[Remove] my-tool: author request`

---

## Body

```markdown
## Lý do đề nghị gỡ
- [ ] Skill đã bị xoá khỏi `openclaw/skills` upstream
- [ ] Skill thuộc danh mục cấm (crypto / blockchain / DeFi / finance)
- [ ] Skill là spam hoặc sinh hàng loạt
- [ ] Tác giả yêu cầu gỡ
- [ ] Skill chứa nội dung độc hại (abuse / bypass / fraud)
- [ ] Skill mất usage / không còn maintained
- [ ] Khác: <ghi rõ>

## Entry liên quan
- **Slug:** `<slug>`
- **Category:** `<tên category>`
- **Link upstream (nếu còn):** https://github.com/openclaw/skills/tree/main/skills/<author>/<slug>

## Entry hiện có trong README.md
```
- [<slug>](URL) - Mô tả hiện tại.
```

## Bằng chứng / dẫn chứng

<Tuỳ loại lý do, đính kèm bằng chứng phù hợp:>

- **Nếu deleted upstream:** screenshot trang 404 + commit upstream xoá folder.
- **Nếu forbidden topic:** trích đoạn SKILL.md nêu rõ chức năng vi phạm.
- **Nếu spam:** liên kết tới các entry tương tự cùng tác giả, hoặc commit history bất thường.
- **Nếu author yêu cầu:** link tới bình luận / email của tác giả (có thể che danh).
- **Nếu nội dung độc hại:** nêu cụ thể hành vi (vd. "skill này tự cài keylogger trong setup hook").

## Đề xuất hành động
- [ ] Tôi sẽ gửi PR gỡ entry (assign tôi)
- [ ] Để maintainer xử lý

## Cảnh báo bảo mật
<Nếu liên quan tới skill có vector tấn công đang được khai thác, đánh dấu rõ và RECOMMEND maintainer act ASAP.>
```

---

## Ví dụ hoàn chỉnh

### Title

```
[Remove] foo-trader: blockchain/crypto skill (forbidden topic)
```

### Body

```markdown
## Lý do đề nghị gỡ
- [x] Skill thuộc danh mục cấm (crypto / blockchain / DeFi / finance)

## Entry liên quan
- **Slug:** `foo-trader`
- **Category:** Finance
- **Link upstream:** https://github.com/openclaw/skills/tree/main/skills/foouser/foo-trader

## Entry hiện có trong README.md
- [foo-trader](https://github.com/openclaw/skills/tree/main/skills/foouser/foo-trader/SKILL.md) - Automated DeFi trading on Uniswap v3.

## Bằng chứng
Trích đoạn SKILL.md upstream:
> "This skill connects to your MetaMask wallet and executes swap transactions on Uniswap v3..."

Skill rõ ràng là DeFi trading — vi phạm policy "No crypto / blockchain / DeFi / finance".

## Đề xuất hành động
- [x] Tôi sẽ gửi PR gỡ entry (assign tôi)
```

---

## Sau khi issue được ack

1. Comment trong issue: "Đang chuẩn bị PR."
2. Mở PR theo [mẫu pull-request.md mục 4](pull-request.md#4-pr-gỡ-skill).
3. Link PR ngược về issue: `Closes #<số issue>`.

---

## Bảng kiểm trước khi gửi

```
☐ Đã verify lý do gỡ (link 404, đọc SKILL.md upstream…)
☐ Đã grep issue/PR cũ — không trùng đề xuất đang treo
☐ Có bằng chứng cụ thể (không chỉ "skill này có vẻ tệ")
☐ Đã quyết định ai sẽ gửi PR (mình hay maintainer)
☐ Nếu là vấn đề bảo mật, đã đánh dấu rõ mức độ ưu tiên
```
