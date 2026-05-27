# Mẫu — Entry skill trong README.md

## 1. Mẫu chuẩn (1 skill)

```markdown
- [<slug>](https://github.com/openclaw/skills/tree/main/skills/<author>/<slug>/SKILL.md) - <Mô tả ≤ 10 từ, tiếng Anh>.
```

### Ví dụ điền xong

```markdown
- [smtp-send](https://github.com/openclaw/skills/tree/main/skills/xiwan/smtp-send/SKILL.md) - Send emails via SMTP with HTML and attachments.
```

---

## 2. Mẫu gom nhiều skill cùng tác giả

Dùng khi 1 tác giả có ≥ 2 skill trong **cùng category**.

```markdown
- [<author>-skills](https://github.com/openclaw/skills/tree/main/skills/<author>) - <Mô tả chung ≤ 10 từ>.
```

### Ví dụ điền xong

```markdown
- [security-skills](https://github.com/openclaw/skills/tree/main/skills/chandrasekar-r) - Security audit and real-time monitoring for Clawdbot deployments.
```

---

## 3. Bảng kiểm trước khi paste

```
☐ Slug trùng tên folder trong openclaw/skills
☐ URL trả HTTP 200 (kiểm bằng curl -I)
☐ Mô tả ≤ 10 từ
☐ Mô tả tiếng Anh, không tiếng Việt / ngôn ngữ khác
☐ Mô tả mô tả CHỨC NĂNG, không quảng cáo / hyperbole
☐ Có dấu chấm cuối câu (giữ nhất quán với entry khác)
☐ Cách URL bằng ' - ' (space-dash-space)
☐ Bắt đầu bằng "- [" (đúng cú pháp list markdown)
```

---

## 4. Anti-patterns — đừng làm

| ❌ Sai | Vì sao | ✅ Sửa thành |
|---|---|---|
| `- [my-tool](https://example.com/me/my-tool) - Cool tool.` | Không trỏ openclaw/skills | `- [my-tool](https://github.com/openclaw/skills/tree/main/skills/me/my-tool/SKILL.md) - Cool tool description.` |
| `- [Best Email Tool Ever!!!](...) - The absolute best email tool you will ever use in your life period.` | Marketing, > 10 từ | `- [smtp-send](...) - Send emails via SMTP with attachments.` |
| `- [my-tool](...) Cool tool.` | Thiếu ` - ` | `- [my-tool](...) - Cool tool.` |
| `- [My Tool](.../My-Tool/SKILL.md) - desc` | Slug viết hoa khác folder | `- [my-tool](.../my-tool/SKILL.md) - desc` |
| `- [send mail tự động](.../SKILL.md) - Gửi mail tự động.` | Tiếng Việt | `- [smtp-send](.../SKILL.md) - Send emails via SMTP.` |

---

## 5. Tham chiếu

- Quy tắc chính thức: [CONTRIBUTING.md](../../../CONTRIBUTING.md)
- Phân tích chi tiết hợp đồng entry: [Giải phẫu repo §3](../01-giai-phau-repo.md#3-hợp-đồng-dữ-liệu-của-một-entry)
