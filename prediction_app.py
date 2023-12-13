import pickle
import customtkinter
import pandas as pd
import tkinter

with open("tree_model.pkl", "rb") as file:
    loaded_tree_model = pickle.load(file)


def make_predictions():
    try:
        user_input_data = {
            "reason_type_1": [int(entry_reason_type_1.get())],
            "reason_type_2": [int(entry_reason_type_2.get())],
            "reason_type_3": [int(entry_reason_type_3.get())],
            "reason_type_4": [int(entry_reason_type_4.get())],
            "reason_type_5": [int(entry_reason_type_5.get())],
            "reason_type_6": [int(entry_reason_type_6.get())],
            "reason_type_7": [int(entry_reason_type_7.get())],
            "reason_type_8": [int(entry_reason_type_8.get())],
            "reason_type_9": [int(entry_reason_type_9.get())],
            "reason_type_10": [int(entry_reason_type_10.get())],
            "reason_type_11": [int(entry_reason_type_11.get())],
            "reason_type_12": [int(entry_reason_type_12.get())],
            "reason_type_13": [int(entry_reason_type_13.get())],
            "reason_type_14": [int(entry_reason_type_14.get())],
            "reason_type_15": [int(entry_reason_type_15.get())],
            "reason_type_16": [int(entry_reason_type_16.get())],
            "reason_type_17": [int(entry_reason_type_17.get())],
            "reason_type_18": [int(entry_reason_type_18.get())],
            "reason_type_19": [int(entry_reason_type_19.get())],
            "reason_type_21": [int(entry_reason_type_21.get())],
            "reason_type_22": [int(entry_reason_type_22.get())],
            "reason_type_23": [int(entry_reason_type_23.get())],
            "reason_type_24": [int(entry_reason_type_24.get())],
            "reason_type_25": [int(entry_reason_type_25.get())],
            "reason_type_26": [int(entry_reason_type_26.get())],
            "reason_type_27": [int(entry_reason_type_27.get())],
            "Transportation Expense": [int(entry_transportation.get())],
            "Distance to Work": [int(entry_distance.get())],
            "Age": [int(entry_age.get())],
            "Daily Work Load Average": [float(entry_work_load.get())],
            "Body Mass Index": [int(entry_bmi.get())],
            "Education": [int(entry_education.get())],
            "Children": [int(entry_children.get())],
            "Pets": [int(entry_pets.get())],
        }

        predictions = loaded_tree_model.predict(pd.DataFrame(user_input_data))
        if predictions == 0:
            tkinter.messagebox.showinfo(
                title="Prediction",
                message=f"Results is: {predictions}. Excessively absent",
            )
        else:
            tkinter.messagebox.showinfo(
                title="Prediction",
                message=f"Results is: {predictions}. Moderately absent ",
            )

    except Exception as e:
        tkinter.messagebox.showerror("Error", str(e))


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x800")
app.title("Predictor")


scrollable_frame = customtkinter.CTkScrollableFrame(master=app, width=200, height=200)
scrollable_frame.pack(fill="both", expand=True)


scroll_frame_content = customtkinter.CTkFrame(master=scrollable_frame)

entry_reason_type_1 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_1"
)
entry_reason_type_1.pack(pady=5, padx=5)

entry_reason_type_2 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_2"
)
entry_reason_type_2.pack(pady=5, padx=5)

entry_reason_type_3 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_3"
)
entry_reason_type_3.pack(pady=5, padx=5)

entry_reason_type_4 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_4"
)
entry_reason_type_4.pack(pady=5, padx=5)

entry_reason_type_5 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_5"
)
entry_reason_type_5.pack(pady=5, padx=5)

entry_reason_type_6 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_6"
)
entry_reason_type_6.pack(pady=5, padx=5)

entry_reason_type_7 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_7"
)
entry_reason_type_7.pack(pady=5, padx=5)

entry_reason_type_8 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_8"
)
entry_reason_type_8.pack(pady=5, padx=5)

entry_reason_type_9 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_9"
)
entry_reason_type_9.pack(pady=5, padx=5)

entry_reason_type_10 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_10"
)
entry_reason_type_10.pack(pady=5, padx=5)

entry_reason_type_11 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_11"
)
entry_reason_type_11.pack(pady=5, padx=5)

entry_reason_type_12 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_12"
)
entry_reason_type_12.pack(pady=5, padx=5)

entry_reason_type_13 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_13"
)
entry_reason_type_13.pack(pady=5, padx=5)

entry_reason_type_14 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_14"
)
entry_reason_type_14.pack(pady=5, padx=5)

entry_reason_type_15 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_15"
)
entry_reason_type_15.pack(pady=5, padx=5)

entry_reason_type_16 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_16"
)
entry_reason_type_16.pack(pady=5, padx=5)

entry_reason_type_17 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_17"
)
entry_reason_type_17.pack(pady=5, padx=5)

entry_reason_type_18 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_18"
)
entry_reason_type_18.pack(pady=5, padx=5)

entry_reason_type_19 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_19"
)
entry_reason_type_19.pack(pady=5, padx=5)

entry_reason_type_21 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_21"
)
entry_reason_type_21.pack(pady=5, padx=5)

entry_reason_type_22 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_22"
)
entry_reason_type_22.pack(pady=5, padx=5)

entry_reason_type_23 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_23"
)
entry_reason_type_23.pack(pady=5, padx=5)

entry_reason_type_24 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_24"
)
entry_reason_type_24.pack(pady=5, padx=5)

entry_reason_type_25 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_25"
)
entry_reason_type_25.pack(pady=5, padx=5)

entry_reason_type_26 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_26"
)
entry_reason_type_26.pack(pady=5, padx=5)

entry_reason_type_27 = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="reason_type_27"
)
entry_reason_type_27.pack(pady=5, padx=5)

entry_transportation = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Transportation Expense"
)
entry_transportation.pack(pady=5, padx=5)

entry_distance = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Distance to Work"
)
entry_distance.pack(pady=5, padx=5)

entry_age = customtkinter.CTkEntry(master=scroll_frame_content, placeholder_text="Age")
entry_age.pack(pady=5, padx=5)

entry_work_load = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Daily Work Load Average"
)
entry_work_load.pack(pady=5, padx=5)

entry_bmi = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Body Mass Index"
)
entry_bmi.pack(pady=5, padx=5)

entry_education = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Education"
)
entry_education.pack(pady=5, padx=5)

entry_children = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Children"
)
entry_children.pack(pady=5, padx=5)

entry_pets = customtkinter.CTkEntry(
    master=scroll_frame_content, placeholder_text="Pets"
)
entry_pets.pack(pady=5, padx=5)

scroll_frame_content.pack(fill="both", expand=True)


run_button = customtkinter.CTkButton(
    master=scroll_frame_content,
    text="Predict",
    fg_color=("#A663CC"),
    hover_color=("#65B891"),
    command=make_predictions,
)
run_button.pack(pady=20, padx=10)

app.mainloop()
