"""
🚀 CẤP ĐỘ 4: AUTONOMOUS AGENT (Agent tự chủ với Planning & Memory)
Tự chia nhỏ mục tiêu phức tạp thành nhiều bước, duy trì bộ nhớ (Memory) và tự đánh giá tiến độ.
"""

class AutonomousGoalAgent:
    def __init__(self, goal: str, max_steps: int = 4):
        self.goal = goal
        self.max_steps = max_steps
        self.memory = []  # Bộ nhớ lưu vết các bước đã thực hiện

    def execute(self):
        print(f"🚀 === Bắt đầu Autonomous Goal: {self.goal} ===")

        for step in range(1, self.max_steps + 1):
            print(f"\n--- Vòng lặp tự chủ Planning & Action (Step {step}/{self.max_steps}) ---")

            if step == 1:
                plan = "Bước 1: Tra cứu danh sách việc làm ngành CNTT"
                action = "Call Tool: search_jobs('Công nghệ thông tin', 'Cả nước')"
                result = "Lập trình viên, Kỹ sư phần mềm, Chuyên gia AI/ML."
            elif step == 2:
                plan = "Bước 2: Tra cứu mức lương ngành CNTT"
                action = "Call Tool: get_salary_info('Công nghệ thông tin')"
                result = "Mức lương 15,000,000 - 50,000,000 VNĐ/tháng."
            elif step == 3:
                plan = "Bước 3: Tra cứu kỹ năng cần thiết"
                action = "Call Tool: get_required_skills('Lập trình viên')"
                result = "Python, JavaScript, SQL, Git."
            else:
                print("🎯 [Goal Evaluation]: Mục tiêu đã hoàn thành 100%!")
                break

            self.memory.append({"step": step, "plan": plan, "result": result})
            print(f"📋 [Planning]: {plan}")
            print(f"🛠️ [Execution]: {action} ➔ {result}")
            print(f"💾 [Memory Saved]: Logged step {step} to memory.")

if __name__ == "__main__":
    agent = AutonomousGoalAgent("Tư vấn hướng nghiệp ngành Công nghệ thông tin")
    agent.execute()
