from gtts import gTTS
import os

# Văn bản bạn muốn chuyển thành giọng nói
text = "Câu lạc bộ bóng đá Manchester City (tiếng Anh: Manchester City Football Club) là một câu lạc bộ bóng đá Anh có trụ sở tại Manchester, thi đấu tại Giải bóng đá Ngoại hạng Anh, giải đấu hàng đầu của bóng đá Anh. Được thành lập vào ngày 16 tháng 4 năm 1880 với tên gọi St. Mark's (West Gorton), họ trở thành Câu lạc bộ bóng đá Ardwick vào năm 1887 và Manchester City vào năm 1894. Sân nhà của câu lạc bộ là Sân vận động Etihad ở phía đông Manchester, nơi họ chuyển đến vào năm 2003 sau khi thi đấu tại Maine Road kể từ năm 1923. Manchester City sử dụng áo thi đấu sân nhà màu xanh da trời của họ vào năm 1894, trong mùa giải đầu tiên với tên hiện tại.[4] Trong suốt lịch sử của mình, câu lạc bộ đã giành được chín chức vô địch quốc gia, bảy Cúp FA, tám Cúp EFL, sáu Siêu cúp Anh, một UEFA Champions League, một UEFA Cup Winners' Cup và một UEFA Super Cup. Câu lạc bộ tham gia Liên đoàn bóng đá năm 1892 và giành được danh hiệu lớn đầu tiên, Cúp FA, năm 1904. Manchester City đã có giai đoạn thành công lớn đầu tiên vào cuối những năm 1960 và đầu những năm 1970, giành chức vô địch quốc gia, Cúp FA, League Cup và European Cup Winners Cup dưới sự huấn luyện của Joe Mercer và Malcolm Allison. Sau khi thua trận Chung kết Cúp FA 1981, Manchester City đã trải qua một thời kỳ sa sút, với đỉnh điểm là việc xuống hạng ba của bóng đá Anh lần đầu tiên trong lịch sử vào năm 1998. Kể từ đó, họ giành lại quyền thăng hạng lên hạng cao nhất vào năm 2001–02 và tiếp tục là một đội xuất hiện thường xuyên ở Premier League kể từ mùa giải 2002–03."

# Tạo một đối tượng gTTS với văn bản và ngôn ngữ cụ thể (tiếng Việt)
tts = gTTS(text, lang='vi')

# Lưu giọng nói vào tệp âm thanh
tts.save("output.mp3")

# Phát âm thanh
os.system("start output.mp3")
