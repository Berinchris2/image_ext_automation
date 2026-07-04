import streamlit as st
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="Image Text Extractor", page_icon="🔎")

st.title("🔎 Image Text Extractor")
st.write("Upload a scanned/photographed record and get all the text out of it. "
         "No field-mapping — just the raw values, cleaned up a little.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "bmp", "tiff"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_container_width=True)

    with st.spinner("Reading text from image..."):
        # --psm 6 = assume a single uniform block of text; works well for
        # single rows / simple forms. Try --psm 3 (fully automatic) if a
        # particular image comes out garbled.
        text = pytesseract.image_to_string(image, config="--psm 6")

    st.subheader("Extracted text")
    if text.strip():
        st.text_area("Result", text.strip(), height=300)

        st.download_button(
            "Download as .txt",
            data=text.strip(),
            file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}_extracted.txt",
            mime="text/plain",
        )
    else:
        st.warning("No text was detected in this image. Try a clearer or higher-resolution photo.")

    with st.expander("Tips for better accuracy"):
        st.markdown(
            "- Higher-resolution images work much better than low-res photos.\n"
            "- Make sure the text is horizontal and not skewed/rotated.\n"
            "- Good lighting / contrast (dark text on light background) helps a lot.\n"
            "- If output looks jumbled, it may be a layout issue — try cropping to just the text block."
        )
else:
    st.info("👆 Upload an image to get started.")
