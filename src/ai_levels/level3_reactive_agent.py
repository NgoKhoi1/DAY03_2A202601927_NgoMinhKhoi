"""
🧠 CẤP ĐỘ 3: REACTIVE AGENT (ReAct Agent - Thought -> Action -> Observation)
Agent biết suy nghĩ, tự ra quyết định gọi Tool thực tế và quan sát kết quả để trả lời.
"""

import json

# Định nghĩa Tool thực tế chủ đề Định Hướng Sự Nghiệp
def search_jobs(nganh_nghe: str, dia_diem: str = "Cả nước") -> str:
    return (f"Việc làm ngành {nganh_nghe} tại {dia_diem}:\n"
            f"  - Lập trình viên\n  - Kỹ sư phần mềm\n  - Chuyên gia AI/ML\n"
            f"  Mức lương tham khảo: 15,000,000 - 50,000,000 VNĐ/tháng")

def get_salary_info(nganh_nghe: str) -> str:
    return f"Thông tin lương ngành {nganh_nghe}: 15,000,000 - 50,000,000 VNĐ/tháng."

def reactive_agent_step(user_goal: str):
    print(f"🎯 Goal: {user_goal}")

    # Bước 1: Thought & Action gọi search_jobs tool
    print("\n🧠 [Thought 1]: Cần tra cứu việc làm cho người dùng trước.")
    print("🛠️ [Action 1] : search_jobs('Công nghệ thông tin', 'Cả nước')")
    obs1 = search_jobs("Công nghệ thông tin", "Cả nước")
    print(f"👁️ [Observation 1]:\n{obs1}")

    # Bước 2: Thought & Final Answer
    print("\n🧠 [Thought 2]: Đã có dữ liệu việc làm. Giờ tư vấn lộ trình cho người dùng.")
    print("🏁 [Final Answer]: Ngành CNTT có nhiều cơ hội như Lập trình viên, Kỹ sư phần mềm, Chuyên gia AI/ML với mức lương hấp dẫn 15-50 triệu/tháng. Bạn nên học Python, JavaScript, SQL để bắt đầu!")

if __name__ == "__main__":
    print("=== DEMO CẤP ĐỘ 3: REACTIVE AGENT (ReAct Loop) ===")
    reactive_agent_step("Học CNTT ra làm gì và lương bao nhiêu?")
