"""
NovelMind Web UI - 用 Streamlit 快速搭建
"""
import streamlit as st
from novelforge import Novel, Character
from novelforge.config import Config

# 页面配置
st.set_page_config(
    page_title="NovelMind - AI长篇小说写作",
    page_icon="📖",
    layout="wide"
)

# 侧边栏 - 配置
with st.sidebar:
    st.title("⚙️ 配置")
    
    st.subheader("LLM 配置")
    api_key = st.text_input("API Key", value=Config.LLM_API_KEY, type="password")
    api_base = st.text_input("API Base URL", value=Config.LLM_BASE_URL)
    model = st.selectbox("模型", list(Config.AVAILABLE_MODELS.keys()), index=0)
    
    st.subheader("写作设置")
    temperature = st.slider("创意度", 0.0, 1.0, 0.8)
    max_tokens = st.slider("最大Token", 500, 8000, 4000)

# 主界面
st.title("📖 NovelMind")
st.markdown("用 AI 写长篇小说，让每个角色都是有灵魂的 Agent")

# 初始化session state
if "novel" not in st.session_state:
    st.session_state.novel = None
if "chapters" not in st.session_state:
    st.session_state.chapters = []

# Tab切换
tab1, tab2, tab3 = st.tabs(["📝 创建小说", "📖 阅读", "👥 角色"])

# Tab 1: 创建小说
with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("小说信息")
        title = st.text_input("标题", placeholder="我的小说")
        genre = st.selectbox("类型", ["奇幻", "科幻", "都市", "历史", "仙侠", "悬疑", "其他"])
        
        if st.button("创建小说"):
            if title:
                st.session_state.novel = Novel(title=title, genre=genre)
                st.session_state.chapters = []
                st.success(f"小说《{title}》创建成功！")
            else:
                st.error("请输入标题")
    
    with col2:
        st.subheader("角色管理")
        if st.session_state.novel:
            with st.form("add_character"):
                c_name = st.text_input("角色名")
                c_role = st.selectbox("定位", ["主角", "女主", "反派", "配角", "NPC"])
                c_personality = st.text_input("性格", placeholder="冷静果敢")
                c_goals = st.text_area("目标（逗号分隔）", placeholder="找到真相,拯救世界")
                c_secrets = st.text_input("秘密（可选）", placeholder="体内有神秘血脉")
                
                if st.form_submit_button("添加角色"):
                    import os
                    os.environ["OPENAI_API_KEY"] = api_key or Config.LLM_API_KEY
                    os.environ["OPENAI_API_BASE"] = api_base or Config.LLM_BASE_URL
                    
                    soul = {"personality": c_personality}
                    if c_goals:
                        soul["goals"] = [g.strip() for g in c_goals.split(",")]
                    if c_secrets:
                        soul["secrets"] = c_secrets
                    
                    char = Character(name=c_name, role=c_role, soul=soul)
                    st.session_state.novel.add_character(char)
                    st.success(f"角色 {c_name} 添加成功！")
        
        # 显示已有角色
        if st.session_state.novel and st.session_state.novel.characters:
            st.write("**已有角色：**")
            for name, char in st.session_state.novel.characters.items():
                st.write(f"- {char.name}（{char.role}）: {char.soul.get('personality', '未设置')}")

# Tab 2: 阅读/生成章节
with tab2:
    if not st.session_state.novel:
        st.info("请先在「创建小说」中创建小说")
    else:
        st.subheader("生成章节")
        
        with st.form("write_chapter"):
            chapter_title = st.text_input("章节标题", placeholder="第一章：下山")
            plot_points = st.text_area("情节点（每行一个）", placeholder="初入江湖\n偶遇女主\n发现线索")
            use_llm = st.checkbox("使用 LLM 生成", value=True)
            
            if st.form_submit_button("生成章节", type="primary"):
                if chapter_title and plot_points:
                    import os
                    os.environ["OPENAI_API_KEY"] = api_key or Config.LLM_API_KEY
                    os.environ["OPENAI_API_BASE"] = api_base or Config.LLM_BASE_URL
                    
                    with st.spinner("AI 创作中..."):
                        points = [p.strip() for p in plot_points.split("\n") if p.strip()]
                        chapter = st.session_state.novel.write_chapter(
                            title=chapter_title,
                            plot_points=points,
                            use_llm=use_llm
                        )
                        st.session_state.chapters.append(chapter)
                        st.success(f"章节「{chapter_title}」生成完成！({chapter.word_count}字)")
                else:
                    st.error("请填写章节标题和情节点")
        
        # 显示已生成章节
        if st.session_state.chapters:
            st.subheader("已生成章节")
            for i, ch in enumerate(st.session_state.chapters):
                with st.expander(f"第{i+1}章：{ch.title} ({ch.word_count}字)"):
                    st.write(ch.content)

# Tab 3: 世界观设定
with tab3:
    if not st.session_state.novel:
        st.info("请先创建小说")
    else:
        st.subheader("世界观设定")
        
        with st.form("world_settings"):
            setting_key = st.text_input("设定名称", placeholder="灵气体系")
            setting_value = st.text_area("设定内容", placeholder="五行灵气修炼体系")
            
            if st.form_submit_button("添加设定"):
                if setting_key and setting_value:
                    if not hasattr(st.session_state.novel, 'world_settings'):
                        st.session_state.novel.world_settings = {}
                    st.session_state.novel.world_settings[setting_key] = setting_value
                    st.success(f"设定「{setting_key}」已添加")
        
        # 显示设定
        if hasattr(st.session_state.novel, 'world_settings') and st.session_state.novel.world_settings:
            st.write("**已有设定：**")
            for k, v in st.session_state.novel.world_settings.items():
                st.write(f"- **{k}**: {v}")

# 底部
st.markdown("---")
st.caption("Powered by NovelMind | 用 AI 写有灵魂的长篇小说")