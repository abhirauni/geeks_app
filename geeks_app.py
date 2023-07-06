import streamlit as st

st.title("Welcome to IITK")                         # Title
st.header("Welcome in Maths Department")            # Header
st.subheader("By Abhishek Rauniyar")                # SubHeader
st.text('In M.Sc. Maths Department')                # Text


st.header("Markdown")
st.markdown("# Hi")                                 # Markdown
st.markdown("## Hi")
st.markdown("### Hi")


st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
st.exception(ZeroDivisionError('Div not possible'))


st.subheader("Help")
st.help(ZeroDivisionError)

st.subheader('Write')
st.write("range(1,10)")
st.write(range(1,10))
st.write("1*2*3")
st.write(1*2*3)

st.subheader("Code")
st.code('x=10\n'
        'for i in range(x):\n'
        '\tprint(i)')
#st.code(i  for i in range(10))

st.subheader('Checkbox')
st.checkbox('Male')
if(st.checkbox('Adult')):
        st.write("You are an adult.")

st.subheader("RadioButton")
radioButon=st.radio('Select :',('Male',"Female","Other"))
if(radioButon=='Male'):
        st.write('You are a Male.')
elif(radioButon=='Female'):
        st.write('You are a Female.')
elif(radioButon=='Other'):
        st.write('You are a Other Gender.')


st.subheader('Select Box')
selectbox=st.selectbox("Data Science : ",['Data Analysis','Machine Learning','Deep Learning','EDA','Statistics','Image Processing',
                                          'Natural Language Processing','Excel','Web Scrapping','Tableu','Python','Library','Data Toolkit'])
st.write("You have selected : ",selectbox)



st.subheader('Multiselect Box')
multiselbox=st.multiselect("Data Science : ",['Data Analysis','Machine Learning','Deep Learning','EDA','Statistics','Image Processing',
                                          'Natural Language Processing','Excel','Web Scrapping','Tableu','Python','Library','Data Toolkit'])
st.write("You have selected : ",multiselbox)
st.write("You have selected : ",len(multiselbox),"courses")


st.subheader("Button")
if(st.button("Click Me")):
        st.write("Thanks For Clicking Me.")

st.subheader("Slider")
vol=st.slider("Select the volume",0,100,step=1)
st.write("Volume is : ",vol)

st.subheader("Text Input")
usrname=st.text_input("Username :")
password=st.text_input("Password :",type='password')


st.subheader("Text Area")
st.text_area("Write Something Intersting About Yourselfs.")


st.subheader("Input Number")
st.number_input("Select Your Age",18,110)


st.subheader("Input Date")
st.date_input("Date")

st.subheader("Input Time")
st.time_input("Time")


