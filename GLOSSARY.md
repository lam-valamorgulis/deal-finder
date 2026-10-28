# Deal Finder

Tìm tin đăng bán đồ cũ trên Chợ Tốt có giá thấp hơn thị trường, và xây dữ liệu giá theo từng loại hàng.

## Người dùng

**Người lướt hàng** (Reseller):
Người mua tin giá thấp trên Chợ Tốt để bán lại có lãi. Là người dùng chính của cảnh báo.
_Avoid_: người mua, user

**Khách dữ liệu giá** (Price-data customer):
Người hoặc doanh nghiệp dùng dữ liệu giá của app để định giá hàng cũ, không cần cảnh báo.
_Avoid_: khách hàng, client

## Tin và nhóm

**Tin** (Listing):
Một bài đăng bán trên Chợ Tốt, có giá rao, tiêu đề và mô tả.
_Avoid_: ad, bài, sản phẩm

**Nhóm so sánh** (Comparable group):
Tập các tin cùng loại hàng, cùng cấu hình và cùng tình trạng, mà giá có thể so trực tiếp với nhau.
Ví dụ: iPhone 15 Pro Max 256GB VN/A là một nhóm; bản lock là nhóm khác.
_Avoid_: key, nhóm giá, category

**Giá rao** (Asking price):
Giá người bán ghi trên tin. Không phải giá giao dịch thật.
_Avoid_: giá bán, giá

**Tin biến mất** (Delisted listing):
Tin không còn trên Chợ Tốt. Là dấu hiệu có thể đã bán, nhưng không chắc.
_Avoid_: tin đã bán, sold

**Khu vực mua** (Buying area):
Danh sách quận mà người lướt hàng đi đến được để gặp người bán, mỗi quận kèm số phút đi lại.
_Avoid_: region, vùng, tỉnh

**Đã đăng lâu** (Re-pushed listing):
Tin được người bán đẩy lên đầu lại sau nhiều ngày chưa bán.
_Avoid_: tin cũ, tin yếu

**Tin cũ — mặc cả** (Haggle candidate):
Tin cá nhân, sạch, đã đăng từ 5 ngày trở lên, có giá rao đủ thấp để trả giá thành deal.
_Avoid_: tin ế, stale deal

**Trạng thái tin** (Listing stage):
Bước mà người lướt hàng đang ở với một tin: Mới, Đang theo dõi, Đã liên hệ, Đã mua, Đã bán, hoặc Bỏ qua.
_Avoid_: status, tình trạng (tình trạng là của máy, không phải của tin)

**Tin theo dõi** (Watched listing):
Tin ở trạng thái Đang theo dõi. Chưa phải deal, nhưng người lướt hàng muốn biết khi tin hạ giá hoặc biến mất.
_Avoid_: tin lưu, bookmark, watchlist (watchlist là danh sách từ khóa)

**Sổ giao dịch** (Trade log):
Ghi chép của người lướt hàng về từng tin đã gọi, đã xem, đã mua và đã bán, kèm giá thật ở mỗi bước. Là nguồn giá giao dịch thật duy nhất.
_Avoid_: lịch sử, đơn hàng, order

**Tuần hiệu chỉnh** (Calibration week):
Khoảng thời gian người lướt hàng gọi người bán để đo giá thật (giá chịu bớt, còn hay đã bán), không mua gì.
_Avoid_: test, thử nghiệm

**Checklist trước khi mua** (Pre-buy checklist):
Các bước kiểm máy bắt buộc khi gặp người bán: Activation Lock, lịch sử linh kiện, pin, khóa mạng, không đặt cọc.
_Avoid_: kiểm tra, check

## Kinh doanh

**Phương án kinh doanh** (Business option):
Một cách kiếm tiền từ dữ liệu của app. Ví dụ: lướt hàng, ký gửi, thu mua tại chỗ, bán cho tiệm, bán dữ liệu giá.
_Avoid_: mode, chiến lược

## Nhãn cảnh báo

**Giá bán lại** (Resale basis):
Giá người lướt hàng có thể bán lại món hàng, ước tính từ tin cá nhân mới đăng của cùng nhóm so sánh.
_Avoid_: giá thị trường, trung vị

**Lãi dự kiến** (Expected profit):
Giá bán lại, trừ giá mua, trừ chi phí để mua và bán lại món hàng đó.
_Avoid_: lời, discount, mức giảm

**Kịch bản lãi** (Profit scenario):
Một bộ giả định để tính lãi dự kiến: xấu, giữa, hoặc tốt.
_Avoid_: case, trường hợp

**Giá bỏ đi** (Walk-away price):
Giá rao cao nhất mà tin vẫn có lãi dự kiến đạt mức tối thiểu trong kịch bản giữa.
_Avoid_: ngưỡng, giá trần

**Deal**:
Tin trong khu vực mua có lãi dự kiến, ở kịch bản giữa, từ mức tiền tối thiểu trở lên.
_Avoid_: tin rẻ, hời, kèo

**Mức ưu tiên** (Alert priority):
Cách một cảnh báo đến tay người lướt hàng: Gửi ngay, Gửi gộp, hoặc Chỉ lưu.
_Avoid_: level, độ quan trọng

**Rẻ bất thường** (Price anomaly):
Tin có giá thấp hơn trung vị nhóm so sánh rất nhiều, đến mức không thể là giá bình thường.
Chỉ nói về giá; không phải kết luận lừa đảo.
_Avoid_: nghi lừa đảo, scam_risk, scam
