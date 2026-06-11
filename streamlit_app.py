import streamlit as st

# 1. 국외 유명 건축물 데이터베이스 (사진 제외)
BUILDING_DATA = {
    "2001": {
        "name": "에펠탑 (Eiffel Tower) - 프랑스 파리",
        "location": "프랑스 파리",
        "height": "330m",
        "description": "1889년 파리 만국박람회를 기념하여 건축가 구스타프 에펠이 설계한 철탑입니다. 건립 당시에는 도시의 미관을 해친다는 이유로 많은 반대를 받았으나, 현재는 파리와 프랑스를 상징하는 세계적인 랜드마크이자 건축 공학의 걸작으로 꼽힙니다."
    },
    "2002": {
        "name": "자유의 여신상 (Statue of Liberty) - 미국 뉴욕",
        "location": "미국 뉴욕 리버티 섬",
        "height": "93m (기단 포함)",
        "description": "1886년 미국의 독립 100주년을 기념하여 프랑스가 기증한 거대한 동상입니다. 오른손에는 횃불을, 왼손에는 독립선언서를 들고 있으며, 아메리칸 드림을 꿈꾸며 뉴욕항으로 들어오는 이민자들을 환영하는 자유와 민주주의의 상징입니다."
    },
    "2003": {
        "name": "부르즈 할리파 (Burj Khalifa) - 아랍에미리트 두바이",
        "location": "아랍에미리트 두바이",
        "height": "828m",
        "description": "지상 163층 규모로, 인간이 만든 구조물 중 세계에서 가장 높은 마천루입니다. 사막의 꽃인 '히메노칼리스'의 모양에서 영감을 얻어 나선형으로 상승하는 구조로 설계되었으며, 대한민국 기업인 삼성물산이 시공에 참여하여 국내에서도 큰 화제가 되었습니다."
    },
    "2004": {
        "name": "타지마할 (Taj Mahal) - 인도 아그라",
        "location": "인도 우타르프라데시주 아그라",
        "height": "약 73m",
        "description": "무굴 제국의 황제 샤 자한이 유독 총애했던 왕비 뭄타즈 마할의 죽음을 애도하며 22년에 걸쳐 지은 백대리석 무덤입니다. 완벽한 대칭 구조와 전 세계에서 가져온 보석들로 장식된 외벽이 특징이며, 세상에서 가장 아름다운 건축물 중 하나로 손꼽힙니다."
    },
    "2005": {
        "name": "콜로세움 (Colosseum) - 이탈리아 로마",
        "location": "이탈리아 로마",
        "height": "약 48m",
        "description": "서기 80년경 로마 제국 시대에 완공된 거대한 타원형 원형 경기장입니다. 약 5만 명의 관객을 수용할 수 있었으며 검투사의 시합, 야수 사냥 등 대중적인 오락 행사가 열렸습니다. 고대 로마의 뛰어난 건축 공학 기술과 규모를 보여주는 대표적인 유적입니다."
    },
    "2006": {
        "name": "시드니 오페라 하우스 (Sydney Opera House) - 호주 시드니",
        "location": "호주 시드니 베네롱 포인트",
        "height": "65m",
        "description": "덴마크의 건축가 이외른 우촌이 설계하여 1973년에 완공된 20세기 최고의 건축물 중 하나입니다. 조개껍데기 혹은 요트의 돛을 형상화한 독창적인 지붕 모양이 특징이며, 빼어난 현대적 디자인을 인정받아 2007년 유네스코 세계문화유산으로 지정되었습니다."
    }
}

# 2. 스트림릿 앱 UI 설정
st.set_page_config(page_title="세계 유명 건축물 조회", page_icon="🌍", layout="centered")

st.title("🌍 세계 유명 건축물 정보 시스템")
st.markdown("건축물 번호를 입력하시면 해당 세계적 건축물의 이름, 위치, 높이 및 상세 설명을 보여드립니다.")

# 팁 박스로 가이드 제공
with st.expander("💡 사용 가능한 건축물 번호 목록 보기", expanded=True):
    cols = st.columns(3)
    for i, (code, info) in enumerate(BUILDING_DATA.items()):
        # 3열로 나누어 이쁘게 배치
        cols[i % 3].markdown(f"**{code}** : {info['name'].split('(')[0]}")

st.divider()

# 3. 사용자 입력 받기
building_id = st.text_input("건축물 번호를 입력하세요 (예: 2001)", placeholder="번호를 입력하고 Enter를 누르세요.").strip()

# 4. 결과 출력
if building_id:
    if building_id in BUILDING_DATA:
        info = BUILDING_DATA[building_id]
        
        # 타이틀 및 기본 정보
        st.subheader(f"🔍 {info['name']}")
        
        # 깔끔하게 표 형태로 위치와 높이 안내
        st.markdown(f"📌 **위치:** {info['location']}")
        st.markdown(f"📏 **높이:** {info['height']}")
        
        st.divider()
        
        # 상세 설명
        st.markdown("### 📝 건축물 설명")
        st.info(info['description'])
        
    else:
        st.error(f"❌ 입력하신 번호 '{building_id}'에 해당하는 건축물 정보가 없습니다. 목록의 번호를 확인해 주세요.")