import tkinter as tk
from tkinter import filedialog
from sklearn.linear_model import LinearRegression
from PIL import Image, ImageTk
import csv
import os


class linearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("linear App")
        self.root.geometry("1080x720")
        self.widgets()

    def widgets(self):
        greeting = tk.Label(self.root, text="linear App", fg="black", font=("Arial", 16))
        greeting.place(x=10, y=10)

        self.frame1 = tk.Frame(self.root, width=500, height=500, bg="#001466")
        self.frame1.place(x=30, y=50)

        frame2 = tk.Frame(self.root, width=370, height=500, bg="#612180")
        frame2.place(x=700, y=10)

        frame2_text = tk.Label(frame2, text="INPUT", fg="white", font=("Arial", 20), bg="#612180")
        frame2_text.place(x=260, y=10)

        input_labels = ["rice varieties", "Soil quality", "temp", "fertilizer", "Pests"]
        self.input_entries = []

        for i, label_text in enumerate(input_labels):
            label = tk.Label(frame2, text=label_text, fg="white", font=("Arial", 14), bg="#612180")
            label.place(x=20, y=70 + i * 40)
            
            var = tk.StringVar()
            var.set("0")
            entry = tk.Entry(frame2, textvariable=var, font=("Arial", 14), bg="white")
            entry.place(x=120, y=70 + i * 40)

            self.input_entries.append(entry)

        frame3 = tk.Frame(self.root, width=1065, height=220, bg="#50E943")
        frame3.place(x=5, y=510)

        frame4 = tk.Frame(self.root, width=970, height=180, bg="#FFFFFF")
        frame4.place(x=55, y=560)

        open_image_button = tk.Button(frame2, text="Open Image", command=self.open_image, font=("Arial", 18), bg="#A577BB", fg="black")
        open_image_button.place(x=0, y=0)
        

        openfile_button = tk.Button(frame4, text="Click Me", command=self.open_file, font=("Arial", 18), bg="#87ceeb", fg="black")
        openfile_button.grid(row=0, column=0, pady=30, padx=120)

        predict_button = tk.Button(frame4, text="Predict", command=self.predict, font=("Arial", 18), bg="#A577BB", fg="black")
        predict_button.grid(row=0, column=1, pady=30, padx=120)

        self.predict_label = tk.Label(frame4, text="Predict: unknown", font=("Arial", 22), bg="#FFFFFF", fg="black")
        self.predict_label.grid(row=0, column=2, pady=30, padx=30)

        self.data = [
            #rice varieties = There are 5 rice varieties.
            #Soil quality = There are 3 types of soil quality: 0 is poor quality, 1 is medium quality, 2 is good quality.
            #temp = temperature in each item
            #fertilizer = Fertilizer is 0 means no fertilizer is applied, 1 means fertilizer is applied.
            #Pests = Pests are 0. No pests. 1 is there are pests
            ["rice varieties", "Soil quality", "temp", "fertilizer", "Pests", "produk"],
            [4, 1, 30, 1, 0, 2.5],
            [4, 0, 29, 1, 0, 2.5],
            [4, 1, 30, 1, 1, 1.3],
            [4, 1, 28, 0, 1, 2.5],
            [4, 2, 31, 0, 0, 2.3],
            [4, 0, 25, 1, 1, 2.2],
            [4, 0, 27, 1, 0, 0.5],
            [4, 1, 29, 0, 0, 0.9],
            [4, 2, 30, 0, 1, 2.2],
            [4, 2, 30, 1, 1, 2.2],
            [5, 1, 29, 1, 0, 2],
            [5, 1, 27, 1, 1, 2],
            [5, 0, 24, 0, 0, 0.3],
            [5, 1, 25, 1, 1, 0.5],
            [5, 2, 25, 0, 1, 2.3],
            [4, 0, 25, 1, 1, 2.5],
            [4, 0, 29, 0, 0, 2.3],
            [4, 2, 29, 0, 0, 2.2],
            [4, 1, 30, 0, 0, 0.5],
            [4, 1, 30, 1, 1, 2],
            [3, 1, 31, 1, 1, 1.9],
            [3, 1, 8, 0, 0, 0.5],
            [3, 0, 27, 1, 1, 0.7],
            [3, 0, 27, 1, 0, 0.2],
            [3, 2, 26, 0, 1, 0.7],
            [4, 1, 26, 1, 0, 0.8],
            [4, 0, 25, 1, 0, 1],
            [5, 1, 26, 1, 1, 1.4],
            [5, 1, 24, 0, 1, 1.3],
            [5, 2, 28, 0, 0, 1.5],
            [5, 0, 29, 1, 1, 2],
            [5, 0, 30, 1, 0, 1.9],
            [4, 1, 30, 0, 0, 2.1],
            [4, 2, 30, 0, 1, 1.5],
            [4, 2, 30, 1, 1, 1.8],
            [4, 1, 31, 1, 0, 0.5],
            [3, 1, 27, 1, 0, 0.9],
            [3, 0, 26, 0, 1, 1.2],
            [3, 1, 25, 1, 1, 1.6],
            [3, 2, 25, 0, 0, 1.7],
            [4, 0, 29, 1, 1, 1.7],
            [4, 0, 29, 0, 0, 1.8],
            [2, 2, 28, 0, 0, 1.5],
            [2, 1, 24, 0, 1, 1.5],
            [2, 1, 25, 1, 1, 2],
            [2, 1, 26, 1, 0, 2.2],
            [5, 1, 27, 0, 0, 0.5],
            [2, 0, 24, 1, 1, 1.3],
            [2, 0, 25, 1, 1, 0.8],
            [5, 2, 28, 0, 0, 2.3],
            [5, 1, 26, 1, 1, 2.5],
            [5, 0, 28, 1, 0, 2.5],
            [5, 1, 25, 1, 0, 1.8],
            [5, 1, 26, 0, 1, 0.9],
            [4, 2, 29, 0, 1, 0.4],
            [4, 0, 29, 1, 0, 1.3],
            [4, 0, 28, 1, 0, 1.8],
            [2, 1, 27, 0, 1, 1.4],
            [2, 2, 23, 0, 1, 0.7],
            [2, 2, 23, 1, 0, 1.8],
            [2, 1, 25, 1, 1, 2.1],
            [2, 1, 28, 1, 0, 1.3],
            [3, 0, 28, 0, 0, 1.1],
            [3, 1, 28, 1, 1, 1.1],
            [3, 2, 28, 0, 1, 1.4],
            [3, 0, 27, 1, 0, 1.2],
            [2, 0, 26, 0, 0, 1.5],
            [2, 2, 26, 0, 1, 1.6],
            [2, 1, 25, 0, 1, 1.1],
            [2, 1, 25, 1, 0, 2.5],
            [2, 1, 25, 1, 1, 2.3],
            [5, 1, 26, 0, 0, 2],
            [4, 0, 28, 1, 0, 1.9],
            [4, 0, 29, 1, 1, 1.4],
            [4, 2, 29, 0, 1, 2.5],
            [4, 1, 30, 1, 0, 2.9],
            [2, 0, 30, 1, 0, 2.5],
            [2, 1, 30, 1, 1, 0.8],
            [2, 1, 28, 0, 1, 1],
            [2, 2, 28, 0, 0, 1.5],
            [2, 0, 27, 1, 1, 1.9],
            [5, 0, 26, 1, 0, 1.5],
            [5, 1, 29, 0, 0, 1.2],
            [5, 2, 29, 0, 1, 3.2],
            [5, 2, 29, 1, 1, 3],
            [5, 1, 26, 1, 0, 1.3],
            [5, 1, 26, 1, 0, 1.2],
            [5, 0, 25, 0, 1, 2.1],
            [5, 1, 25, 1, 1, 2.1],
            [4, 2, 27, 0, 0, 2.8],
            [4, 0, 24, 1, 1, 2.5],
            [4, 0, 23, 0, 0, 2.3],
            [4, 2, 25, 0, 0, 1.9],
            [4, 1, 28, 0, 1, 1.5],
            [3, 1, 29, 1, 1, 1.1],
            [3, 1, 29, 1, 0, 2.1],
            [3, 1, 27, 0, 0, 2.1],
            [3, 0, 25, 1, 1, 2],
            [3, 0, 28, 1, 1, 2.7],
            [4, 2, 28, 0, 0, 3.1]
        ]
        

        self.update_frame1()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.open_new_window_image(file_path)
    
    def open_new_window_image(self, image_path):
        new_window = tk.Toplevel(self.root)
        new_window.title("Image Window")

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.load_data_from_csv(file_path)

    def predict(self):
        user_input = [float(entry.get()) for entry in self.input_entries[:4]]

        # Change from KNeighborsClassifier to LinearRegression
        linear_model = LinearRegression()

        X_train = [row[:-2] for row in self.data[1:]]
        y_train = [row[-1] for row in self.data[1:]]

        linear_model.fit(X_train, y_train)
        prediction = linear_model.predict([user_input])

        # Adjust the code for displaying the prediction
        predicted_value = round(prediction[0], 1)
        self.predict_label.configure(text=f"Predict: {predicted_value}")

        if 0 <= predicted_value <= 1.5:
            self.open_new_window_low_yield("low.png")
        elif 1.6 <= predicted_value <= 3.1:
            self.open_new_window_high_yield("high.png")



    def open_new_window_high_yield(self, image_path):
        new_window = tk.Toplevel(self.root)
        new_window.title("Image Window")

        # Use os.path.join to create the absolute path
        absolute_path = os.path.join(os.path.dirname(__file__), image_path)

        image = Image.open(absolute_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()

    def open_new_window_low_yield(self, image_path):
        new_window = tk.Toplevel(self.root)
        new_window.title("Image Window")

        # Use os.path.join to create the absolute path
        absolute_path = os.path.join(os.path.dirname(__file__), image_path)

        image = Image.open(absolute_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()

    def load_data_from_csv(self, csv_file):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                raw_data = [row for row in reader]

            headers = raw_data[0]

            self.data = [headers] + [[int(cell) if i < 4 else float(cell) for i, cell in enumerate(row)] for row in raw_data[1:]]

            self.update_frame1()
        except FileNotFoundError:
            print(f"Error: CSV file '{csv_file}' not found.")

    def update_frame1(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()

        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                label = tk.Label(self.frame1, width=10, height=1, text=str(value), bg="#FFFFFF", fg="black")
                label.grid(row=i, column=j, padx=10, pady=10)
                if i == 0:
                    label.configure(bg="#F1D3FF")


def main():
    root = tk.Tk()
    app = linearApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
