import streamlit as st


def main():
    st.title("Streamlit Photo App")
    col1, col2 = st.columns([1, 2])
    col1.markdown("# Ready!")

    with col2:
        camera_photo = st.camera_input("Take a photo")
        if camera_photo:
            st.image(camera_photo)
            col2.success("Photo taken succcesfully")


if __name__ == "__main__":
    main()