# Image Text Extractor

Upload an image, get all the OCR'd text out of it — no field-mapping, just
the raw extracted values. Deployable as a free website via Streamlit
Community Cloud, hooked up to a GitHub repo.

## Files
- `streamlit_app.py` — the web app
- `requirements.txt` — Python packages
- `packages.txt` — system package (Tesseract OCR engine) for the hosting server

## 1. Put this on GitHub
1. Go to https://github.com/new and create a new repository (e.g. `image-text-extractor`). Public is fine and free.
2. Upload these three files (`streamlit_app.py`, `requirements.txt`, `packages.txt`) to the repo — either drag-and-drop them on the GitHub website ("Add file" → "Upload files"), or via git:
   ```
   git clone https://github.com/YOUR_USERNAME/image-text-extractor.git
   cd image-text-extractor
   # copy the three files in here
   git add .
   git commit -m "Initial app"
   git push
   ```

## 2. Deploy for free on Streamlit Community Cloud
1. Go to https://share.streamlit.io and sign in with your GitHub account.
2. Click "New app".
3. Pick your repo, branch (`main`), and set the main file path to `streamlit_app.py`.
4. Click "Deploy".

Streamlit Cloud automatically reads `requirements.txt` (Python packages) and
`packages.txt` (system packages like Tesseract) and installs them for you.

After a minute or two, you'll get a public URL like:
`https://your-app-name.streamlit.app`

That link works from any device — phone, another PC, anywhere — no
installation needed on the client side.

## 3. Using it
Open the URL, upload an image, and the extracted text appears on the page
with a "Download as .txt" button.

## Notes
- Free Streamlit Cloud apps "sleep" after a period of inactivity and take a
  few seconds to wake up on the next visit — that's normal.
- If OCR looks jumbled for a particular image, try `--psm 3` instead of
  `--psm 6` in `streamlit_app.py` (line with `pytesseract.image_to_string`),
  or crop the image to just the text before uploading.
