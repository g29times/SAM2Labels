# Streamlit 前端主程序
# Adapted from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps#build-a-simple-chatbot-gui-with-streaming
import streamlit as st
import random
import time
import restllm as client
from PIL import Image
import json
from io import StringIO

import sys
sys.path.append(r"D:\WorkHome\Projects\SELF\ML\utils")
import upload_image_util
import converte
sys.path.append(r"D:\WorkHome\Projects\SELF\ML\g_sam")
import gen
import get
import timeutil

system = ""
fileName = ""
to_xywh_json = ""
width = 100
height = 100
project_id = 1

with st.sidebar:
    if st.button("清除历史"):
        st.session_state.messages.clear()

    st.markdown("<span ><font size=1>联系我</font></span>", unsafe_allow_html=True)
    "[GitHub](<https://github.com/g29times>)"

    st.write("设置您的项目号：")
    project_id = st.text_input("")
    folder = '.'
    option = st.selectbox('选择您的操作系统', (system, 'windows', 'linux', 'mac'), index=None)
    # st.write("You selected:", option)
    if option == "windows":
        folder_windows = st.text_input("设置Windows图片文件夹路径(\结尾)：", value="E:\GoogleSync\\6 AI\\3 dataset\Picture\\")
        folder = folder_windows
    elif option == "linux":
        folder_linux = st.text_input("设置Linux图片文件夹路径(/结尾)：", value="/mnt/pictures/")
        folder = folder_linux

    if 'model' not in st.session_state or st.session_state.model != option:
        st.session_state.model = option

    upload_image = st.file_uploader("上传图像", accept_multiple_files=False, type=['jpg', 'png'])
    if upload_image:
        fileName = upload_image.name
        st.write(folder + fileName)
        
        # 显示图片
        image = Image.open(upload_image)
        # 获取图片的宽度和高度
        width, height = image.size
        st.write(width, height)
        st.image(image, caption=fileName, use_column_width=True)
        
        # TODO 1 相对路径问题 2 import 3 convert 4 文件下载 5 路径
        # 开始上传到互联网
        try:
            upload_response = upload_image_util.upload_image(folder + fileName)
            # st.write(upload_response)
            # st.write(upload_response.content)
            # st.write(upload_response.status_code)
            if(upload_response.status_code == 200):
                img_url = json.loads(upload_response.text)['data']['url']
                st.write("已上传至: " + img_url)
                
                # SAM处理
                gen_response = gen.lable_image(img_url)
                if(json.loads(gen_response)['status'] == "starting"):
                    st.info("启动远程打标！")
                    sam_url = json.loads(gen_response)['urls']['get']
                    st.write("获取SAM结果: " + sam_url)
                    print()
                    # 等待g-sam解析
                    while True:
                        flag = get.get_labels("", project_id, sam_url, width, height)
                        if flag:
                            print("远程结果已经返回。")
                            st.write(flag)
                            # TODO 可下载json文件
                            break
                        else:
                            print("结果还未返回，正在等待...")
                            time.sleep(15)
                else:
                    # 402 付费 {"title":"Free time limit reached","detail":"You have reached the free time limit. To continue usinlicate, set up billing at https://replicate.com/account/billing#billing.","status":402}
                    st.info("远程打标失败！状态[{}]".format(json.loads(gen_response)['status']))
                    
                    upload_json = st.file_uploader("可选择本地SAM数据以继续", accept_multiple_files=False, type=['json', 'txt'])
                    # TODO if upload_json:触发了无限请求
                    if upload_json:
                        print(" --- Streamlit 读取本地SAM文件 --- ")
                        json_file_name = upload_json.name
                        # To convert to a string based IO:
                        stringio = StringIO(upload_json.getvalue().decode("utf-8"))
                        # st.write(stringio)

                        # To read file as string:
                        string_data = stringio.read()
                        # st.write(string_data)
                        
                        to_xywh_json = converte.convert_json(json.loads(string_data), project_id, fileName, width, height)
                        # st.write(to_xywh_json)

                        st.info("可复制以下命令到对话框查看，或下载结果文件：")
                        st.code(f"""data/{json_file_name}""")
                        st.download_button(
                            label="下载结果!",
                            data=json.dumps(to_xywh_json, default=timeutil.json_serial, indent=4),
                            file_name=fileName + ".json",
                            mime="application/json"
                        )
            else:
                st.error("图片上传失败！请稍后重试")
        # except OSError as e:
            # print(f"发生了一个文件系统错误：{e}")
        except OSError as e:
            print(f"发生了一个文件系统错误：{e}")
            st.error("找不到指定的文件夹或文件！")
def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None

col1, col2 = st.columns([6,1])

with col1:
    st.header(f"IMAGE AUTO LABELING")

with col2:
    st.button('Reset ↺', on_click=reset_chat)


# Initialize chat history
if "messages" not in st.session_state:
    reset_chat()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.chat_input("What's up?")
if prompt:
# if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        context = st.session_state.context

        print("system ----------------- ", system) # TODO 根据系统做处理
        # msg = client.chat_with_model(MODEL, prompt, system, context=context)
        # st.session_state.messages.append({"role": "assistant", "content": msg})
        # st.chat_message("assistant").write(msg)

        # Simulate stream of response with milliseconds delay
        # for chunk, ctx in client.chat_with_model(MODEL, prompt, system, context=context):
        #     full_response += chunk
        #     message_placeholder.markdown(full_response + "▌")
        # full_response = msg
        message_placeholder.markdown("*:red[Streamlit]* :orange[can] :green[write] :blue[text] :violet[in]:gray[pretty] :rainbow[colors] and :blue-background[highlight] text. &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
        # st.session_state.context = ctx
        
        if(to_xywh_json == "" or to_xywh_json is None):
            # TODO 缓存逻辑失效
            print("未使用缓存")
            to_xywh_json = converte.convert_file(project_id, prompt, fileName, width, height)
        to_xywh_json_str = json.dumps(to_xywh_json, default=timeutil.json_serial, indent=4)
        st.code(f"""{to_xywh_json_str}""")
        # 无需清空
        # to_xywh_json = ""

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})