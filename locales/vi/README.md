# OneToEight Agent: tổng quan và quy trình thiết lập

**OneToEight Agent** là một trợ lý AI cá nhân được xây dựng trên
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) dành cho
người trẻ đang học cách đưa **Tám điều thiết yếu** vào thực hành
hằng ngày. Đây là một người cố vấn dịu dàng vận hành nhịp điệu mỗi
ngày gồm các kế hoạch audio, những buổi check-in suy ngẫm, và những
hành động nhỏ, được giảng dạy từ cẩm nang Tám điều thiết yếu đi kèm
trong repo.

README này là phần tổng quan và quy trình để đưa agent hoạt động từ
đầu đến cuối. Hãy đọc một lần, rồi lần lượt làm theo các bước.

> **Hai cách để bắt đầu.** Hãy đi theo **build path** và xây dựng
> agent từng phần một: mỗi tuần một năng lực, một kết quả, kèm audio
> để theo cùng. Hoặc cài đặt bằng quy trình thiết lập bên dưới.
>
> **Bắt đầu build path tại: <https://gladtobe.here.now/build-path/>**

> Đọc bản này bằng: **Tiếng Việt** · [Filipino](README.tl.md) · [English](README.md) · [Bahasa Melayu](README.ms.md) · [ไทย](README.th.md) · [Bahasa Indonesia](README.id.md) · [Español](README.es.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

---

## Sản phẩm này là gì

Một người trẻ học **Tám điều thiết yếu** tốt nhất bằng cách **làm một
việc nhỏ mỗi ngày** suốt nhiều tuần và nhiều tháng, chứ không phải
bằng cách đọc một cuốn sách. OneToEight Agent ra đời để giúp nhịp
điệu hằng ngày đó bền bỉ:

- Một **Phút Buổi Sáng** (Morning Minute) đến vào thời điểm học viên
  chọn, ngay trong chat của họ (Telegram hoặc WhatsApp). Đó là một kế
  hoạch audio ngắn cho ngày mới, kèm văn bản.
- Một **Check-in Buổi Chiều** (Afternoon Check-In) đến vào buổi chiều.
  Đó là một tin nhắn ngắn: ngày hôm nay diễn ra thế nào, tiếp theo là
  gì, một câu hỏi để suy ngẫm qua đêm.
- Một **Buổi Lập Kế Hoạch** (Planning Session) đến trước giờ đi ngủ.
  Nó vạch ra ngày mai: bài vở ở trường, hạn nộp bài tập, điều thiết
  yếu đang thực hành trong tuần, một việc thật ngoài đời họ muốn làm.
  Agent phác thảo kế hoạch, học viên chỉnh sửa, và kế hoạch được lưu
  ngay trên máy. Không app, không tài khoản, không đồng bộ đám mây.
- Agent giảng dạy từ **cẩm nang Tám điều thiết yếu** lưu trong repo
  (`essentials/01..08/lessons/*.md`), phân nhánh theo truyền thống mà
  học viên đã chọn.
- Cẩm nang cũng được xuất bản bằng **mười ngôn ngữ** -- đọc trực
  tuyến, hoặc tải về dưới dạng gói ngoại tuyến để dùng khi không có
  internet. Xem `essentials/guide-editions.md`.

Agent không giảng bài. Nó khơi ra sự khôn ngoan từ chính học viên
bằng những câu hỏi, nâng đỡ nhịp điệu một cách dịu dàng, và giúp họ
bắt đầu lại khi lỡ nhịp -- mà không trách mắng.

### Hai truyền thống, hoặc truyền thống của riêng bạn

Mỗi học viên chọn một truyền thống khi onboarding. Hoặc nói với agent
truyền thống của bạn và nó sẽ tích hợp điều đó. Agent luôn ở trong
truyền thống đã chọn; nó không bao giờ trộn lẫn các truyền thống:

- **Kitô giáo**: neo vào Kinh Thánh. Phút Buổi Sáng có một câu Kinh
  Thánh mỗi sáng, đọc một cách tự nhiên. Check-in đặt ngày hôm nay
  trong một đức tin đang sống.
- **Universal (thế tục)**: tôn trọng các truyền thống trí tuệ mà
  không áp đặt giáo lý. Phút Buổi Sáng có một suy ngẫm hoặc câu hỏi
  ngắn từ một nhà tư tưởng. Check-in đặt ngày hôm nay trong suy ngẫm,
  lòng biết ơn, và ý định.

Học viên có thể đổi truyền thống về sau, nhưng các bài học rẽ nhánh
từ thời điểm đó trở đi.

### Hai trình tự truyền đạt

Mỗi học viên cũng chọn cách tám điều thiết yếu được đưa đến:

- **Theo trình tự** (mặc định): đi lần lượt từ điều thiết yếu 1 đến
  8. Đây là cách mạch lạc nhất và là trình tự mà cẩm nang được viết
  cho. Khuyến nghị cho học viên mới.
- **Ngẫu nhiên**: rút bất kỳ điều thiết yếu nào vào bất kỳ ngày nào,
  khớp với điều học viên có vẻ cần ngày hôm đó (khoảng trống lâu
  nhất, khó khăn gần đây, năng lượng trong ngày). Mỗi Phút Buổi Sáng
  mở đầu bằng bản tóm tắt kiến thức từ điều thiết yếu được chọn, kèm
  một hoạt động nhỏ. Phù hợp nhất cho học viên đã biết mình cần gì.

Ở cả hai chế độ, **rốt cuộc cả tám điều thiết yếu đều được học.**
Học viên có thể chuyển đổi về sau bằng cách cập nhật memory key
`essentials_order` -- không cần onboarding lại.

### Tám điều thiết yếu (theo thứ tự cẩm nang giảng dạy)

1. **Khả năng ngồi trong tĩnh lặng**: ngồi yên, ở một mình với những suy nghĩ của chính mình
2. **Cơ thể bạn là một mái nhà**: giấc ngủ, thức ăn, nước, vận động, ánh nắng
3. **Kỹ năng hữu ích cho đời thực**: năng lực thực tế hữu ích (nấu ăn, sửa chữa, đóng đồ, quản lý chi tiêu)
4. **Tự vệ số**: quyền riêng tư, sự chú ý, hiểu biết về danh tính
5. **Cộng đồng thật**: những người biết tên bạn
6. **Kiến thức không cần Wi-Fi**: sở hữu, không đi thuê
7. **Kê đơn thiên nhiên**: thời gian ở ngoài trời được kê đơn, không thương lượng
8. **Xác tín đã được thử thách**: của riêng bạn, và đứng vững dưới áp lực

---

## Cách hoạt động

### Vòng lặp hằng ngày

```
06:00  Phút Buổi Sáng      Audio Piper TTS + văn bản → Telegram hoặc WhatsApp
        ↓
ngày   Học viên thực hiện hành động nhỏ đó
        ↓
17:00  Check-in Buổi Chiều  Chỉ văn bản → Telegram hoặc WhatsApp
        ↓
21:00  Buổi Lập Kế Hoạch    Chỉ văn bản → Telegram hoặc WhatsApp
       Agent phác thảo kế hoạch ngày mai → học viên chỉnh sửa → lưu trên máy
        ↓
        Ngủ
        ↓
        Lặp lại
```

Agent củng cố vòng lặp này mà không hối thúc. Những ngày lỡ được bắt
đầu lại dịu dàng. Không trách mắng. Không lên lớp đạo đức.

**Về lịch trình:** Các mốc thời gian ở trên là theo múi giờ của học
viên. Cron daemon lưu lịch trình theo **UTC**. Nếu bạn chọn 6 giờ
sáng giờ Việt Nam (UTC+7), cron lưu thành `0 23 * * *` (23:00 UTC).
Lịch trình luôn là "thời gian trong múi giờ của bạn" -- việc chuyển
sang UTC diễn ra tự động.

### Công việc của agent ở mỗi lượt

| Khi nào | Agent làm gì |
|---|---|
| Chat đầu tiên trên profile mới | Gợi ý phần định hướng, ngắn gọn, bằng giọng của chính nó |
| Học viên nói "thiết lập cho tôi" | Chạy `agent-onboarding` (cần đồng ý, theo từng giai đoạn) |
| Học viên đặt câu hỏi | Đọc `essentials/<NN-name>/lessons/*.md` liên quan, tổng hợp, giảng giải |
| Cron Phút Buổi Sáng kích hoạt | Tạo kế hoạch cho ngày, chạy Piper, tải lên, gửi trực tiếp |
| Cron Check-in kích hoạt | Đọc Phút Buổi Sáng gần nhất, phác thảo suy ngẫm ngắn, gửi dạng văn bản |
| Cron Buổi Lập Kế Hoạch kích hoạt | Phác thảo kế hoạch ngày mai (bài vở, hạn nộp, điều thiết yếu của tuần, một việc thật), học viên chỉnh sửa, lưu trên máy |
| Học viên muốn học sâu hơn | Dùng skill `eight-essentials-curriculum` -- đọc cẩm nang, giảng từ đó |

### Những gì chạy nền

Ba cron job, tất cả đều tắt cho đến khi học viên chấp thuận khi
onboarding:

1. **Phút Buổi Sáng**: kích hoạt vào thời điểm đã chọn theo múi giờ
   của học viên, mỗi ngày (hoặc chỉ các ngày trong tuần, nếu muốn).
   Tạo audio + văn bản và gửi đến Telegram hoặc WhatsApp.
2. **Check-in Buổi Chiều**: kích hoạt vào thời điểm buổi chiều đã
   chọn, cùng quy tắc ngày như Phút Buổi Sáng. Gửi một tin nhắn ngắn.
3. **Buổi Lập Kế Hoạch**: kích hoạt trước giờ đi ngủ (mặc định 9
   giờ tối), cùng quy tắc ngày. Phác thảo kế hoạch ngày mai để học
   viên chỉnh sửa, rồi lưu trên máy.

Cả ba đều là **opt-in** -- phần định hướng chỉ tạo chúng sau khi có
sự chấp thuận rõ ràng.

### Hai mươi câu hỏi hằng ngày

Một thư viện nhỏ gồm những câu hỏi quen thuộc mà người trẻ có thể
đặt cho OneToEight Agent bất cứ lúc nào. Agent đọc chương cẩm nang
liên quan, dựa trên những gì nó đã biết về học viên, và trả lời
theo giọng của họ, trong truyền thống của họ.

Điểm mấu chốt **không phải** là trả lời cả hai mươi câu mỗi ngày.
Điểm mấu chốt là có một bộ câu hỏi quen thuộc nhỏ để làm nổi lên
các điều thiết yếu, khơi ra suy ngẫm, và biến sự tò mò thành thực
hành hằng ngày. Chọn một hoặc hai câu. Bỏ qua phần còn lại. Xoay
vòng qua tuần.

Các câu hỏi được viết theo giọng của người trẻ. Agent không giảng
ngược trở lại. Nó đặt câu hỏi, giữ khoảng trống cho câu trả lời, và
tiếp nối bằng một hành động nhỏ.

Tệp đầy đủ các câu hỏi nằm ở
`essentials/00-introduction/lessons/prompts.md`. Agent đọc tệp này
khi học viên xin "một điều gì đó để suy nghĩ", một câu hỏi để ngồi
với nó, hoặc giúp gỡ bí.

#### Theo kiểu

| Kiểu | Câu hỏi |
|---|---|
| Tự suy ngẫm | #1, #3, #6, #7, #12, #15, #16, #20 |
| Hoạt động | #2, #9, #13, #14, #17, #19 |
| Tư duy phản biện | #5, #8, #10, #18 |
| Nghi thức hằng ngày | #11, #16, #20 |

#### Theo năng lượng

| Năng lượng | Câu hỏi gợi ý |
|---|---|
| Mệt, thiếu năng lượng | #1, #20, #11 |
| Bồn chồn, tò mò | #5, #10, #14 |
| Bế tắc hoặc mất hứng | #3, #9, #15 |
| Muốn suy nghĩ | #4, #6, #16, #18 |
| Muốn hành động | #2, #9, #13, #17, #19 |

#### Theo điều thiết yếu (mỗi điều thiết yếu xuất hiện ít nhất hai lần)

| Điều thiết yếu | Những câu hỏi nghiêng về nó |
|---|---|
| Tĩnh lặng | #1, #7, #9, #12, #16 |
| Cơ thể | #2, #9, #14, #19 |
| Kỹ năng | #8, #13, #14 |
| Tự vệ số | #4, #8, #18 |
| Cộng đồng thật | #6, #15, #17 |
| Kiến thức không cần Wi-Fi | #3, #6, #8, #10, #11 |
| Thiên nhiên | #9, #19 |
| Xác tín đã được thử thách | #1, #5, #7, #10, #16, #18 |

#### Những câu hỏi nặng (dùng ít thôi)

Những câu **#1**, **#5**, **#10**, và **#18** là những câu nặng.
Agent không bao giờ tự dựa vào chúng. Học viên phải chủ động gọi
tên chúng. Nếu học viên xin một câu hỏi nặng và agent thấy không
phải ngày phù hợp, agent có thể nhẹ nhàng gợi ý một lựa chọn nhẹ
hơn và giải thích vì sao.

#### Hai mươi câu

| # | Câu hỏi | Kiểu | Năng lượng | Điều thiết yếu |
|---|----------|------|--------|------------|
| 1 | Hỏi tôi một câu mà có lẽ tôi không muốn trả lời, nhưng nên trả lời. | Tự suy ngẫm | Mệt / thiếu năng lượng | Cả tám (đặc biệt là Xác tín đã được thử thách, Tĩnh lặng) |
| 2 | Cho tôi một việc 10 phút khiến tôi thấy khó chịu theo một cách hữu ích. | Hoạt động | Muốn hành động | Cơ thể, Tĩnh lặng, Xác tín đã được thử thách |
| 3 | Ba ngày trước tôi đã làm điều gì mà từ đó tới nay chưa làm lại? Vì sao? | Tự suy ngẫm | Bế tắc / mất hứng | Hiểu mình, Kiến thức không cần Wi-Fi |
| 4 | Chọn một điều thiết yếu tôi yếu nhất. Đâu là thực hành nhỏ nhất tôi có thể làm hôm nay? | Tư duy phản biện | Muốn suy nghĩ | Cả tám (để chẩn đoán) |
| 5 | Phản biện quyết định gần nhất của tôi. Một người phê bình khôn ngoan sẽ nói gì? | Tư duy phản biện | Bồn chồn / tò mò | Kiến thức không cần Wi-Fi, Xác tín đã được thử thách |
| 6 | Nếu tôi phải dạy một học viên mới một điều tôi học được trong năm nay, đó nên là điều gì? | Tự suy ngẫm | Muốn suy nghĩ | Kiến thức không cần Wi-Fi, Cộng đồng thật |
| 7 | Ở đâu trong cuộc sống tôi đang diễn thay vì thật sự làm? Ở đâu tôi thật sự làm thay vì diễn? | Tự suy ngẫm | Mệt / thiếu năng lượng | Xác tín đã được thử thách, Tĩnh lặng |
| 8 | Tôi đang thuê ngoài điều gì mà lẽ ra tôi phải tự xây dựng? | Tư duy phản biện | Muốn suy nghĩ | Kỹ năng, Tự vệ số, Kiến thức không cần Wi-Fi |
| 9 | Cho tôi một hoạt động 30 phút không cần điện thoại và không cần ai khác. | Hoạt động | Bế tắc / mất hứng | Cơ thể, Tĩnh lặng, Thiên nhiên |
| 10 | Đâu là một niềm tin tôi đang giữ mà nếu bị chất vấn tôi không thể bảo vệ? Tôi có nên giữ nó lại không? | Tư duy phản biện | Bồn chồn / tò mò | Xác tín đã được thử thách, Kiến thức không cần Wi-Fi |
| 11 | Kiểm tra tôi về một điều tôi quên mất là mình từng biết. | Nghi thức hằng ngày | Mệt / thiếu năng lượng | Kiến thức không cần Wi-Fi |
| 12 | Hỏi tôi về lần gần nhất tôi thật sự thấy chán, và điều tôi nhận ra trong tĩnh lặng. | Tự suy ngẫm | Bế tắc / mất hứng | Tĩnh lặng, Cơ thể |
| 13 | Gợi ý một việc tôi có thể hoàn thành hôm nay mà tôi đã bắt đầu hơn một tuần trước. | Hoạt động | Muốn hành động | Kỹ năng, Xác tín đã được thử thách |
| 14 | Hướng dẫn tôi cách làm một việc thực tế mà tôi chưa biết làm: tự lo bữa ăn, vá lốp thủng, viết CV, thay lốp xe. | Hoạt động | Bồn chồn / tò mò | Kỹ năng, Cơ thể |
| 15 | Ai trong cuộc đời tôi sẽ có mặt lúc 2 giờ sáng? Ai sẽ không? Vì sao? | Tự suy ngẫm | Bế tắc / mất hứng | Cộng đồng thật |
| 16 | So sánh cách tôi dùng thời gian hôm nay với cách tôi nói tôi muốn dùng nó. Khoảng cách nằm ở đâu? | Nghi thức hằng ngày | Muốn suy nghĩ | Xác tín đã được thử thách, Tĩnh lặng |
| 17 | Cho tôi một câu mở đầu trò chuyện để dùng với một người mà tôi đã lâu không nói chuyện tử tế. | Hoạt động | Muốn hành động | Cộng đồng thật |
| 18 | Nếu tôi xóa mọi ứng dụng trên điện thoại trừ ba ứng dụng, ba ứng dụng nào nên ở lại và vì sao? | Tư duy phản biện | Muốn suy nghĩ | Tự vệ số, Xác tín đã được thử thách |
| 19 | Dẫn tôi ra ngoài 15 phút. Tôi nên thật sự nhìn gì, lắng nghe gì, để ý điều gì? | Hoạt động | Muốn hành động | Thiên nhiên, Cơ thể, Tĩnh lặng |
| 20 | Cùng tôi khép lại một ngày. Ba điều đã xảy ra, ba điều tôi để ý thấy, một điều tôi biết ơn. | Nghi thức hằng ngày | Mệt / thiếu năng lượng | Cả tám (khép lại một ngày) |

#### Cách agent dùng chúng

Agent đọc
`essentials/00-introduction/lessons/prompts.md` mỗi khi học viên
xin một câu hỏi. Nó **không** dán các câu hỏi ra trước mặt học
viên. Nó nhắc đến một câu, mời học viên đọc nó, và giữ khoảng trống
cho câu trả lời. Nó không bao giờ hỏi ba câu liên tiếp.

Ở trình tự **theo trình tự**, các câu hỏi tự nhiên tụ lại quanh
điều thiết yếu mà học viên đang học. Ở trình tự **ngẫu nhiên**,
agent chọn câu hỏi khớp với thời điểm. Cả tám điều thiết yếu vẫn
luôn sẵn có ở cả hai chế độ.

---

## Các nghi thức hằng ngày

Đây là bản đồ nhìn một lượt mọi nghi thức mà agent vận hành: đó là
gì, kích hoạt khi nào, đến ở đâu, và được ghi lại chi tiết ở đâu.

| Nghi thức | Khi nào | Kênh | Điều gì diễn ra |
|---|---|---|---|
| **Phút Buổi Sáng** | Hằng ngày vào thời điểm học viên chọn (mặc định 6 giờ sáng) | Telegram hoặc WhatsApp, **tin nhắn thoại + văn bản** | Kế hoạch audio cho ngày mới, tập trung vào một hành động nhỏ từ điều thiết yếu hiện tại. |
| **Check-in Buổi Chiều** | Hằng ngày vào thời điểm học viên chọn (mặc định 5 giờ chiều) | Telegram hoặc WhatsApp, **chỉ văn bản** | Suy ngẫm về ngày đã qua, kế hoạch cho ngày mai, một câu hỏi để suy ngẫm qua đêm. |
| **Buổi Lập Kế Hoạch** | Hằng ngày trước giờ đi ngủ theo thời điểm học viên chọn (mặc định 9 giờ tối) | Telegram hoặc WhatsApp, **chỉ văn bản** | Agent phác thảo kế hoạch ngày mai (bài vở ở trường, hạn nộp bài tập, điều thiết yếu của tuần, một việc thật ngoài đời). Học viên chỉnh sửa. Lưu trên máy. |
| **Tóm tắt Điều thiết yếu** | Khi được yêu cầu, bất cứ lúc nào | Telegram hoặc WhatsApp, **tin nhắn thoại** | Bản tóm tắt bằng giọng nói 3 đến 5 phút về một điều thiết yếu, kèm danh sách ngắn các ý chính dạng văn bản. |
| **Bài học Điều thiết yếu** | Khi được yêu cầu, bất cứ lúc nào | here.now, **link trang HTML trong chat** | Bài học ba trang về một điều thiết yếu, kèm nguồn được trích dẫn, những trích dẫn chính, và một bài quiz ngắn. |
| **Bài thơ Điều thiết yếu** | Khi được yêu cầu, bất cứ lúc nào | Telegram hoặc WhatsApp, **tin nhắn thoại + văn bản** | Một bài thơ có vần theo lối nói về điều thiết yếu, đọc to kèm văn bản bên dưới. |
| **Bài hát Điều thiết yếu** | Khi được yêu cầu, bất cứ lúc nào | Telegram hoặc WhatsApp, **tin nhắn thoại MP3 + văn bản** | Agent viết một bài thơ về điều thiết yếu, rồi biến nó thành bài hát thật qua Google Lyria 3 trên OpenRouter. Chi phí khoảng ~$0.08 mỗi bài, xác nhận trước khi chạy. |
| **Video ca nhạc Điều thiết yếu** | Khi được yêu cầu, bất cứ lúc nào | here.now, **link video MP4 trong chat** | Bài hát ở trên, kèm storyboard các ảnh tĩnh ghép với audio, có thể phủ thêm lời thơ. Tổng chi phí khoảng ~$0.35, xác nhận trước khi chạy. |

**Một ngày.** Phút Buổi Sáng mở đầu ngày, Check-in khép lại ngày, và
Buổi Lập Kế Hoạch vạch ra ngày mai trước giờ ngủ. Ba định dạng theo
yêu cầu (Tóm tắt / Bài học / Bài thơ) luôn có sẵn mỗi khi người trẻ
muốn học một điều thiết yếu sâu hơn mức một phút của Phút Buổi Sáng.

**Code nằm ở đâu.** Mỗi dòng trong bảng trỏ đến một skill trong repo:

| Nghi thức | Đường dẫn skill |
|---|---|
| Phút Buổi Sáng | `skills/hermes/morning-minute/` |
| Check-in Buổi Chiều | `skills/profile/afternoon-checkin/` |
| Buổi Lập Kế Hoạch | `skills/profile/planning-session/` |
| Tóm tắt, Bài học, Bài thơ, Bài hát, Video ca nhạc | `skills/profile/essential-deep-dives/` (Bài hát và Video ca nhạc dùng `skills/creative/openrouter-lyria-music/` và `skills/creative/poem-song-video-studio/`) |

**Sự đồng ý.** Ba nghi thức chạy theo cron (Phút Buổi Sáng, Check-in,
Buổi Lập Kế Hoạch) đều tắt cho đến khi học viên hoặc phụ huynh chấp
thuận khi onboarding. Năm định dạng theo yêu cầu (Tóm tắt, Bài học,
Bài thơ, Bài hát, Video ca nhạc) có sẵn ngay, học viên chỉ cần yêu
cầu. Hai định dạng tính phí (Bài hát và Video ca nhạc, Lyria 3 + ảnh
storyboard) yêu cầu học viên xác nhận chi phí mỗi lần. Xem [Quy
trình thiết lập → Những gì chạy nền](#những-gì-chạy-nền) để biết
chính xác luồng opt-in.

**Skill Bài hát và Video ca nhạc.** Hai định dạng tính phí dùng lại
hai skill sẵn có thay vì viết lại từ đầu:

| Định dạng | Skill nền tảng | Bổ sung gì trên `essential-deep-dives` |
|---|---|---|
| **Bài hát Điều thiết yếu** | `skills/creative/openrouter-lyria-music/` | Lời THƠ → audio MP3 qua Google Lyria 3 (~$0.08/bài). |
| **Video ca nhạc Điều thiết yếu** | `skills/creative/poem-song-video-studio/` | BÀI HÁT + ~8 ảnh storyboard + ffmpeg → MP4 (~$0.35 tổng cộng). |

Hai skill này đã có sẵn trong repo với đầy đủ ghi chú về model Lyria
3, các script, và cost guard. Agent nạp skill nền tảng khi học viên
yêu cầu định dạng đó.

**Cách tùy chỉnh.** Agent hướng dẫn học viên chọn thời điểm, múi
giờ, và quy tắc ngày cho từng nghi thức cron khi thiết lập. Cả ba có
thể tạm dừng, chạy lại, hoặc gỡ bỏ về sau bằng
`cronjob(action="...")`. Các định dạng theo yêu cầu tự chọn truyền
thống của học viên; giọng và độ dài của chúng kế thừa từ giọng Piper
đã chọn cho Phút Buổi Sáng.

---

## Chi phí vận hành

OneToEight Agent hoạt động theo hình thức **trả tiền theo mức dùng**,
không thuê bao. Bạn nạp tiền vào một tài khoản OpenRouter và agent
dùng số dư đó.

| Khoản chi | Số tiền | Ghi chú |
|---|---|---|
| **Tháng đầu** | **khoảng $20** | Bao gồm thiết lập và tháng đầu sử dụng thật trong lúc học viên dần ổn định |
| **Về sau** | **$5–$10 mỗi tháng** | Dùng hằng ngày ở mức nhẹ với các model chi phí thấp |

Profile dựa vào các model chi phí thấp cho công việc thường ngày:

- **DeepSeek V4 Flash**: mặc định cho chat hằng ngày và bài học.
- **Google Gemini 3.7 Flash**: phương án dự phòng nhanh cho tác vụ ngắn.
- **Các model mã nguồn mở** (miễn phí hoặc gần như miễn phí): cho công việc cơ bản, khối lượng lớn, không cần model tiên tiến nhất.

Gói miễn phí thay đổi theo từng tháng, nên danh sách chính xác cũng
thay đổi. Xem danh sách model miễn phí hiện hành tại
<https://openrouter.ai/openrouter/free>. Profile mặc định dùng các
lựa chọn phải chăng và chỉ chuyển sang model lớn hơn khi tác vụ thật
sự cần.

---

## Các tutorial

Muốn một hướng dẫn có người dẫn đường? Trung tâm tutorial gom tất cả
các trang thiết lập về một chỗ:

- **Build path**: bảy trang dạy bằng cách làm: agent được dựng từng phần một, kèm audio để theo cùng. Bắt đầu tại <https://gladtobe.here.now/build-path/>.
- **Giáo trình onboarding**: bảy trang: khóa học cài đặt, từ lần cài đặt đầu tiên đến một agent đã kết nối với chat.
- **Các bảng walkthrough**: bản thiết lập gói gọn trong một trang, ở ba ngôn ngữ.

Mở trung tâm tại <https://gladtobe.here.now/hub-tutorials.html>. Quy
trình bên dưới bao quát nội dung tương tự bằng văn bản, từng bước.

---

## Quy trình thiết lập

### 1: Điều kiện cần (một lần, trên máy)

Bạn cần:

- **Hermes Agent** đã cài đặt. Kiểm tra nhanh: `hermes --version`. Xem [hướng dẫn cài đặt](https://hermes-agent.nousresearch.com/docs).
- **Python 3.10 đến 3.13** (không phải bản shim của Windows Store, mà là bản cài thật). `python --version`.
- **Piper TTS.** Một bản cài hoạt động được. Xem Bước 2 bên dưới.
- **ffmpeg** để chuyển đổi WAV → OGG. `ffmpeg -version`.
- **Một khóa nhà cung cấp model.** Profile mặc định dùng `openrouter + deepseek-v4-flash`. Một khóa mở ra cả một catalogue model lớn, gồm các model miễn phí và đa phương thức (hình ảnh, audio). Đăng ký miễn phí tại <https://openrouter.ai/> và thêm khóa bằng `hermes setup`. OpenCode Go là phương án dự phòng.
- **Một Jina AI API key miễn phí** cho tìm kiếm web. Đăng ký miễn phí tại <https://jina.ai/>, không cần thẻ tín dụng. Gói miễn phí đủ cho nhu cầu dùng hằng ngày của một người trẻ.
- **Một bot Telegram** (khuyến nghị) hoặc cầu nối WhatsApp. Telegram dễ hơn nhiều, xem Bước 4.

### 2: Giải nén profile (một lần)

Bạn nhận được profile dưới dạng một tệp zip, `onetoeight-agent-vi.zip`.
Giải nén nó vào trong `~/.hermes/profiles/` để thành
`~/.hermes/profiles/onetoeight-agent/`, sau đó:

```bash
mkdir -p ~/.hermes/profiles
# giải nén onetoeight-agent-vi.zip vào trong thư mục này
hermes profile use onetoeight-agent
hermes chat
```

> **Lưu ý:** thư mục profile có tên là `onetoeight-agent`, không phải
> `onetoeight`. Hãy cập nhật các lệnh tham chiếu đến đường dẫn
> profile cho đúng.

Để cập nhật về sau: tải tệp zip mới và giải nén vào một thư mục tạm.
Sao chép các tệp mới vào, nhưng **đừng xóa** thư mục `memories/` và
các phiên đã lưu của bạn. Tệp `LOCALE.md` ở gốc thư mục ghi lại bản
dựng này đến từ phiên bản nào.

### 3: Chat đầu tiên → định hướng

Ở lần chat đầu tiên, agent mở đầu bằng:

> "Trước khi bắt đầu, bạn có muốn tôi hướng dẫn bạn thiết lập không?
> Việc này chỉ mất vài phút và giúp các công cụ, memory, và Phút
> Buổi Sáng của bạn hoạt động đúng theo cách bạn muốn. Hoặc chúng ta
> bỏ qua và bắt đầu luôn."

Hãy nói đồng ý (hoặc chỉ cần hỏi *"giúp tôi thiết lập profile"* bất
cứ lúc nào). Skill `agent-onboarding` sẽ chạy.

### 4: Phần định hướng (cần đồng ý)

Phần định hướng là một cuộc trò chuyện. Agent hỏi từng nhóm câu hỏi
nhỏ liên quan đến nhau một lúc và **dừng lại ở mỗi cổng thông tin
xác thực**, nó không bao giờ hỏi khóa hay token trong chat.

Đây là những gì được đề cập, theo thứ tự:

| Bước | Điều gì diễn ra | Bạn thêm gì ở đâu |
|---|---|---|
| 1. Danh tính | Tên (của bạn, của học viên, của agent), phong cách trả lời, và ngôn ngữ cho cẩm nang, bài học và tin nhắn | Lưu trong profile memory |
| 2. Profile và cuộc sống | Tuổi, nơi ở, hoàn cảnh sống, hình dạng tuần, 3 sở thích, mục tiêu trọng tâm, vòng bạn bè, rào cản, điều cấm đề cập, những trường agent dùng để tùy chỉnh Phút Buổi Sáng và bài học | Lưu trong profile memory |
| 3. Truyền thống | Kitô giáo, Universal, hoặc truyền thống riêng của học viên | Lưu trong profile memory |
| 4. Cài Piper + chọn giọng | Xác minh Piper hoạt động, chọn một giọng, tải model giọng nói | Model giọng nói trong `piper-voices/` |
| 5. Jina API key | Đăng ký miễn phí, thêm vào `.env`, agent xác minh bằng một tìm kiếm thật | `JINA_API_KEY=` trong `.env` |
| 6. Kênh gửi | Thông tin xác thực bot Telegram hoặc WhatsApp | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` trong `.env` |
| 7. Cẩm nang Tám điều thiết yếu | Xác nhận các tệp bài học MD nằm trong `essentials/01..08/lessons/`, và chia sẻ bản cẩm nang theo ngôn ngữ của học viên (`essentials/guide-editions.md`) | Các tệp trong repo |
| 8. Memory | Khuyến nghị Mnemosyne (lưu trên máy, không cần tài khoản ngoài) | `hermes memory setup` |
| 9. Lịch Phút Buổi Sáng | Mấy giờ, múi giờ nào, những ngày nào | Tạo thành một cron job |
| 10. Lịch Check-in Buổi Chiều | Mấy giờ, múi giờ nào, những ngày nào | Tạo thành một cron job |
| 11. Lịch Buổi Lập Kế Hoạch | Mấy giờ (mặc định 9 giờ tối), múi giờ nào, những ngày nào | Tạo thành một cron job |
| 12. Token Router (tùy chọn) | Plugin thu hẹp bề mặt công cụ | `plugins.enabled` trong `config.yaml` |

Cuối cùng, agent hiển thị bản tóm tắt **Proposed setup** và chờ bạn
chấp thuận rõ ràng trước khi áp dụng bất cứ điều gì.

### 5: Kiểm tra từng phần

Trước Phút Buổi Sáng đầu tiên chạy theo lịch, hãy kiểm tra từng
thành phần:

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer jina_x...xxxx" \
  "https://s.jina.ai/https://hermes-agent.nousresearch.com/docs"
# → clean snippet of the docs page means it works

# Telegram bot works (sends a test message)
# Use the test script in Step 3 of the Telegram setup below.
# If you get "chat not found", you must first send any message to your bot in Telegram.

# Guide MD files are present
for d in essentials/*/lessons/; do echo "--- $d ---"; ls "$d"; done

# Mnemosyne is configured
hermes memory status

# Cron jobs are queued
cronjob(action="list")
```

**Vị trí của tệp nhị phân Piper theo nền tảng:**

| Nền tảng | Đường dẫn thường gặp |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (cài thủ công) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, sau đó `piper` có trong PATH |

Phần định hướng sẽ dò tìm Piper và tìm thấy nó nếu nó nằm trong PATH
của bạn. Nếu nó được cài ở một vị trí lạ, phần định hướng sẽ hỏi
đường dẫn.

**Nơi lưu model giọng nói** (tải một lần, dùng mãi về sau):

| Giọng | Khu vực | Đường dẫn Hugging Face |
|---|---|---|
| `en_US-joe-medium` | Nam (US) | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | Nữ (US) | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | Nam (UK) | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | Nữ (UK) | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | Nữ (AU) | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

Cách tải (ví dụ, Joe trên Linux):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6: Lần chạy theo lịch đầu tiên

Phút Buổi Sáng kích hoạt vào thời điểm đã lên lịch kế tiếp theo múi
giờ của học viên. Nó tạo audio (Piper), tải lên here.now để lấy URL
công khai, rồi gửi audio đó trực tiếp đến Telegram qua multipart
upload, **không** qua liên kết `MEDIA:<url>` (cấu hình Cloudflare
của here.now chặn bot tải tệp của Telegram). Check-in kích hoạt vào
thời điểm buổi chiều đã lên lịch kế tiếp.

### 7: Vận hành hằng ngày

Học viên không tương tác với agent qua terminal mỗi ngày. Chat
Telegram hoặc WhatsApp **chính là** bề mặt hằng ngày:

- **Phút Buổi Sáng** đến dưới dạng tin nhắn thoại + kế hoạch văn bản.
- **Check-in Buổi Chiều** đến dưới dạng văn bản.
- **Buổi Lập Kế Hoạch** đến trước giờ đi ngủ dưới dạng văn bản, agent phác thảo kế hoạch ngày mai (bài vở ở trường, hạn nộp bài tập, điều thiết yếu của tuần, một việc thật ngoài đời), học viên chỉnh sửa, và kế hoạch được lưu trên máy. Xem `skills/profile/planning-session/`.
- **Trả lời check-in** bằng một dòng ghi chú về ngày hôm nay. Agent lưu lại bản tóm tắt và dùng nó làm móc nối trong Phút Buổi Sáng hôm sau.
- **Đặt câu hỏi bất cứ lúc nào.** "Đức tin đã được thử thách thật ra trông như thế nào?" "Làm sao tôi tìm được một cộng đồng thật?" Agent đọc cẩm nang và giảng giải.

#### Những cách học sâu hơn (theo yêu cầu)

Ngoài nhịp điệu hằng ngày, học viên có thể yêu cầu bất kỳ **định
dạng sâu hơn** nào về bất kỳ điều thiết yếu nào. Cả ba đều do skill
`essential-deep-dives` đảm nhiệm (xem `skills/profile/essential-deep-dives/`),
và cả ba chỉ cần một điều duy nhất: yêu cầu:

- **Tóm tắt Điều thiết yếu**: những ý chính của một điều thiết yếu
  bằng ngôn ngữ đơn giản, kèm một **tin nhắn thoại** 3 đến 5 phút do
  agent tạo (Piper) và thả vào chat để học viên nghe khi đi bộ hoặc
  làm việc nhà.
- **Bài học Điều thiết yếu**: một **bài học ba trang** đẹp mắt, dựng
  thành trang HTML và xuất bản lên tài khoản **here.now** của gia
  đình. Bài học dạy điều thiết yếu đó với **nguồn được trích dẫn**
  (tra cứu qua Jina API mỗi khi bài học cần tư liệu mà cẩm nang
  không có), **những trích dẫn chính**, và một **bài quiz** ngắn do
  học viên tự trả lời trên trang. Agent gửi link trong chat.
- **Bài thơ Điều thiết yếu**: một **bài thơ nói** có vần về điều
  thiết yếu đó, đọc lên dưới dạng tin nhắn thoại kèm văn bản bên
  dưới để học viên đọc theo.
- **Bài hát Điều thiết yếu**: agent viết một bài thơ gốc về điều
  thiết yếu đó, rồi biến nó thành một bài hát thật (MP3) qua
  `google/lyria-3-pro-preview` trên OpenRouter (~$0.08 mỗi bài).
  Tin nhắn thoại phát trong chat, phần văn bản của bài thơ theo sau.
  Xác nhận chi phí trước khi chạy.
- **Video ca nhạc Điều thiết yếu**: Bài hát ở trên, kèm storyboard
  các khung hình ảnh ghép với audio và lớp phủ lời thơ tùy chọn
  (~$0.35 tổng cộng cho bài hát + ảnh storyboard + dựng ffmpeg).
  Xuất bản dưới dạng MP4 lên here.now; link được gửi trong chat.
  Xác nhận chi phí trước khi chạy.

Agent đọc cẩm nang trước khi phác thảo bất kỳ định dạng nào, phân
nhánh theo truyền thống của học viên, và tùy chỉnh theo profile của
học viên, cùng những quy tắc như skill curriculum.

### 8: Bảo trì

Thỉnh thoảng:

- `hermes update`: kéo thư viện skill chuẩn của Hermes vào profile (các skill được tuyển chọn không bao giờ bị ghi đè).
- `git -C ~/.hermes/profiles/onetoeight-agent pull`: nhận các cải tiến thượng nguồn cho cẩm nang hoặc skill.
- `cronjob(action="list")`: xác nhận cả hai job vẫn còn được lên lịch.

---

## Những gì bạn sẽ cấu hình trong `.env`

Profile đi kèm tệp `.env.example` hiển thị mọi biến. Đây là những
gì bạn thật sự điền.

### Bắt buộc (với mọi thiết lập)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Bắt buộc để gửi qua Telegram

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Lưu ý về thiết lập Telegram:** sau khi tạo bot qua @BotFather,
> bạn **phải gửi cho nó ít nhất một tin nhắn** (ví dụ `/start`)
> trước khi agent có thể gửi cho bạn. Một bot chưa từng nhận tin
> nhắn sẽ thất bại âm thầm khi gửi.

Để tìm chat ID của bạn: nhắn tin cho `@userinfobot` trên Telegram và
nó sẽ trả lời ID số của bạn.

### Bắt buộc cho audio (Phút Buổi Sáng)

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **Lưu ý về here.now:** audio được tải lên qua API publish của
> here.now, API này trả về một URL công khai. URL đó được gửi đến
> Telegram qua multipart upload, nên **không** cần DRIVE_ID. Nếu
> bạn thấy `HERENOW_DRIVE_ID` trong tài liệu hoặc ví dụ cũ, đó là
> phần legacy và không được dùng trong luồng gửi audio hiện tại.

### Tích hợp tùy chọn

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### Những thứ KHÔNG phải env var

- **Đường dẫn model giọng nói**: lưu trong profile memory, không phải env. Đường dẫn tùy theo từng máy.
- **Lịch cron**: đặt qua `cronjob(action="create", ...)`, lưu trong sổ đăng ký cron, không phải env.
- **Đường dẫn tệp nhị phân Piper**: lưu trong profile memory.
- **Mnemosyne**: lưu trên máy, không cần khóa.

---

## Những gì có trong repo

```
onetoeight-agent/
├── README.md                              ← tệp này
├── SOUL.md                                ← persona và giọng vận hành
├── AGENTS.md                              ← nguyên tắc vận hành
├── profile.yaml                           ← mô tả profile
├── config.yaml                            ← cấu hình runtime của Hermes
├── .env.example                           ← mọi biến, kèm chú thích
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← nội dung nguồn của Tám điều thiết yếu
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← Giới thiệu (bản Kitô giáo)
│   │   └── universal.md                   ← Giới thiệu (bản Universal)
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← ghi chú giảng dạy của agent cho điều thiết yếu này
│   │   ├── lessons/
│   │   │   ├── README.md                 ← lược đồ tệp
│   │   │   ├── christian.md               ← Chương 1 (bản Kitô giáo)
│   │   │   └── universal.md               ← Chương 1 (bản Universal)
│   │   └── activities/README.md
│   ├── 02-body/        (cùng cấu trúc)
│   ├── 03-skills/      (cùng cấu trúc)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← Xác tín đã được thử thách + tùy biến Kitô giáo
│   │   │   └── universal.md               ← Xác tín đã được thử thách + tùy biến thế tục
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← cẩm nang trực tuyến bằng mười ngôn ngữ
│
├── skills/
│   ├── hermes/                            ← các skill Hermes được tuyển chọn
│   │   ├── agent-onboarding/  ← phần định hướng
│   │   ├── morning-minute/                ← kế hoạch hằng ngày + audio
│   │   ├── hermes-mnemosyne/              ← nhà cung cấp memory
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← các skill của chính profile
│       ├── afternoon-checkin/           ← suy ngẫm buổi chiều
│       ├── eight-essentials-curriculum/   ← giảng dạy từ cẩm nang
│       ├── essential-deep-dives/          ← các định dạng tóm tắt, bài học, bài thơ
│       └── setup-walkthrough/            ← thiết lập Piper, Jina, kênh gửi
│
├── plugins/hermes-token-router/           ← plugin thu hẹp công cụ (tùy chọn)
├── memories/                              ← các hạt giống thực hành vận hành chung
└── skins/onetoeight.yaml                 ← chủ đề màu
```

> **Các skill Hermes chuẩn** (web, terminal, github, creative, v.v.)
> được `hermes update` kéo về và không thuộc repo này. Chúng nằm
> trong thư viện chuẩn, không phải ở đây.

---

## Tham chiếu cấu hình

### Nhà cung cấp model (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

Thay đổi `provider` và `default` để chuyển. OpenRouter là mặc định vì
một khóa duy nhất mở ra catalogue rộng nhất: các model miễn phí và
đa phương thức (hình ảnh, audio) mà không cần đổi nhà cung cấp.
Chuỗi dự phòng chỉ chạy khi nhà cung cấp chính không khả dụng.

### Toolsets (`config.yaml`)

Mọi toolset CLI đều **bật theo mặc định**. Phần định hướng hướng dẫn
học viên xem xét từng bộ. Để tắt thủ công:

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

Toolset `tts` phải luôn bật cho Phút Buổi Sáng.

### Cron jobs

Tạo qua phần định hướng. Để quản lý thủ công:

```python
# List
cronjob(action="list")

# Create Morning Minute (UTC schedule — 6am AEST = 20:00 UTC)
cronjob(
    action="create",
    schedule="0 20 * * *",
    name="Morning Minute",
    prompt="""You are running the student's Morning Minute.
    Use the morning-minute skill. The student's tradition is
    <christian/universal>. Generate the day's plan, run Piper TTS,
    upload to here.now, deliver via multipart upload to Telegram.
    Do not write memories. Deliver only the final voice + text.""",
    skills=["morning-minute"],
    deliver="telegram",
)

# Weekdays only Morning Minute (6am, Mon–Fri)
cronjob(
    action="create",
    schedule="0 20 * * 1-5",
    name="Morning Minute",
    ...
)

# Pause without deleting
cronjob(action="pause", job_id="<id>")

# Resume
cronjob(action="resume", job_id="<id>")

# Remove (requires approval — deletes the schedule permanently)
cronjob(action="remove", job_id="<id>")
```

Xem `skills/hermes/morning-minute/SKILL.md` để biết toàn bộ đặc tả
cron của Phút Buổi Sáng.

> **Gửi cron:** phiên TUI/CLI không có kênh gửi trực tiếp. Nếu bạn
> muốn được thông báo khi một cron kích hoạt, hãy đặt
> `deliver="telegram"` (hoặc `deliver="all"`) khi tạo. Nếu không,
> kết quả được lưu trên máy và xem được qua `cronjob(action="list")`.

---

## Những lỗi thường gặp

| Triệu chứng | Nguyên nhân thường gặp | Cách khắc phục |
|---|---|---|
| Piper không nạp được | Sai đường dẫn model giọng nói, hoặc chưa tải về | Chạy lại bước Piper trong phần định hướng |
| Audio Phút Buổi Sáng im lặng hoặc bị cắt | Văn bản đầu vào của TTS bị cắt | Kiểm tra tệp văn bản đã đầy đủ trước khi tổng hợp giọng |
| Gửi Telegram thất bại với "chat not found" | Bot chưa từng nhận được tin nhắn | Mở Telegram, tìm bot của bạn, gửi `/start` |
| Audio Telegram không hiển thị | Đang dùng `MEDIA:<url>` với URL here.now | Dùng multipart upload qua `sendVoice` (skill xử lý việc này) |
| Cron kích hoạt sai giờ | Nhầm lẫn UTC | Cron lưu theo UTC. 6 giờ sáng giờ Việt Nam = `0 23 * * *`. 6 giờ sáng giờ Sydney = `0 20 * * *` |
| Đặt là hằng ngày nhưng chỉ kích hoạt ngày thường | Sai định dạng cron | `0 6 * * *` = mỗi ngày. `0 6 * * 1-5` = Thứ Hai đến Thứ Sáu |
| Tìm kiếm Jina không trả về kết quả | Khóa không có trong `.env` hoặc sai | Kiểm tra bằng `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"` |
| Agent đưa nội dung sai truyền thống | Truyền thống chưa có trong memory | Chạy lại bước truyền thống trong phần định hướng |
| Không đọc được tệp bài học | Thiếu hậu tố `.christian.md` hoặc `.universal.md` | Kiểm tra `ls essentials/<NN>/lessons/`, tên tệp phải có hậu tố đúng |

---

## Plugin Token Router (tùy chọn)

Token Router là một plugin Hermes tùy chọn **thu hẹp bề mặt công cụ**
mà agent nhìn thấy, không phải học viên. Khi được bật, agent thấy
ít công cụ hơn theo mặc định, điều này có thể giảm lượng token dùng
và giữ agent tập trung vào công việc của tám điều thiết yếu.

Nó **không** giấu tính năng khỏi học viên. Học viên vẫn có thể hỏi
bất cứ điều gì; router chỉ ảnh hưởng đến những gì agent tự động
chọn.

Bật nếu:
- Bạn muốn giữ agent tập trung vào việc giảng dạy, không phải code hay phân tích dữ liệu.
- Bạn quan tâm đến lượng token dùng.

Giữ tắt nếu:
- Học viên (hoặc phụ huynh) muốn toàn bộ bề mặt công cụ luôn sẵn có.

Để bật: `hermes plugins enable hermes-token-router` (sau khi
`hermes profile use onetoeight-agent`).

---

## Giấy phép

MIT, xem `LICENSE`.

Persona của OneToEight Agent là một nguyên mẫu trợ lý gốc được viết
cho dự án này. Nội dung cẩm nang tám điều thiết yếu đến từ bộ
*Tám điều thiết yếu* của onetoeight, Bản Universal V.3.0.0, được
đưa vào kèm sự cho phép để sử dụng trong profile này.
