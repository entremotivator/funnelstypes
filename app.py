import streamlit as st

# App title and introductory text
st.title("Comprehensive Funnel Checklist & Management App")
st.write("""
Welcome to the Funnel Checklist & Management App! This tool will help you design, track, and optimize various marketing funnels.
From digital products to software funnels, use this checklist to ensure each element is aligned for success. Utilize additional tips,
notes, and resources to further enhance your funnel-building journey.
""")

# Sidebar for navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Choose a section:", ["Funnel Types", "Checklist Features", "Funnel Goals", "Notes & Tips", "FAQ & Resources", "Summary"])

# Funnel Types Section
if page == "Funnel Types":
    st.header("Main Funnel Types")
    st.write("""
    Below are common funnel types. Check each one relevant to your business needs, and view detailed descriptions and best practices for each.
    """)

    funnel_data = {
        "Digital Download Funnel": "For offering downloadable products like e-books, software, or digital courses. Key elements include strong calls-to-action and instant delivery options.",
        "Physical Product Funnel": "Ideal for e-commerce sales of tangible items. Focus on optimizing for conversions with upsell/downsell features.",
        "Event Funnel": "Designed for promoting live or virtual events. Should include registration forms, reminders, and post-event follow-up sequences.",
        "Membership Funnel": "Helps in building a subscription-based model, often for exclusive content. Essential features are retention strategies and loyalty rewards.",
        "Webinar Funnel": "Optimized to attract and convert webinar attendees. Key elements include registration, reminders, and a follow-up sales offer.",
        "Appointment Funnel": "Encourages visitors to schedule appointments. Often used in service-based businesses for consultations or meetings.",
        "Affiliate Funnel": "Targets affiliate marketers to promote products. Includes referral links and performance tracking.",
        "Course Funnel": "For selling online educational courses. Includes sections for previews, pricing, and payment options.",
        "Software Funnel": "Used to promote and sell software products. Focuses on free trials, feature showcases, and customer support.",
        "Wait List Funnel": "Builds anticipation for upcoming products. Collects contact info to notify potential customers when ready.",
        "Lead Magnet Funnel": "Offers a valuable freebie in exchange for contact information, often used as an entry point for other funnels."
    }

    selected_funnels = []
    for funnel, description in funnel_data.items():
        if st.checkbox(f"{funnel} - {description}"):
            selected_funnels.append(funnel)
            st.text_area(f"{funnel} Best Practices", f"Write best practices here for {funnel}", key=f"{funnel}_best_practices")

# Checklist Features Section
elif page == "Checklist Features":
    st.header("Essential Funnel Checklist Features")
    st.write("""
    Each funnel can be optimized with the following features. Use these checkboxes to track your progress, and read the descriptions for each item.
    """)

    features = {
        "A/B Testing": "Test multiple versions of your funnel to determine which one drives more conversions.",
        "Themes": "Apply different visual themes to enhance user experience and brand consistency.",
        "Email Segmentation": "Organize leads into targeted segments for personalized follow-ups.",
        "Copy": "Focus on persuasive, compelling copywriting to engage and convert leads.",
        "CTA": "Place strong, clear calls-to-action throughout the funnel to guide visitors.",
        "Upsells/Downsells": "Include additional offers to increase order value post-initial purchase.",
        "Close Sale": "Implement techniques to finalize the sale, such as limited-time offers or social proof.",
        "Order Bump": "Provide an extra offer at checkout to increase the overall transaction value.",
        "Builder": "Utilize a funnel builder tool to easily create and customize funnels.",
        "TO-C": "Include Terms and Conditions to set clear expectations with customers.",
        "Name Custom Link": "Create a unique URL to improve brand awareness and ease of access."
    }

    selected_features = []
    for feature, description in features.items():
        if st.checkbox(f"{feature} - {description}"):
            selected_features.append(feature)
            st.text_area(f"Implementation Tips for {feature}", f"Write implementation tips here for {feature}", key=f"{feature}_tips")

# Funnel Goals Section
elif page == "Funnel Goals":
    st.header("Set Specific Goals for Each Funnel")
    st.write("""
    For each selected funnel, set specific, measurable goals. This will help you track your progress and identify areas for improvement.
    """)

    for funnel in selected_funnels:
        st.subheader(f"Goals for {funnel}")
        st.number_input(f"Target Conversion Rate for {funnel}", min_value=0.0, max_value=100.0, step=0.1, key=f"{funnel}_conversion_rate")
        st.number_input(f"Monthly Leads Target for {funnel}", min_value=0, step=10, key=f"{funnel}_leads_target")
        st.number_input(f"Revenue Goal for {funnel} ($)", min_value=0.0, step=100.0, key=f"{funnel}_revenue_goal")

# Notes & Tips Section
elif page == "Notes & Tips":
    st.header("Additional Notes & Tips")
    st.write("""
    Use this section to jot down any additional notes, reminders, or strategies for each funnel or feature.
    """)

    for funnel in selected_funnels:
        st.subheader(f"Notes for {funnel}")
        st.text_area(f"Add notes or reminders for {funnel}", f"Write additional notes for {funnel}", key=f"{funnel}_notes")

    st.write("---")

    for feature in selected_features:
        st.subheader(f"Tips for {feature}")
        st.text_area(f"Best practices or strategies for {feature}", f"Write best practices for {feature}", key=f"{feature}_best_practices")

# FAQ & Resources Section
elif page == "FAQ & Resources":
    st.header("Frequently Asked Questions & Resources")
    
    st.subheader("Frequently Asked Questions")
    st.write("**Q: What is a funnel?**")
    st.write("A funnel is a series of steps designed to guide visitors towards a specific goal, such as a sale or lead.")
    
    st.write("**Q: How often should I test my funnels?**")
    st.write("Regular testing is recommended, especially during major promotions or new product launches.")
    
    st.write("**Q: How can I improve my conversion rates?**")
    st.write("Focus on clear CTAs, optimized copy, A/B testing, and audience segmentation.")

    st.subheader("Useful Resources")
    resources = {
        "ClickFunnels Blog": "https://blog.clickfunnels.com",
        "HubSpot Funnel Guide": "https://blog.hubspot.com/marketing/sales-funnel",
        "Neil Patel on Funnels": "https://neilpatel.com/blog/sales-funnel/",
        "A/B Testing Guide by Optimizely": "https://www.optimizely.com/optimization-glossary/ab-testing/"
    }
    for resource_name, url in resources.items():
        st.markdown(f"[{resource_name}]({url})")

# Summary Section
elif page == "Summary":
    st.header("Summary of Selected Items and Goals")
    
    if selected_funnels or selected_features:
        st.subheader("Selected Funnel Types")
        if selected_funnels:
            for funnel in selected_funnels:
                st.write(f"- **{funnel}**")
        else:
            st.write("No funnel types selected.")

        st.subheader("Selected Checklist Features")
        if selected_features:
            for feature in selected_features:
                st.write(f"- **{feature}**")
        else:
            st.write("No features selected.")
        
        st.subheader("Funnel Goals Summary")
        for funnel in selected_funnels:
            st.write(f"### {funnel} Goals")
            st.write(f"- Target Conversion Rate: {st.session_state.get(f'{funnel}_conversion_rate', 'Not set')}")
            st.write(f"- Monthly Leads Target: {st.session_state.get(f'{funnel}_leads_target', 'Not set')}")
            st.write(f"- Revenue Goal: ${st.session_state.get(f'{funnel}_revenue_goal', 'Not set')}")
    else:
        st.write("No selections made yet. Use the other tabs to choose funnel types, features, and set goals.")

# Closing notes
st.write("---")
st.write("""
### Next Steps
- Review your selected funnels, features, and goals.
- Visit the FAQ and Resources for guidance on further improving your funnel strategies.
- Regularly update this checklist as you refine and optimize your funnels.
""")
