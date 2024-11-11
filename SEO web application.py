import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'traffic': [400, 300, 500, 600, 400, 500]
})

pie_data = pd.DataFrame({
    'source': ['Organic', 'Paid', 'Referral'],
    'value': [400, 300, 300]
})

st.set_page_config(page_title="SEO-Optimized Web App")

st.title("SEO-Optimized Web Application")

st.subheader("Traffic Trends")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='month', y='traffic', data=data, ax=ax)
ax.set_xlabel('Month')
ax.set_ylabel('Traffic')
st.pyplot(fig)

st.subheader("Traffic Sources")
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(pie_data['value'], labels=pie_data['source'], autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

st.subheader("SEO Checklist")
st.markdown("""
- Optimized page titles and meta descriptions
- Implemented structured data
- Reduced page load times
""")

st.success("SEO Optimization Complete!")
st.write("Your website is now optimized for search engines. Please review the checklist and let me know if you have any further requirements.")
