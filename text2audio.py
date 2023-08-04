import tkinter as tk
import PyPDF2 
from tkinter import filedialog
from gtts import gTTS

# se crea una instancia de tk para abrir una ventana
window = tk.Tk()
# titulo de la ventana
window.title("PDF to Audio")
# tamano de la ventana L x A
window.minsize(400,200) 
window.maxsize(400,200)

# necesito un metodo que me permita hacer esto
def open_file_dialog():
    global selected_file
    # abre caja de dialogo para que selecciones el archivo
    pdf_file_path = filedialog.askopenfile()
    # verifica si se selecciono un archivo
    if pdf_file_path is not None:
        selected_file = pdf_file_path.name
        # label en frame para colocar el archivo y mostrarlo
        pdf_file_path_label.config(text=selected_file)
        return selected_file
    else:
        # label en frame que diga "No file selected."
        pdf_file_path_label.config(text="No file selected.")
        return ""
    
# necesito un metodo para extraer el contenido del pdf
def pdf_to_text():
    pdf_reader = PyPDF2.PdfReader(open(selected_file, "rb"))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        clean_text = text.strip().replace('\n',' ')
        print(clean_text)
    return text
    
# necesito un metodo para convertir de texto a audio
def text_to_audio():
    tts = gTTS(pdf_to_text(), lang="en")
    audio_file_path = filedialog.asksaveasfilename(
        title="Save file",
        filetypes=[("Mp3 files", "*.mp3"),
                   ("WAV files", "*.wav")],
        defaultextension=".mp3"
    )
    tts.save(audio_file_path)

# necesito el boton para abrir la caja de dialogo y seleccionar el archivo a cambiar
select_file_button = tk.Button(window, text="Select File", command=open_file_dialog)
select_file_button.pack()

# necesito ponerle un label Select File
selected_file_frame = tk.Frame(window)
selected_file_frame.pack()

pdf_file_path_label = tk.Label(selected_file_frame, text="No file selected.")
pdf_file_path_label.pack()

# necesito el boton para convertir el pdf en audio
convert_audio = tk.Button(window,text="Convert File", command=text_to_audio)
convert_audio.pack()

# necesito un boton para terminar la ejecucion y salir
quit_button = tk.Button(window, text="Exit", command=window.destroy)
quit_button.pack()

window.mainloop()