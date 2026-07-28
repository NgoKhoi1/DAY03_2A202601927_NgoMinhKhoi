"""
🚀 CORE AGENT APP (Dành cho Role 4: Core Agent Developer)
File chính ghép nối tất cả các thành phần: Tools + Prompts + Test Cases + Multi-Provider.
"""

import json
import os
import re
import sys
from dotenv import load_dotenv

# Đảm bảo import các module cùng thư mục src/ hoạt động mượt mà
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Đảm bảo in ra Tiếng Việt và Emojis không bị lỗi trên Windows Console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import các thành phần từ file của Role 2, Role 3 & Multi-Provider Adapter
from tools import AVAILABLE_TOOLS
from prompts import CHATBOT_BASELINE_PROMPT, REACT_SYSTEM_PROMPT, MAX_ITERATIONS
from providers import get_llm_provider

load_dotenv()

def load_test_cases():
    """Đọc bộ test cases từ config/test_cases.json của Role 1"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "test_cases.json")

    # Fallback kiểm tra nếu file ở thư mục hiện tại
    if not os.path.exists(config_path):
        config_path = "test_cases.json"

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_baseline_chatbot(user_query: str, provider):
    """
    Dựng Chatbot gốc (Baseline) không có công cụ.
    """
    print(f"\n💬 [CHATBOT BASELINE] Câu hỏi: {user_query}")
    print(f"⚙️ System Prompt: {CHATBOT_BASELINE_PROMPT.strip()}")

    # Gọi LLM Provider thực hiện sinh câu trả lời
    response = provider.generate(user_query, system_prompt=CHATBOT_BASELINE_PROMPT)
    print(f"🤖 Chatbot trả lời:\n{response}")


# Regex tách "Thought:", "Action: ten_tool[tham_so]" và "Final Answer:" từ output của LLM
_THOUGHT_RE = re.compile(r"Thought:\s*(.*)")
_ACTION_RE = re.compile(r"Action:\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\[(.*?)\]", re.DOTALL)
_FINAL_ANSWER_RE = re.compile(r"Final Answer:\s*(.*)", re.DOTALL)


def _parse_action_args(raw_args: str) -> list:
    """Tách chuỗi tham số 'a, b' thành list ['a', 'b'], bỏ dấu nháy/khoảng trắng thừa."""
    if not raw_args.strip():
        return []
    return [arg.strip().strip("'\"") for arg in raw_args.split(",") if arg.strip()]


def _execute_tool(tool_name: str, raw_args: str) -> str:
    """Thực thi tool tương ứng, luôn trả về chuỗi (không bao giờ crash) theo phanh an toàn của Role 2."""
    tool_func = AVAILABLE_TOOLS.get(tool_name)
    if tool_func is None:
        return (f"LỖI: Không tìm thấy công cụ '{tool_name}'. "
                f"Các công cụ khả dụng: {', '.join(AVAILABLE_TOOLS.keys())}")
    try:
        return tool_func(*_parse_action_args(raw_args))
    except Exception as e:
        return f"LỖI: Tool '{tool_name}' gặp sự cố khi thực thi ({e})."


def run_react_agent(user_query: str, provider):
    """
    Vòng lặp ReAct Agent thật: gọi LLM sinh Thought -> Action, hệ thống thực thi tool
    để lấy Observation thật, rồi phản hồi ngược lại cho LLM tới khi có Final Answer
    hoặc chạm giới hạn MAX_ITERATIONS (Guardrail).
    """
    print(f"\n🤖 [REACT AGENT] Câu hỏi: {user_query}")

    scratchpad = ""
    step = 0

    while step < MAX_ITERATIONS:
        step += 1
        print(f"\n--- 🔄 Vòng lặp ReAct (Step {step}/{MAX_ITERATIONS}) ---")

        prompt = f"Câu hỏi của người dùng: {user_query}\n\n{scratchpad}"
        response = provider.generate(prompt, system_prompt=REACT_SYSTEM_PROMPT)

        action_match = _ACTION_RE.search(response)
        final_match = _FINAL_ANSWER_RE.search(response)

        # Nếu Final Answer xuất hiện trước (hoặc không có Action nào) -> Agent kết thúc
        if final_match and (not action_match or final_match.start() < action_match.start()):
            thought_match = _THOUGHT_RE.search(response)
            if thought_match:
                print(f"🧠 Thought: {thought_match.group(1).strip().splitlines()[0]}")
            final_answer = final_match.group(1).strip()
            print(f"🏁 Final Answer: {final_answer}")
            return final_answer

        if action_match:
            thought_match = _THOUGHT_RE.search(response)
            thought_text = thought_match.group(1).strip().splitlines()[0] if thought_match else "(không rõ)"
            tool_name, raw_args = action_match.group(1), action_match.group(2)

            print(f"🧠 Thought: {thought_text}")
            print(f"🛠️ Action: {tool_name}[{raw_args}]")

            # Chỉ tin Thought/Action đầu tiên từ LLM; Observation LUÔN do hệ thống tự thực thi tool sinh ra
            obs = _execute_tool(tool_name, raw_args)
            print(f"👁️ Observation:\n{obs}")

            scratchpad += f"Thought: {thought_text}\nAction: {tool_name}[{raw_args}]\nObservation: {obs}\n"
            continue

        # LLM không trả về đúng định dạng Thought/Action/Final Answer -> dùng nguyên văn làm câu trả lời cuối
        print("⚠️ Không phát hiện định dạng Action/Final Answer hợp lệ. Dùng phản hồi thô làm câu trả lời cuối.")
        print(f"🏁 Final Answer: {response.strip()}")
        return response.strip()

    print(f"🛡️ GUARDRAIL TRIGGERED: Đã đạt giới hạn tối đa {MAX_ITERATIONS} bước. Ngắt lặp an toàn!")
    return None


if __name__ == "__main__":
    print("==================================================")
    print("🏫 ĐẠI HỌC VINUNI - BÀI LAB 3: CHATBOT VS REACT AGENT")
    print("💼 CHỦ ĐỀ: CHATBOT ĐỊNH HƯỚNG SỰ NGHIỆP")
    print("==================================================")

    # Khởi tạo Multi-Provider LLM Adapter (Đọc từ biến môi trường LLM_PROVIDER)
    provider = get_llm_provider()
    model_name = getattr(provider, "model_name", "Offline Mock Mode")
    print(f"🔌 LLM Provider đang hoạt động: {provider.__class__.__name__} (Model: {model_name})")

    tests = load_test_cases()
    print(f"✅ Đã tải thành công {len(tests)} Test Cases từ config/test_cases.json\n")

    # Chạy thử câu test số 3
    sample_query = tests[2]["question"]

    print("--- DEMO 1: CHẠY TRÊN CHATBOT BASELINE ---")
    run_baseline_chatbot(sample_query, provider)

    print("\n--- DEMO 2: CHẠY TRÊN REACT AGENT ---")
    run_react_agent(sample_query, provider)

    # Demo Guardrail: chạy câu hỏi bẫy (Edge Case) để kiểm tra Agent không bị lặp vô hạn
    trap_query = next((t["question"] for t in tests if "Bẫy" in t.get("category", "")), None)
    if trap_query:
        print("\n--- DEMO 3: KIỂM TRA GUARDRAIL VỚI CÂU HỎI BẪY (EDGE CASE) ---")
        run_react_agent(trap_query, provider)
