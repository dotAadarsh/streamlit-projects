import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(page_title='Sieve of Eratosthenes')
st.header('Visualization of Sieve of Eratosthenes')

code_c_file = open("programs/prime.c","r+") 
code_c = code_c_file.read()

code_cpp_file = open("programs/prime.cpp","r+") 
code_cpp = code_cpp_file.read()

code_python_file = open("programs/prime.py","r+") 
code_python = code_python_file.read()

code_java_file = open("programs/prime.java","r+") 
code_java = code_java_file.read()

code_js_file = open("programs/prime.js","r+") 
code_js = code_js_file.read()

with st.sidebar:
    choice = st.selectbox('In which language you want to view the code?', options= ['C','C++','Java','Python','JavaScript'])
    st.info(f'Scroll to view the code 👉')
    st.subheader('References')
    st.markdown('''
    - Sieve of Eratosthenes - [Wiki](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- Sieve of Eratosthenes | Journey into cryptography - [YT](https://youtu.be/klcIklsWzrY)
- The Sieve of Eratosthenes – How Fast Can WeCompute a Prime Number Table? [Research Paper](https://www.researchgate.net/publication/230595538_The_Sieve_of_Eratosthenes_--_How_Fast_Can_We_Compute_a_Prime_Number_Table)
''')

def prime(n):

    list_columns = [0, n-1]
    prime = [True for i in range(n+1)]
    p = 2 
    loop_count=0

    #df = pd.DataFrame(prime, columns=list_columns)
   # st.table(df)

    col1, col2 = st.columns(2)

    with col1:
        st.info('Change of the boolean Value over different iterations 👇')
        with st.expander("Initial state"):
            df = pd.DataFrame(prime	)
            st.table(df)
        while(p*p <= n) :
            if(prime[p]==True):
                for i in range(p*p, n+1, p):
                    prime[i] = False
                loop_count +=1
                with st.expander(f'Change at iteration: {loop_count}', expanded=True):
                    df = pd.DataFrame(prime) # Table Creation
                    df.columns =['Value'] 
                    
                    st.table(df.style.highlight_min(color= '#F9D923'))
            p += 1

    with col2: 
        st.markdown('''
        **Given a number n, print all primes smaller than or equal to n**
The `sieve of Eratosthenes` is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so.
- Let us take an example when n = 50. So we need to print all prime numbers smaller than or equal to 50.
- We create a list of all numbers from 2 to 50.
- According to the algorithm we will mark all the numbers which are divisible by 2 and are greater than or equal to the square of it.
- Now we move to our next unmarked number 3 and mark all the numbers which are multiples of 3 and are greater than or equal to the square of it.
- We move to our next unmarked number 5 and mark all multiples of 5 and are greater than or equal to the square of it.
- We continue this process  until the conditon becomes false.
- So the prime numbers are the unmarked ones.
_**Time Complexity:** O(n*log(log(n)))_
_**Auxiliary Space:** O(n)_
''')
        st.write(f"The Loop has ran `{loop_count}` times")		
        total_prime = 0
        prime_final = []
        for p in range(2, n+1):
            if prime[p]:
                prime_final.append(p)
                total_prime+=1
        st.write(f'Number of primes: `{total_prime}`')
        df = pd.DataFrame(prime_final)
        df.columns =['Value'] 
        st.table(df)


if __name__ == '__main__':
     n = st.slider("Slide to choose the number", 2, 100, value=23)
     with st.expander("sieve of Eratosthenes | pseudocode"):
         pseudo_file = open("programs/prime.txt","r+") 
         pseudo = pseudo_file.read()
         st.code(pseudo)

     prime(n)
     if choice == 'C':
            st.code(code_c, language="C")
     elif choice == 'C++':
            st.code(code_cpp, language="cpp")    
     elif choice ==  'Java':
            st.code(code_java, language="java")    
     elif choice == 'Python':
            st.code(code_python, language="python")            
     elif choice == 'JavaScript':
            st.code(code_js, language="javascript")    

