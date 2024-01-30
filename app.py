import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

st.set_page_config(layout='wide')

lottie_assets = {
    'coder': 'https://lottie.host/a00519a6-d16a-4a93-91c2-3314df555467/2NCinvu9GQ.json'
}
images_paths = {
    'project1': '',
    'idrica_logo': 'https://media.licdn.com/dms/image/C4D0BAQF8s5k4ek7wuw/company-logo_200_200/0/1630549593890/go_aigua_logo?e=2147483647&v=beta&t=wpid4IqGQwP83oYYsy_XJlEhemcsbl-wC9jjmhf98cc',
    'nexus_integra_logo': 'https://media.licdn.com/dms/image/C4D0BAQFKE6BEF9PZjA/company-logo_200_200/0/1630532228233/nexusintegra_logo?e=2147483647&v=beta&t=maENu7eeJN-rClOfcjPAZYal8j4wm810IXRIFgET8wI',
    'wola_logo': 'https://media.licdn.com/dms/image/C4D0BAQGXaLjsuDV5xw/company-logo_200_200/0/1630509827807?e=2147483647&v=beta&t=o3y-aphAtPrmrnLIpEs6L072iEdYyRpH_wFdZTrBEVw',
    'linkedin_pfp': 'https://media.licdn.com/dms/image/D4E03AQFLIP0zYgSjmg/profile-displayphoto-shrink_800_800/0/1673424451844?e=1712188800&v=beta&t=4pkilKmK5IAwf1cOCRVTdefZlwbQMoXQ46Qfmw7SYAA',
    'cnn_weather': ...,
    'price_predictor_image': ...,
    'upv': 'https://media.licdn.com/dms/image/C4D0BAQFi7R3IyJyZhw/company-logo_100_100/0/1632842290836/upv_logo?e=1714608000&v=beta&t=ztS9gw9MGHlZm6QR3xlF7y7fSaIEY0DPNARPv-KUyZA',
    'coursera': 'https://media.licdn.com/dms/image/C4D0BAQGexnfBxeEG-g/company-logo_100_100/0/1630530042036/coursera_logo?e=1714608000&v=beta&t=LozTIh7NeTGoQQATPWA7t0gos8XdL0yqgv_JyHjLLJo',
    'udemy': 'https://media.licdn.com/dms/image/C4D0BAQFQr9e68bBOPQ/company-logo_100_100/0/1630536914848/udemy_logo?e=1714608000&v=beta&t=2A0jkOOhpG1aQwscsHtKNOv6QxWpMCNPMRs0AGk63SE',
    'cnn-app': './images/labels_cnn.png',
    'lstm-app': './images/lstm_predictor.png',
    'smart-battery-manager': 'https://camo.githubusercontent.com/e2130d8287111292c8e3145103d3d5a1f0d59230470b6aac0e0f727fd34fdb50/68747470733a2f2f692e696d6775722e636f6d2f553350556943532e706e67',
}

contact_form = """
<form action="https://formsubmit.co/ricardo.gomez.aldaravi@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
""", unsafe_allow_html=True)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        st.error('Failed to load Lottie asset from {}'.format(url))
        return None
    else:
        return r.json()

def get_lotie_asset(asset_name: str):
    asset_url = lottie_assets.get(asset_name)
    if asset_url is None:
        st.error('No Lottie asset named "{}" found'.format(asset_name))
        return None
    asset = load_lottie_url(asset_url)
    return st_lottie(asset)

col1, col2 = st.columns(2)
with col1:
    st.write('##')
    image, text = st.columns([2, 20])
    with image:
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="{}" style="border-radius: 50%; width: 80px; height: 80px;">
            </div>
            """.format(images_paths['linkedin_pfp']),
            unsafe_allow_html=True
        )
    with text:
        st.title('Ricardo Gómez-Aldaraví Sotos')
    st.subheader('Python Developer')

    lang = option_menu(
        menu_title = None,
        options = ['Spanish', 'English'],
        orientation = 'horizontal',
        menu_icon=None
    )

    if lang == 'English':
        st.markdown(
            """
            Industrial Engineer, specializing in electronics. Currently working on energy efficiency and optimization projects using Python.

            I have been programming in Python for ~3 years in data analysis/process optimization applications, I know well the Data Science stack and good coding practices. Among others, I am proficent in the following technologies

            - Data manipulation (Pandas)
            - Data analysis and visualization (Plotly, matplotlib, seaborn...)
            - Linear programming optimization (Pyomo)
            - Artificial Intelligence (Tensorflow, Pytorch)
            - SQL queries
            - Use of API Rest services
            - Creation and maintenance of Python packages
            - Deploy models or services using Docker (Streamlit, Gradio, FastAPI)

            I have certificates of courses that can accredit this knowledge, as well as personal projects that make use of these technologies.

            I like working in teams, especially in interdisciplinary teams where I can learn a lot from the people around me. I am not afraid to present new ideas and I believe I can bring a lot to the company that gives me the opportunity to grow with them.
            """
        )
    elif lang == 'Spanish':
        st.markdown(
            """
            Ingeniero Industrial, especialización en electrónica. Actualmente trabajando en proyectos de eficiencia y optimización energética empleando Python.

            Llevo ~3 años programando en Python en aplicaciones de análisis de datos/optimización de procesos, conozco bien el stack de Data Science y buenas prácticas de código. Entre otros, conozco bien las siguientes tecnologías

            - Manipulación de datos (Pandas)
            - Análisis y visualización de datos (Plotly, matplotlib, seaborn...)
            - Optimización mediante programación lineal (Pyomo)
            - Inteligencia artificial (Tensorflow, Pytorch)
            - SQL queries
            - Uso de servicios API Rest
            - Creación y mantenimiento de paquetes Python
            - Deploy de modelos o servicios mediante Docker (Streamlit, Gradio, FastAPI)

            Dispongo de certificados de cursos que pueden acreditar estos conocimientos, así como proyectos personales que hacen uso de estas tecnologías.

            Me gusta trabajar en equipo, en especial en equipos interdisciplinares en los que puedo aprender muchísimo de la gente a mi alrededor. No tengo miedo a presentar ideas nuevas y creo que puedo aportar mucho a la empresa que me de la oportunidad de crecer con ellos.
            """
        )
    
with col2:
    get_lotie_asset('coder')
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <a href="https://www.linkedin.com/in/ricardogomez-al/" target="_blank" data-toggle="tooltip" data-placement="top" title="LinkedIn">
                <i class="bi bi-linkedin" style="font-size: 3rem; margin-right: 20px;"></i>
            </a>
            <a href="https://github.com/RikiSot" target="_blank" data-toggle="tooltip" data-placement="top" title="GitHub">
                <i class="bi bi-github" style="font-size: 3rem; margin-left: 20px;"></i>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Experience', 'Projects', 'Education and Certifications', 'Contact'],
        icons = ['person', 'code-slash', 'mortarboard-fill','chat-left-text-fill'],
        orientation = 'horizontal'
    )
    
if selected == 'Experience':

    st.write('---')

    with st.container():
        st.markdown("<h1 style='text-align: center; color: white;'><i class='bi bi-briefcase'></i> Work Experience</h1>", unsafe_allow_html=True)
        st.write('##')

        with st.container():
            image, text = st.columns([1, 20])
            with image:
                st.image(images_paths['idrica_logo'])
            with text:
                st.subheader("[Idrica](http://www.idrica.com)")
            st.markdown("Python developer, Valencia, Spain (01/2023 - Present)")
            st.markdown("""
            - Research and find new methods to improve energy efficiency for water facilities
            - Design data dashboards and relevant KPIs
            - Standalone development of a smart pump scheduling algorithm using AI and optimization techniques
            """)
            st.write('---')

        with st.container():
            image, text = st.columns([1, 20])
            with image:
                st.image(images_paths['nexus_integra_logo'])
            with text:
                st.subheader("[Nexus Integra](https://nexusintegra.io/)")
            st.markdown("Junior Engineer, Valencia, Spain (04/2021 - 01/2023)")
            st.markdown("""
            - Data Analysis with Python
            - SQL queries
            - SCADA systems design
            - Data Visualization
            - Webscraping and API REST usage
            - Building and maintaining Python packages
            """)
            st.write('---')

        with st.container():
            image, text = st.columns([1, 20])
            with image:
                st.image(images_paths['wola_logo'])
            with text:
                st.subheader("[Water Online Analysis](https://www.biosensores.com/water-online-analysis-europe-wola-sl/)")
            st.markdown("Intern Electronics Engineer, Water Online Analysis, Castellón, Spain (07/2020 - 10/2020)")
            st.markdown("""
            - Participation in a project under PRIMA program supported by EU
            - PLC's automation
            - Database management with .NET libraries and C#
            """)
            st.write('---')

        
if selected == 'Projects':
    st.markdown("<h1 style='text-align: center; color: white;'><i class='bi bi-gear-fill'></i> Projects</h1>", unsafe_allow_html=True)
    st.write('##')
    
    with st.container():
        st.subheader("""LSTM Iberian Energy Prices Predictor""")
        st.markdown("""Long Short-Term Memory (LSTM) neural network using PyTorch to predict energy prices in the Iberian market.""")
        st.markdown("""
        Stack used:  
        - Pytorch
        - Docker
        - Gradio
        - Pandas

        **Model Architecture**
                    
        The LSTM model is constructed with configurable hyperparameters for the number of hidden units, layers, and dropout rate.
        The PyTorch framework facilitates the creation of the LSTM layers and the linear regression layer for output.
        The model takes a time series input of 3 * 24 elements of hourly data scaled between 0-1 for all columns, so the shape of the input is [BatchSize, 3 * 24, N features (20)].            

                    
        **Training**
                    
        The model is trained using 2023 data from REE. Data is previously preprocessed by:

        Adding categorical variables in one hot encoding from datetime info for each date. Features added are:
        Day of the weekday (Monday-Sunday)
        Day of the month
        Month
        Create sequences of 3 * 24 elements for each feature of the data (value of the time series and categorical variables).
        Training involves:

        - Preprocessing and loading the data using custom DataLoader instances.
        - Defining the LSTM model architecture with the specified hyperparameters.
        - Using MSE as loss function and the Adam optimizer.
        - Running the training loop for a set number of epochs, evaluating on the test set at each epoch.
        - Process is supervised using TensorBoard for logging the loss and a plot of evaluation data vs predictions.
        - An early stopping callback stops the training if validation loss stops improving after a certain number of epochs
                    
        Screenshot of the live app:
        """)
        st.image(images_paths['lstm-app'], caption='Screenshot of the live app. You can click on the link below to test it')

        git, live = st.columns(2)

        with git:
            st.markdown("""
                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <a href="https://github.com/RikiSot/LSTMEnergyPricePrediction" target="_blank" data-toggle="tooltip" data-placement="top" title="GitHub">
                        <i class="bi bi-github" style="font-size: 3rem; margin-left: 20px;"></i>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        with live:
            st.markdown("""
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
                    <a href="https://huggingface.co/spaces/RikiSot/energy-price-predictor" target="_blank" data-toggle="tooltip" data-placement="top" title="Access the live app">
                    <i class="bi bi-play-circle" style="font-size: 3rem; margin-bottom: 10px;"></i>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        
    st.divider()
    st.write('##')

    with st.container():
        st.subheader("""CNN Weather Recognition API""")
        st.markdown("""Image recognition app for weather phenomenona images.  
        This is a project I made to experiment with CNN architectures and transfer learningf.
        I used transferred learning on models previously trained with ImageNet weights and compared some of the most used architectures to choose the best model.
        Finally I built an API to access the predictions in a simple way.
        """)
        st.markdown("""
        Stack used:  
        - Tensforflow
        - Pandas
        - FastAPI
        - Docker
                    
        Screenshot of some of the results during model building:
                    
        """)
        st.image(images_paths['cnn-app'], caption='Predictions vs Labels after training model')
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <a href="https://github.com/RikiSot/cnn-weather-recognition" target="_blank" data-toggle="tooltip" data-placement="top" title="GitHub">
                    <i class="bi bi-github" style="font-size: 3rem; margin-left: 20px;"></i>
                </a>
            </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.write('##')

    with st.container():
        st.subheader("""Smart battery manager (TFM)""")
        st.markdown("""Development of a battery management software using Big Data and Artificial Intelligence (Master's thesis)""")
        st.markdown("""
        Stack used:  
        - Tensforflow
        - Pandas

                    
        The purpose of this project is to control the batteries charge cycle of a house in a smart way in order to save energy and reduce the needed capacity of the batteries. Besides, increasing the charging-decision frequency can lead to better battery life expectancy as the batteries are less exposed to full charging cyles.

        Using big data and deep learning tools, it is possible to forecast electric consumption and compare the result to the power output from a solar panel array. The comparision will determine the behaviour of the charging profile of the batteries.

        The whole project can be reached at the public UPV repository (Spanish) RiuNet

        """)
        st.image(images_paths['smart-battery-manager'])

        git, live = st.columns(2)

        with git:
            st.markdown("""
                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                    <a href="https://github.com/RikiSot/smart-battery-manager" target="_blank" data-toggle="tooltip" data-placement="top" title="GitHub">
                        <i class="bi bi-github" style="font-size: 3rem; margin-left: 20px;"></i>
                    </a>
                </div>
            """, unsafe_allow_html=True)
        with live:
            st.markdown(f"""
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
                    <a href="https://riunet.upv.es/handle/10251/181879" target="_blank" data-toggle="tooltip" data-placement="top" title="UPV repository">
                        <img src="{images_paths['upv']}" style="max-width: 70%; height: auto;">
                    </a>
                </div>
            """, unsafe_allow_html=True)

            
if selected == 'Education and Certifications':
    st.write('## Education')
    st.write('##')
    
    education, certification = st.columns(2)
    img_dimensions = [2, 20]
    
    with education:
        with st.container():
            image, text = st.columns(img_dimensions)
            with image:
                st.image(images_paths['upv'])
            with text:
                st.markdown("""
                **Universitat Politècnica de València (UPV)**

                *Master's degree, Ingeniería industrial, especialización en electrónica* - 2019 - 2022
                """)

        with st.container():
            image, text = st.columns(img_dimensions)
            with image:
                st.image(images_paths['upv'])
            with text:
                st.markdown("""
                **Universitat Politècnica de València (UPV)**

                *Grado en Ingeniería en Tecnologías Industriales* - 2015 - 2019
                """)
                
    with certification:
        with st.container():
            image, text = st.columns(img_dimensions)
            with image:
                st.image(images_paths['coursera'])
            with text:
                st.markdown("""
                **DeepLearning.AI Deep Learning Specialization**
                
                [Credential](#https://www.coursera.org/account/accomplishments/specialization/certificate/VNSA3W2QJUAG)
                """)
        with st.container():
            image, text = st.columns(img_dimensions)
            with image:
                st.image(images_paths['coursera'])
            with text:
                st.markdown("""
                **Programa Especializado - IBM Data Science**
                
                [Credential](#https://www.coursera.org/account/accomplishments/specialization/certificate/F93GRNETWE5E)
                """)
        with st.container():
            image, text = st.columns(img_dimensions)
            with image:
                st.image(images_paths['udemy'])
            with text:
                st.markdown("""
                **Scrum Master + Liderar Equipos Scrum y Ágil**
                
                [Credential](#http://ude.my/UC-5e56e8fe-09ee-4c2a-900f-9fcd56628398)
                """)
                
        with st.container():
            image, text = st.columns(img_dimensions)
            with image:
                st.image(images_paths['udemy'])
            with text:
                st.markdown("""
                **Big Data con Apache Spark 3 y Python: de cero a experto**
                
                [Credential](#https://www.udemy.com/certificate/UC-9d604b2d-9d6b-40b0-a4eb-40211b0041a5/)
                """)
                
                
if selected == 'Contact':
    st.header('Escríbeme')
    st.write('##')
    st.write('##')
    st.markdown(contact_form, unsafe_allow_html=True)
        
if selected == 'Skills':
    with st.container():
        st.header('My Skills')
        st.write('##')
        col1, col2, col3 = st.columns(3)
        with col1:
            st_lottie('skill_animation_1')
            st.subheader('Skill 1')
        with col2:
            st_lottie('skill_animation_2')
            st.subheader('Skill 2')
        with col3:
            st_lottie('skill_animation_3')
            st.subheader('Skill 3')
