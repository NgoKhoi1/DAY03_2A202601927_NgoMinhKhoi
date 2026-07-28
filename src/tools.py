"""
🛠️ TOOL REGISTRY & SCHEMAS (Dành cho Role 2: Tool & Spec Engineer)
Chủ đề: Chatbot Định Hướng Sự Nghiệp (Career Guidance)
Các công cụ giúp tra cứu thông tin việc làm, lộ trình nghề nghiệp, kỹ năng, lương, công ty.
"""

CAREER_DATA = {
    "cong_nghe_thong_tin": {
        "jobs": ["Lập trình viên", "Kỹ sư phần mềm", "Chuyên gia AI/ML", "Kỹ sư dữ liệu"],
        "salary_range": "15,000,000 - 50,000,000 VNĐ/tháng",
        "skills": ["Python", "JavaScript", "SQL", "Machine Learning", "Git"],
        "top_companies": ["FPT Software", "VNG", "Viettel", "Vingroup"],
        "career_path": "Junior Dev -> Middle Dev -> Senior Dev -> Tech Lead -> Engineering Manager"
    },
    "kinh_doanh_quan_tri": {
        "jobs": ["Chuyên viên Marketing", "Quản trị kinh doanh", "Chuyên viên Nhân sự", "Chuyên viên Tài chính"],
        "salary_range": "10,000,000 - 35,000,000 VNĐ/tháng",
        "skills": ["Phân tích dữ liệu", "Quản lý dự án", "Giao tiếp", "Tiếng Anh"],
        "top_companies": ["Unilever", "P&G", "MASAN", "Vingroup"],
        "career_path": "Chuyên viên -> Trưởng nhóm -> Phó phòng -> Trưởng phòng -> Giám đốc"
    },
    "y_duoc": {
        "jobs": ["Bác sĩ", "Dược sĩ", "Điều dưỡng", "Kỹ thuật viên xét nghiệm"],
        "salary_range": "12,000,000 - 60,000,000 VNĐ/tháng",
        "skills": ["Chẩn đoán", "Giao tiếp bệnh nhân", "Kiến thức chuyên môn", "Tiếng Anh y khoa"],
        "top_companies": ["BV Bạch Mai", "BV Chợ Rẫy", "Vinmec", "BV Nhi Đồng"],
        "career_path": "Thực tập -> Bác sĩ/Dược sĩ -> Chuyên khoa -> Trưởng khoa -> Giám đốc bệnh viện"
    },
    "kien_truc_xay_dung": {
        "jobs": ["Kiến trúc sư", "Kỹ sư xây dựng", "Kỹ sư kết cấu", "Giám sát công trình"],
        "salary_range": "12,000,000 - 40,000,000 VNĐ/tháng",
        "skills": ["AutoCAD", "Revit", "Quản lý dự án", "Tiếng Anh kỹ thuật"],
        "top_companies": ["Coteccons", "Hoa Binh", "Ricons", "Unicons"],
        "career_path": "Kỹ sư tập sự -> Kỹ sư -> Kỹ sư trưởng -> Quản lý dự án -> Giám đốc dự án"
    },
    "truyen_thong_bao_chi": {
        "jobs": ["Phóng viên", "Biên tập viên", "Chuyên viên Truyền thông", "Content Creator"],
        "salary_range": "8,000,000 - 25,000,000 VNĐ/tháng",
        "skills": ["Viết lách", "Dựng video", "Quay phim", "SEO", "Mạng xã hội"],
        "top_companies": ["VTV", "VnExpress", "Tuổi Trẻ", "VNPT Media"],
        "career_path": "Thực tập -> Phóng viên/Biên tập -> Trưởng ban -> Phó TBT -> Tổng Biên tập"
    }
}


def search_jobs(nganh_nghe: str, dia_diem: str = "Cả nước") -> str:
    """
    Tra cứu danh sách công việc theo ngành nghề và địa điểm.

    Args:
        nganh_nghe (str): Tên ngành nghề (Ví dụ: 'Công nghệ thông tin', 'Kinh doanh', 'Y dược')
        dia_diem (str): Địa điểm làm việc (Ví dụ: 'Hà Nội', 'TP.HCM', 'Đà Nẵng'). Mặc định: 'Cả nước'

    Returns:
        str: Danh sách các vị trí công việc phù hợp
    """
    key = _normalize_major(nganh_nghe)
    if key not in CAREER_DATA:
        return (f"LỖI: Không tìm thấy thông tin ngành nghề '{nganh_nghe}'. "
                f"Các ngành hiện có: {', '.join(k.replace('_', ' ').title() for k in CAREER_DATA)}")

    data = CAREER_DATA[key]
    jobs_str = "\n".join(f"  - {job}" for job in data["jobs"])
    return (f"Việc làm ngành {nganh_nghe.title()} tại {dia_diem}:\n"
            f"{jobs_str}\n"
            f"Mức lương tham khảo: {data['salary_range']}")


def get_career_path(nganh_hoc: str) -> str:
    """
    Tra cứu lộ trình thăng tiến nghề nghiệp theo ngành học.

    Args:
        nganh_hoc (str): Tên ngành học (Ví dụ: 'Công nghệ thông tin', 'Kinh doanh quản trị')

    Returns:
        str: Lộ trình nghề nghiệp từ cấp bậc thấp lên cao
    """
    key = _normalize_major(nganh_hoc)
    if key not in CAREER_DATA:
        return (f"LỖI: Không tìm thấy lộ trình cho ngành '{nganh_hoc}'. "
                f"Vui lòng chọn: {', '.join(k.replace('_', ' ').title() for k in CAREER_DATA)}")

    data = CAREER_DATA[key]
    return (f"Lộ trình nghề nghiệp ngành {nganh_hoc.title()}:\n"
            f"  {data['career_path']}\n\n"
            f"Các vị trí phổ biến:\n" +
            "\n".join(f"  - {job}" for job in data["jobs"]))


def get_salary_info(nganh_nghe: str) -> str:
    """
    Tra cứu mức lương tham khảo theo ngành nghề.

    Args:
        nganh_nghe (str): Tên ngành nghề (Ví dụ: 'Công nghệ thông tin', 'Y dược')

    Returns:
        str: Khoảng lương phổ biến của ngành
    """
    key = _normalize_major(nganh_nghe)
    if key not in CAREER_DATA:
        return (f"LỖI: Không tìm thấy thông tin lương cho ngành '{nganh_nghe}'. "
                f"Các ngành hiện có: {', '.join(k.replace('_', ' ').title() for k in CAREER_DATA)}")

    data = CAREER_DATA[key]
    return (f"Thông tin lương ngành {nganh_nghe.title()}:\n"
            f"  Khoảng lương: {data['salary_range']}\n"
            f"  Các vị trí: {', '.join(data['jobs'])}")


def get_required_skills(cong_viec: str) -> str:
    """
    Tra cứu kỹ năng cần thiết cho một công việc hoặc ngành nghề.

    Args:
        cong_viec (str): Tên công việc hoặc ngành nghề (Ví dụ: 'Lập trình viên', 'Công nghệ thông tin')

    Returns:
        str: Danh sách kỹ năng quan trọng cần có
    """
    for key, data in CAREER_DATA.items():
        if _match_job_or_major(cong_viec, key, data):
            skills_str = "\n".join(f"  - {skill}" for skill in data["skills"])
            return (f"Các kỹ năng cần thiết cho '{cong_viec.title()}':\n"
                    f"{skills_str}")

    return (f"LỖI: Không tìm thấy thông tin kỹ năng cho '{cong_viec}'. "
            f"Các ngành hiện có: {', '.join(k.replace('_', ' ').title() for k in CAREER_DATA)}")


def get_top_companies(linh_vuc: str) -> str:
    """
    Tra cứu danh sách công ty / tập đoàn hàng đầu trong lĩnh vực.

    Args:
        linh_vuc (str): Tên lĩnh vực (Ví dụ: 'Công nghệ thông tin', 'Y dược')

    Returns:
        str: Danh sách các công ty nổi bật
    """
    key = _normalize_major(linh_vuc)
    if key not in CAREER_DATA:
        return (f"LỖI: Không tìm thấy thông tin công ty cho lĩnh vực '{linh_vuc}'. "
                f"Các lĩnh vực hiện có: {', '.join(k.replace('_', ' ').title() for k in CAREER_DATA)}")

    data = CAREER_DATA[key]
    companies_str = "\n".join(f"  - {c}" for c in data["top_companies"])
    return (f"Các công ty hàng đầu trong lĩnh vực {linh_vuc.title()}:\n"
            f"{companies_str}")


MAJOR_ALIASES = {
    "cong_nghe_thong_tin": ["công nghệ thông tin", "cntt", "it", "lập trình", "phần mềm", "tin học", "informatique"],
    "kinh_doanh_quan_tri": ["kinh doanh", "quản trị kinh doanh", "marketing", "tài chính", "kế toán", "business"],
    "y_duoc": ["y dược", "dược", "bác sĩ", "y khoa", "dược sĩ", "medical"],
    "kien_truc_xay_dung": ["kiến trúc", "xây dựng", "công trình", "architecture"],
    "truyen_thong_bao_chi": ["truyền thông", "báo chí", "media", "báo chí truyền thông"],
}

COURSE_DATA = {
    "python": ["Python for Everybody (Coursera)", "100 Days of Code Python (Udemy)", "Python Data Structures"],
    "machine learning": ["Machine Learning Specialization by Andrew Ng (Coursera)", "Deep Learning Specialization"],
    "sql": ["Complete SQL Bootcamp (Udemy)", "SQL for Data Science (Coursera)"],
    "marketing": ["Digital Marketing Specialization (Coursera)", "Google Digital Garage Certificate"],
    "tieng anh": ["IELTS Preparation Specialization", "Business English Certificate"],
    "quan ly du an": ["PMP Exam Prep Course", "Agile Project Management Specialization (Google)"],
    "autocad": ["AutoCAD Complete Course (Udemy)", "Revit Architecture Essential"],
}

CERTIFICATION_DATA = {
    "cong_nghe_thong_tin": ["AWS Certified Solutions Architect", "Google Cloud Professional", "CKA (Certified Kubernetes Administrator)", "TensorFlow Developer Certificate"],
    "kinh_doanh_quan_tri": ["PMP (Project Management Professional)", "CFA (Chartered Financial Analyst)", "Digital Marketing Professional"],
    "y_duoc": ["Chứng chỉ hành nghề Y/Dược", "USMLE (Kỳ thi giấy phép y tế Hoa Kỳ)", "IELTS Academic 7.0+"],
    "kien_truc_xay_dung": ["Chứng chỉ hành nghề thiết kế kiến trúc", "Chứng chỉ Kỹ sư định giá", "Autodesk Certified Professional"],
    "truyen_thong_bao_chi": ["HubSpot Content Marketing Certification", "Google Analytics Certification", "Adobe Certified Professional"]
}

INTERVIEW_DATA = {
    "cong_nghe_thong_tin": [
        "1. Hãy trình bày về một dự án lập trình quan trọng bạn đã từng thực hiện?",
        "2. Phân biệt SQL và NoSQL, khi nào nên chọn loại nào?",
        "3. Làm thế nào bạn giải quyết vấn đề xung đột mã nguồn (merge conflict) trong Git?"
    ],
    "kinh_doanh_quan_tri": [
        "1. Bạn đánh giá hiệu quả của một chiến dịch Marketing bằng những chỉ số nào?",
        "2. Hãy kể về một lần bạn xử lý bất đồng ý kiến trong nhóm dự án.",
        "3. Kế hoạch phát triển doanh số trong 3 tháng đầu tiên của bạn là gì?"
    ],
    "y_duoc": [
        "1. Bạn xử lý như thế nào khi gặp trường hợp bệnh nhân không hợp tác?",
        "2. Nêu các bước quy trình chẩn đoán lâm sàng chuẩn.",
        "3. Bạn cập nhật kiến thức y khoa mới bằng những nguồn nào?"
    ]
}

RESUME_TIPS_DATA = {
    "cong_nghe_thong_tin": [
        "• Dùng link GitHub / Portfolio đính kèm trong CV.",
        "• Đưa các dự án thực tế kèm công nghệ sử dụng (Tech Stack) lên đầu.",
        "• Định lượng kết quả (Ví dụ: Tối ưu thời gian phản hồi API giảm 30%)."
    ],
    "kinh_doanh_quan_tri": [
        "• Tập trung vào con số (Doanh thu tăng %, số lượng khách hàng thu hút).",
        "• Mổ xẻ các dự án từng tham gia và vai trò cụ thể của bạn.",
        "• Nêu rõ kỹ năng mềm và kỹ năng quản lý nhóm."
    ]
}

MIN_SUBSTRING_LENGTH = 4


def _normalize_major(name: str) -> str:
    name_lower = name.lower().strip()
    for key, aliases in MAJOR_ALIASES.items():
        key_no_sep = key.replace("_", " ")
        if name_lower == key_no_sep:
            return key
        for alias in aliases:
            if name_lower == alias:
                return key
            if len(alias) >= MIN_SUBSTRING_LENGTH and len(name_lower) >= MIN_SUBSTRING_LENGTH:
                if name_lower in alias or alias in name_lower:
                    return key
    if name_lower in CAREER_DATA:
        return name_lower
    return name_lower


def _match_job_or_major(name: str, key: str, data: dict) -> bool:
    name_lower = name.lower().strip()
    key_no_sep = key.replace("_", " ")
    if name_lower == key_no_sep:
        return True
    for job in data["jobs"]:
        job_lower = job.lower()
        if name_lower == job_lower:
            return True
        if len(name_lower) >= MIN_SUBSTRING_LENGTH and len(job_lower) >= MIN_SUBSTRING_LENGTH:
            if name_lower in job_lower or job_lower in name_lower:
                return True
    for alias in MAJOR_ALIASES.get(key, []):
        if name_lower == alias:
            return True
        if len(alias) >= MIN_SUBSTRING_LENGTH and len(name_lower) >= MIN_SUBSTRING_LENGTH:
            if name_lower in alias or alias in name_lower:
                return True
    return False


def assess_career_suitability(so_thich: str, ky_nang: str) -> str:
    """
    Đánh giá mức độ phù hợp và gợi ý ngành nghề dựa trên sở thích và kỹ năng hiện có.

    Args:
        so_thich (str): Sở thích của người dùng (Ví dụ: 'lập trình', 'vẽ', 'giao tiếp', 'kinh doanh')
        ky_nang (str): Kỹ năng hiện có (Ví dụ: 'Python', 'tiếng Anh', 'viết lách')

    Returns:
        str: Gợi ý các ngành nghề phù hợp kèm lý do
    """
    input_text = f"{so_thich} {ky_nang}".lower()
    matches = []

    if any(w in input_text for w in ["lập trình", "python", "it", "máy tính", "code", "ai", "dữ liệu"]):
        matches.append("Công nghệ thông tin (Phù hợp với tư duy logic & kỹ năng kỹ thuật)")
    if any(w in input_text for w in ["giao tiếp", "kinh doanh", "bán hàng", "marketing", "quản lý"]):
        matches.append("Kinh doanh & Quản trị (Phù hợp với giao tiếp & tư duy thị trường)")
    if any(w in input_text for w in ["y học", "chăm sóc", "bệnh nhân", "thuốc", "y tế", "sức khỏe"]):
        matches.append("Y dược (Phù hợp với tinh thần chăm sóc & kiến thức y khoa)")
    if any(w in input_text for w in ["vẽ", "thiết kế", "xây dựng", "kiến trúc", "công trình"]):
        matches.append("Kiến trúc & Xây dựng (Phù hợp với khả năng sáng tạo không gian & kỹ thuật)")
    if any(w in input_text for w in ["viết", "content", "báo chí", "quay phim", "truyền thông", "mạng xã hội"]):
        matches.append("Truyền thông & Báo chí (Phù hợp với tư duy sáng tạo & khả năng thể hiện nội dung)")

    if not matches:
        matches.append("Công nghệ thông tin hoặc Kinh doanh quản trị (Các ngành phổ biến & đa dạng cơ hội)")

    results_str = "\n".join(f"  - {m}" for m in matches)
    return (f"Dựa trên sở thích '{so_thich}' và kỹ năng '{ky_nang}', các ngành gợi ý cho bạn:\n"
            f"{results_str}")


def search_courses(ky_nang: str) -> str:
    """
    Tìm kiếm các khóa học / chứng chỉ đề xuất theo kỹ năng cần học.

    Args:
        ky_nang (str): Kỹ năng cần tìm khóa học (Ví dụ: 'Python', 'Machine Learning', 'Marketing', 'Tiếng Anh')

    Returns:
        str: Danh sách khóa học tham khảo
    """
    ky_nang_lower = ky_nang.lower().strip()
    found_courses = []
    for k, courses in COURSE_DATA.items():
        if k in ky_nang_lower or ky_nang_lower in k:
            found_courses.extend(courses)

    if not found_courses:
        found_courses = [
            f"Khóa học chuyên sâu về {ky_nang.title()} trên Coursera",
            f"Khóa học {ky_nang.title()} thực hành trên Udemy",
            f"Chứng chỉ chuyên môn về {ky_nang.title()} trên LinkedIn Learning"
        ]

    courses_str = "\n".join(f"  - {c}" for c in found_courses)
    return (f"Gợi ý các khóa học phù hợp cho kỹ năng '{ky_nang.title()}':\n"
            f"{courses_str}")


def recommend_certifications(nganh_nghe: str) -> str:
    """
    Đề xuất các chứng chỉ nghề nghiệp uy tín và giá trị cho ngành nghề.

    Args:
        nganh_nghe (str): Tên ngành nghề (Ví dụ: 'Công nghệ thông tin', 'Kinh doanh', 'Y dược')

    Returns:
        str: Danh sách các chứng chỉ hàng đầu
    """
    key = _normalize_major(nganh_nghe)
    certs = CERTIFICATION_DATA.get(key, [
        f"Chứng chỉ chuyên môn ngành {nganh_nghe.title()} (Quốc tế)",
        "Chứng chỉ Ngoại ngữ (IELTS / TOEIC / JLPT)",
        "Chứng chỉ Quản lý & Kỹ năng mềm"
    ])
    certs_str = "\n".join(f"  - {c}" for c in certs)
    return (f"Các chứng chỉ giá trị cho ngành {nganh_nghe.title()}:\n"
            f"{certs_str}")


def get_interview_questions(vi_tri_hoac_nganh: str) -> str:
    """
    Tra cứu danh sách các câu hỏi phỏng vấn thường gặp cho ngành/vị trí.

    Args:
        vi_tri_hoac_nganh (str): Vị trí hoặc ngành nghề (Ví dụ: 'Công nghệ thông tin', 'Kinh doanh')

    Returns:
        str: Danh sách các câu hỏi phỏng vấn gợi ý
    """
    key = _normalize_major(vi_tri_hoac_nganh)
    questions = INTERVIEW_DATA.get(key, [
        f"1. Hãy giới thiệu bản thân và lý do bạn chọn vị trí {vi_tri_hoac_nganh.title()}?",
        f"2. Bạn đã từng đối mặt với khó khăn gì lớn nhất trong công việc và cách vượt qua?",
        f"3. Định hướng nghề nghiệp 3-5 năm tới của bạn là gì?"
    ])
    q_str = "\n".join(f"  {q}" for q in questions)
    return (f"Các câu hỏi phỏng vấn thường gặp cho '{vi_tri_hoac_nganh.title()}':\n"
            f"{q_str}")


def get_resume_tips(vi_tri_hoac_nganh: str) -> str:
    """
    Tra cứu các mẹo viết CV và tối ưu hồ sơ ứng tuyển cho vị trí/ngành nghề.

    Args:
        vi_tri_hoac_nganh (str): Vị trí hoặc ngành nghề (Ví dụ: 'Công nghệ thông tin', 'Kinh doanh')

    Returns:
        str: Các lời khuyên tối ưu CV
    """
    key = _normalize_major(vi_tri_hoac_nganh)
    tips = RESUME_TIPS_DATA.get(key, [
        "• Trình bày CV ngắn gọn, súc tích (1-2 trang).",
        "• Sử dụng từ khóa chính liên quan đến mô tả công việc (JD).",
        "• Nêu rõ thành tích và kết quả đạt được bằng con số cụ thể."
    ])
    tips_str = "\n".join(f"  {t}" for t in tips)
    return (f"Mẹo viết CV ấn tượng cho ngành '{vi_tri_hoac_nganh.title()}':\n"
            f"{tips_str}")


AVAILABLE_TOOLS = {
    "search_jobs": search_jobs,
    "get_career_path": get_career_path,
    "get_salary_info": get_salary_info,
    "get_required_skills": get_required_skills,
    "get_top_companies": get_top_companies,
    "assess_career_suitability": assess_career_suitability,
    "search_courses": search_courses,
    "recommend_certifications": recommend_certifications,
    "get_interview_questions": get_interview_questions,
    "get_resume_tips": get_resume_tips,
}

