from io import BytesIO
from PIL import Image, ImageEnhance,ImageFilter
import streamlit as st
# st.beta_set_page_config(page_title="Online Image Editor")

st.set_page_config(
    page_title="Online Image Editor",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="auto",
)


# ======================== This  section will remove the hamburger and watermark and footer and header from streamlit ===========
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}
            footer:after {
                            content:'\u00A9 Rahul-AkaVector. All rights reserved.'; 
	                        visibility: visible;
	                        display: block;
	                        position: relative;
	                        #background-color: red;
	                        padding: 5px;
	                        top: 2px;
                        }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ======================== This  section will remove the hamburger and watermark and footer and header from streamlit ===========

# -------------------------------------------------- ACTUAL CODE -------------------------------------------------------
def apply_image_modifications(image, color_change, rotation, mirror ,brightness, colour , contrast , sharpness, blur, gaussian_blur , contour, detail , edge_enhance , ultra_edge_enhance ,find_edges , sharp , smooth ,ultra_smooth, grayscale):

    modified_image = image.convert("RGB")
    modified_image = modified_image.convert("P", palette=Image.ADAPTIVE, colors=color_change)

    modified_image = modified_image.rotate(rotation)

    if mirror:
        modified_image = modified_image.transpose(Image.FLIP_LEFT_RIGHT)
    #crop

    # -------------------- Enhancement --------------------------

    modified_image = modified_image.convert("RGB")

    modified_image = ImageEnhance.Brightness(modified_image)
    modified_image = modified_image.enhance(brightness)

    modified_image = ImageEnhance.Color(modified_image)
    modified_image = modified_image.enhance(colour)

    modified_image = ImageEnhance.Contrast(modified_image)
    modified_image = modified_image.enhance(contrast)

    modified_image = ImageEnhance.Sharpness(modified_image)
    modified_image = modified_image.enhance(sharpness)

    # ---------------------- Filters ------------------------------
    modified_image = modified_image.convert("RGB")

    if blur:
        modified_image  = modified_image.filter(ImageFilter.BLUR)
    if gaussian_blur:
        modified_image  = modified_image.filter(ImageFilter.GaussianBlur)
    if contour:
        modified_image  = modified_image.filter(ImageFilter.CONTOUR)
    if detail:
        modified_image  = modified_image.filter(ImageFilter.DETAIL)
    if edge_enhance:
        modified_image  = modified_image.filter(ImageFilter.EDGE_ENHANCE)
    if ultra_edge_enhance:
        modified_image  = modified_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    if find_edges:
        modified_image  = modified_image.filter(ImageFilter.FIND_EDGES)
    if sharp:
        modified_image  = modified_image.filter(ImageFilter.SHARPEN)
    if smooth:
        modified_image  = modified_image.filter(ImageFilter.SMOOTH)
    if ultra_smooth:
        modified_image  = modified_image.filter(ImageFilter.SMOOTH_MORE)
    if grayscale:
        modified_image = modified_image.convert("L")

    # -return image -------------------------------------------------
    return modified_image

def main():
    # ---------------------------------- Upload image ----------------------------------
    st.sidebar.markdown(
        "<h1 style='text-align: center;'>Upload An Image ☁️➡️</h1>",
        unsafe_allow_html=True)
    uploaded_file = st.sidebar.file_uploader(" " , type=["jpg", "jpeg"])


    st.title("ONLINE IMAGE EDITOR 🤩🤩🤩")
    st.markdown("<p style='text-align: right;'>by&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VECTOR 💻👨‍💻</p>", unsafe_allow_html=True)
    st.text("""An online image editor is a user-friendly web-based tool that empowers users to edit and enhance their images
effortlessly.🎨✨ With intuitive features and a user-friendly interface, it enables individuals to resize, crop, apply
filters, add text, and make various adjustments to their images, all within a convenient online platform. 🖼️💻Whether you're
an amateur photographer or a social media enthusiast, an online image editor provides a hassle-free solution for quick
and efficient image editing, allowing you to unleash your creativity and achieve professional-looking results in just
a few simple steps 🌟📸.""")



    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.sidebar.image(image, caption='Original Image 📷', use_column_width=True)

        st.sidebar.markdown(
            "<h1 style='text-align: center;'>Utility ⚙️</h1>",
            unsafe_allow_html=True )
        # ------------------------------------------------------------------
        color_change = st.sidebar.slider("Color Change", 1, 255, 127)
        rotation = st.sidebar.slider("Rotation", -180, 180, 0)
        mirror = st.sidebar.checkbox("Mirror")

        st.sidebar.markdown(
            "<h1 style='text-align: center;'>Enhancement 🌟</h1>",
            unsafe_allow_html=True)
        # ==============================================================
        brightness_enhance = st.sidebar.slider("Brightness", 0.0, 4.0, 1.0)
        colour_enhance = st.sidebar.slider("Colour", 0.0, 4.0, 1.0)
        contrast_enhance = st.sidebar.slider("Contrast", 0.0, 4.0, 1.0)
        sharpness_enhance = st.sidebar.slider("Sharpness", 0.0, 4.0, 1.0)
        st.sidebar.markdown(
            "<h1 style='text-align: center;'>Filters 🏞️</h1>",
            unsafe_allow_html=True)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        blur = st.sidebar.checkbox("Blur")
        gaussian_blur = st.sidebar.checkbox("Gaussian Blur")
        contour = st.sidebar.checkbox("Contour")
        detail = st.sidebar.checkbox("Detail")
        edge_enhance = st.sidebar.checkbox("Edge Enhance")
        ultra_edge_enhance = st.sidebar.checkbox("Ultra Edge Enhance")
        find_edges = st.sidebar.checkbox("Find Edges")
        sharp = st.sidebar.checkbox("Sharp")
        smooth = st.sidebar.checkbox("Smooth")
        ultra_smooth = st.sidebar.checkbox("Ultra Smooth")
        grayscale = st.sidebar.checkbox("Grayscale")

        # ----------------------------------- modify image function ------------------------------
        modified_image = apply_image_modifications(image, color_change, rotation, mirror, brightness_enhance,colour_enhance, contrast_enhance, sharpness_enhance,blur,gaussian_blur , contour, detail , edge_enhance , ultra_edge_enhance ,find_edges , sharp , smooth ,ultra_smooth, grayscale )

        # =========================== Displaying the modified image to right side of website ================
        st.header("Your Modified Image 📂")
        st.header(" ")
        st.image(modified_image, caption='Modified Image 🔧', use_column_width=True)

        # ------------------- saving --------------------
        if st.button("Done Editing ? ✅"):

            tmp_file = BytesIO()
            modified_image.save(tmp_file, format='JPEG')

            headers = {
                'Content-Disposition': 'attachment; filename=modified_image.jpg',
                'Content-Type': 'image/jpeg'
            }

            file_data = tmp_file.getvalue()

            st.download_button(label="Download Your Edit ⬇️", data=file_data, file_name="modified_image.jpg",
                               mime='image/jpeg')


if __name__ == "__main__":
    main()
