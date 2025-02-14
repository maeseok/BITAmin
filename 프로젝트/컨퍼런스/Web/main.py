import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

# 디바이스 설정
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")  # GPU 대신 CPU 사용

# 모델 저장된 로컬 경로
explainer_model_path = "C:/Users/LWG/Downloads/model"  # 경로 앞에 r을 붙여 원시 문자열로 사용

# 모델 및 토크나이저 로드
explainer_tokenizer = AutoTokenizer.from_pretrained(explainer_model_path)
explainer_model = AutoModelForCausalLM.from_pretrained(explainer_model_path).to(device)




# 대화 상태 관리
story_progress = 0  # 이야기 진행 단계 (1~5)
story_segments = []  # 5단계로 나눈 이야기 저장

few_shot_examples = [
    {
        "input": "꼬꼬무가 무엇인지 설명해줘.",
        "output": "꼬리에 꼬리를 무는 그날 이야기, 줄여서 ‘꼬꼬무’. 사건을 흥미진진하게 풀어가면서 예상치 못한 반전과 충격적인 전개를 선사하는 SBS 교양 프로그램이야. 이야기 속 인물들의 심리를 깊이 파고들고, 중요한 순간마다 '그런데 말이야' 같은 반전 요소를 넣어 몰입감을 높이는 게 특징이지."
    },
    {
        "input": "꼬꼬무에서 이야기를 시작하는 방법 알려줘.",
        "output": "꼬꼬무는 보통 **시간과 장소**를 강조하면서 시작해. 예를 들면: '때는 1999년 10월, 대전의 한 가정집.' 이렇게 말이야. 그리고 **인물 소개와 사건의 평범한 시작**을 보여줘. 하지만 곧이어 **반전 요소**가 등장하면서 본격적인 이야기가 시작되지."
    },
    {
        "input": "꼬꼬무에서 반전이 나올 때 어떻게 표현해?",
        "output": "꼬꼬무는 반전이 있을 때 **'그런데 말이야'** 같은 표현을 써서 시청자들의 기대를 깨. 예를 들어: '평범한 신혼부부의 행복한 나날... 그런데 말이야. 남편이 실종된 지 나흘째, 충격적인 소식이 전해졌습니다. 남편이 차 안에서 숨진 채 발견된 겁니다.' 이렇게 반전을 강조하면서 긴장감을 높여."
    },
    {
        "input": "꼬꼬무에서는 어떻게 시청자의 몰입을 유도해?",
        "output": "꼬꼬무는 이야기를 풀어나가면서 자연스럽게 질문을 던져. 예를 들면: '자, 여기서 이상한 점이 하나 있어. 피해자가 차에서 발견됐는데, 중요한 것이 사라졌어. 그건 뭐였을까?' 이렇게 질문을 던지면 시청자들은 스스로 추리하게 되고, 이야기 속으로 더 빠져들게 돼."
    },
    {
        "input": "꼬꼬무에서는 사건의 진행 과정을 어떻게 설명해?",
        "output": "꼬꼬무는 **시간 순서**를 강조하면서 이야기를 진행해. '자, 10월 2일. 혼인신고를 했어. 그리고 보름 후, 생명보험을 가입했지. 그리고 단 2주 후... 남편이 사라져.' 이렇게 특정 날짜를 반복해서 강조하면서 긴박한 느낌을 줘."
    },
    {
        "input": "꼬꼬무의 결론을 내리는 방식 알려줘.",
        "output": "꼬꼬무는 마지막에도 여운을 남기면서 마무리해. 예를 들면: '그렇게 25년이 지난 지금도, 강영민은 사형수로 복역 중이야. 하지만… 아직도 풀리지 않은 의문이 하나 있어. 그날 밤, 낚시터에서 정말 그들만 있었을까?' 이렇게 새로운 의문을 던지면서 마무리하는 게 특징이지."
    },
    {
        "input": "꼬꼬무에서는 증거가 등장할 때 표현하는 방법 알려줘.",
        "output": "꼬꼬무는 결정적인 증거가 나올 때 **점진적인 서술**을 통해 극적 긴장감을 높여. 예를 들면: '형사들은 차 안을 샅샅이 뒤졌어. 그런데… 조수석에서 발견된 혈흔. 분석 결과, 그것은… 피해자의 것이 아니었어!' 이렇게 **결론을 점진적으로 드러내는 방식**이야."
    },
    {
        "input": "꼬꼬무에서 사건의 배경을 설명할 때 표현하는 방법 알려줘.",
        "output": "꼬꼬무는 사건의 배경을 설정할 때 **차분하게 시작하지만, 점차 긴장감을 높이는 방식**을 사용해. 예를 들면: '때는 1980년 5월. 광주의 거리에는 평범한 시민들이 가득했어. 하지만… 군인들이 총을 들고 거리로 나오기 시작했지.' 이렇게 점진적으로 분위기를 고조시키는 게 중요해."
    },
    {
        "input": "꼬꼬무에서는 사건의 배경을 강조할 때 어떻게 표현해?",
        "output": "꼬꼬무는 사건의 배경을 묘사할 때 감각적인 표현을 많이 사용해. 예를 들면: '때는 1985년 여름. 무더운 날씨 속, 한 남자가 시장 한가운데를 천천히 걸어가고 있었어. 하지만… 몇 시간 후, 그 남자는 흔적도 없이 사라졌지.' 이렇게 생생한 묘사를 통해 시청자의 상상력을 자극해."
    },
    {
        "input": "꼬꼬무에서 등장인물의 심리를 강조하는 방법은?",
        "output": "꼬꼬무는 등장인물의 심리를 강조할 때 감정이입을 유도하는 질문을 던져. 예를 들면: '수연 씨는 아무것도 모른 채 저녁을 차리고 있었어. 하지만… 그녀는 몰랐지. 그날이 남편을 마지막으로 보는 날이 될 거라는 걸.' 이렇게 인물의 감정 변화를 강조해서 몰입감을 높여."
    },
    {
        "input": "꼬꼬무에서는 반복적인 표현을 어떻게 활용해?",
        "output": "꼬꼬무는 특정 단어나 구절을 반복해서 강조하는 방식으로 긴장감을 조성해. 예를 들면: '그날 밤, 경찰은 단서를 찾지 못했어. 단 하나의 단서도. 단 한 조각도. 그런데… 다음 날, 놀라운 사실이 밝혀지지.' 이렇게 반복적인 문장을 활용해서 점점 압박감을 높이는 거지."
    },
    {
        "input": "꼬꼬무에서 중요한 순간을 강조할 때 어떤 기법을 사용해?",
        "output": "꼬꼬무는 중요한 순간을 강조할 때 **일부 정보를 숨긴 채 문장을 끊어** 궁금증을 유발해. 예를 들면: '형사들은 서랍을 열었어. 그리고… 믿기 힘든 걸 발견하지. 그것은 바로…' 이렇게 궁금증을 극대화하면서 긴장감을 유지하는 방식이야."
    },
    {
        "input": "꼬꼬무에서 공포감을 조성할 때 어떤 기법을 사용해?",
        "output": "꼬꼬무는 공포감을 조성할 때 **느린 템포로 진행하며 주변 분위기를 강조해**. 예를 들면: '깜깜한 밤이었어. 거리에는 아무도 없었지. 그런데… 누군가 따라오고 있었어. 발소리가 하나… 둘… 가까워지고 있었지.' 이렇게 감각적인 표현과 템포 조절을 활용해 긴장감을 고조시켜."
    },
    {
        "input": "꼬꼬무에서 예상과 다른 결말을 강조하는 방법은?",
        "output": "꼬꼬무는 예상과 다른 결말을 강조할 때 마지막 순간까지 긴장을 유지해. 예를 들면: '모든 게 끝난 줄 알았어. 범인은 검거됐고, 사건은 해결됐지. 그런데 말이야… 10년 후, 한 통의 편지가 도착했어.' 이렇게 결말 부분에서 또 다른 반전을 제시해서 시청자의 흥미를 유도해."
    },
    {
        "input": "꼬꼬무에서 범인의 심리를 묘사하는 방법은?",
        "output": "꼬꼬무는 범인의 심리를 묘사할 때 **행동을 구체적으로 설명하면서 불안감을 강조해**. 예를 들면: '그는 계속해서 손을 떨고 있었어. 그리고… 창밖을 자꾸 확인했지. 마치 누군가를 기다리는 것처럼.' 이렇게 작은 행동 하나하나를 묘사하면서 시청자가 긴장감을 느끼게 만들어."
    },
    {
        "input": "꼬꼬무 스타일로 1972년 워터게이트 사건을 설명해줘.",
        "output": "때는 1972년. 미국 대통령 선거를 앞둔 워싱턴 D.C. 민주당 본부에 낯선 사람들이 침입해. 단순한 절도일까? 그런데 말이야 이 사건의 배후에 당시 대통령이었던 리처드 닉슨이 있었다면?"
    },
    {
        "input": "꼬꼬무 스타일로 1994년 성수대교 붕괴 사건을 설명해줘.",
        "output": "때는 1994년 10월 21일, 서울 성수대교. 평범한 출근길이었어. 그런데 말이야… 갑자기 다리가 '쾅!' 무너져 내린 거야. 과연, 이 사고는 정말 예측할 수 없었던 걸까?"
    },
    {
        "input": "꼬꼬무 스타일로 1997년 IMF 외환위기를 설명해줘.",
        "output": "때는 1997년 11월. 대한민국 경제가 휘청이기 시작해. 그런데 말이야… 단순한 경기 침체가 아니었어. 결국 대한민국은 IMF에 구제금융을 신청하는 사상 초유의 사태를 맞이하게 되지."
    },
    {
        "input": "꼬꼬무 스타일로 1980년 5.18 광주 민주화운동을 설명해줘.",
        "output": "때는 1980년 5월. 광주 시민들은 군부 독재에 맞서 민주화를 외쳤어. 그런데… 계엄군이 시민들을 향해 총을 겨누었지. 그날, 광주에서는 무슨 일이 있었던 걸까?"
    }
]


# 이야기 단계 추출 함수
def extract_contents(text):
    pattern = r"\*\*\d+단계:.*?\*\*\s*([\s\S]*?)(?=\n\s*\*\*|\Z)"
    return [match.strip() for match in re.findall(pattern, text)]

# 불필요한 텍스트 정리
def clean_text(text):
    return re.sub(r"\.\n\s*\n\s*---", "", text).strip()

# 첫 번째 프롬프트 (이야기 개요 생성)
def generate_story_outline(user_input):
    global story_segments, story_progress
    story_progress = 0  # 초기화
    
    prompt = f"""
    🎬 **꼬리에 꼬리를 무는 이야기 (꼬꼬무) 스타일 스토리텔링**
    
    아래 예시 답변을 참고해서, 주어진 주제에 대한 꼬꼬무 스타일의 이야기를 만들어줘.
    
    ---
    **📌 꼬꼬무 스타일 예시 답변 구조**
    {few_shot_examples}
    ---
    
    **📝 생성 가이드라인**
    - 답변은 반드시 **꼬리에 꼬리를 무는 이야기**처럼 구성해야 해.
    - 모든 문장은 **반말체**로 진행해야 해.
    - 총 **5단계**로 나누어 이야기를 전개하며, 각 단계는 "1단계: "와 같이 명확히 구분해.
    - **긴장감과 몰입도를 유지하도록** 각 단계마다 반전 요소나 궁금증을 유발하는 내용을 포함해.
    - **최대한 자연스럽고 생동감 있는 서술 방식**으로, 독자가 마치 다큐멘터리를 보듯이 흥미롭게 읽을 수 있도록 작성해.
    - 문장 길이는 적절히 조절하며, 전체 답변은 **3000자 내외**로 구성해.
    - 과장된 표현과 묘사를 활용해 분위기를 극대화해.
    
    ---
    **🔎 질문:** {user_input}
    
    🎬 **답변**
    """
    
    inputs = explainer_tokenizer(prompt, return_tensors="pt").to(device)
    outputs = explainer_model.generate(**inputs, max_new_tokens=4000, do_sample=True, top_p=0.9, temperature=0.8)
    full_story = explainer_tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    story_segments = extract_contents(full_story)
    if story_segments:
        story_progress = 1  # 첫 번째 단계로 진행
        return clean_text(story_segments[0])
    else:
        return "이야기 생성에 실패했습니다. 다시 시도해주세요."

# 두 번째 프롬프트 (단계별 진행 + 사용자 반응 포함)
def generate_story_segment(user_response):
    global story_progress, story_segments
    
    if story_progress >= len(story_segments):
        return "✅ 오늘의 이야기는 여기까지야!"
    
    prompt = f"""
    🎬 **지금까지의 이야기 요약**  
    "{' '.join(story_segments[:story_progress])}"
    
    🗣 **사용자의 반응**  
    "{user_response}"
    
    ---
    너는 해설자로서, 사용자의 반응에 맞는 짧고 임팩트 있는 리액션을 해.  
    답변은 **10자 이내**, **반말**, **문장 끝은 감탄사 또는 여운을 남기는 표현**을 사용해야 한다.  
    이야기의 진행을 바꾸지 않지만, **긴장감을 유지하거나 다음 전개를 암시할 수 있다.**  
    사용자의 감정에 따라 맞춰 반응하되, 필요하면 감탄사, 의문형, 단호한 코멘트를 활용할 수 있다.  

    🎬 **답변 예시**  
    1. 사용자: "헉, 너무 소름 돋아", 해설자: "소름 끼치지?"
    2. 사용자: "와 진짜 대박이다", 해설자: "대박이지!"  
    3. 사용자: "뭐야, 갑자기 왜 그래?", 해설자: "그러게, 이상하지?"  
    4. 사용자: "이제 어떻게 돼?", 해설자: "다음이 중요해!"  
    5. 사용자: "설마 죽는 거야?", 해설자: "그럴지도...!"  
    6. 사용자: "아, 그냥 뻔한 이야기네", 해설자: "과연 그럴까?"  

    🎬 **답변**  
    """
    
    inputs = explainer_tokenizer(prompt, return_tensors="pt").to(device)
    outputs = explainer_model.generate(**inputs, max_new_tokens=1024, do_sample=True, top_p=0.9, temperature=0.8)
    reaction = explainer_tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    response = reaction + "\n\n" + clean_text(story_segments[story_progress])
    story_progress += 1
    
    return response

# Gradio UI 생성
def chatbot(user_input, user_response):
    global story_progress
    
    if story_progress == 0:
        return generate_story_outline(user_input)
    else:
        return generate_story_segment(user_response)

# Gradio UI 적용
with gr.Blocks(css='#chatbot .overflow-y-auto{height:750px}') as demo:
    state_chatbot = gr.State([])  # 대화 기록 저장

    with gr.Row():
        gr.HTML("""
        <div style="text-align: center; max-width: 600px; margin: 0 auto;">
            <h1>📜 꼬꼬무 RAG 챗봇</h1>
            <p style="margin-bottom: 10px; font-size: 94%">
                역사와 사건을 탐구하는 AI 챗봇!  
            </p>
        </div>
        """)

    # 챗봇 UI
    with gr.Row():
        chatbot_ui = gr.Chatbot(elem_id='chatbot')

    # 입력창 + 버튼
    with gr.Row():
        txt_input = gr.Textbox(show_label=False, placeholder='질문을 입력하세요...').style(container=False)
        btn_next = gr.Button("➡️ 다음 단계")

    # 챗봇 동작 로직
    def chatbot_logic(state_chatbot, user_input):
        global story_progress
        
        if story_progress == 0:
            response = generate_story_outline(user_input)
        else:
            response = generate_story_segment(user_input)
        
        state_chatbot.append(("🗣 사용자", user_input))
        state_chatbot.append(("📜 해설자", response))

        return state_chatbot, state_chatbot

    # 입력창에서 Enter 키 입력 시 실행
    txt_input.submit(chatbot_logic, [state_chatbot, txt_input], [state_chatbot, chatbot_ui])
    txt_input.submit(lambda: '', None, txt_input)  # 입력창 초기화

    # 버튼 클릭 시 다음 단계 진행
    btn_next.click(chatbot_logic, [state_chatbot, txt_input], [state_chatbot, chatbot_ui])

# 실행
demo.launch(debug=True, share=True)
