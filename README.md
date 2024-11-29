# Text Summarization Tool 🌟  

A clean and modern web application that uses AI to generate concise summaries from user-provided text. Built with Django for the backend and styled with a sleek, Apple-inspired frontend using Tailwind CSS.

---

## 🛠️ Features  

- **AI-Powered Summarization**: Generate precise summaries using the Hugging Face API.  
- **Minimalistic Design**: Inspired by Apple's design principles for a clean and modern user interface.  
- **Responsive Layout**: Works seamlessly across desktops, tablets, and mobile devices.  
- **Fast and Efficient**: Provides summaries within seconds with a simple copy-paste workflow.  

---

## 🚧 Constraints  

- **Text Length**: The input text is processed in chunks of up to **500 words** for optimal summarization. Longer texts are split and summarized individually.  
- **Summary Length**: The summarized output is dynamically determined based on the input text length:  
  - **Short Inputs**: Summaries are concise, with a minimum of **30 words** and a maximum of **50 words**.  
  - **Long Inputs**: Summaries can go up to **150 words** but are constrained by the capabilities of the Hugging Face API.  
- **API Limits**: The app relies on the Hugging Face API, so response time and accuracy depend on their service availability.  
- **Context Preservation**: For very large texts, summaries are generated for individual chunks and then combined. This may lead to slightly reduced coherence across combined summaries.  

---

## 📸 Preview  

![Text Summarization Tool Preview](Text_Summarization_Tool.jpg)

---

## 🚀 Installation  

### Prerequisites  
- Python 3.8+  
- Django 4.x  
- Node.js & npm (for Tailwind CSS)  
- Hugging Face API key  

### Clone the Repository  
```bash  
git clone https://github.com/obiwan04kanobi/text_summarizer.git  
cd text_summarizer  
```  

### Backend Setup  
1. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  
2. **Run Database Migrations**  
   ```bash  
   python manage.py migrate  
   ```  
3. **Start the Development Server**  
   ```bash  
   python manage.py runserver  
   ```  

### Frontend Setup  
1. **Install Tailwind CSS**  
   Navigate to the `static` folder:  
   ```bash  
   cd static  
   npm install  
   ```  
2. **Build Tailwind Styles**  
   ```bash  
   npx tailwindcss -i ./src/input.css -o ./css/output.css --watch  
   ```  

---

## 🌐 Usage  

1. Access the app locally at `http://127.0.0.1:8000`.  
2. Paste your text into the input field.  
3. Click "Summarize" to generate a concise summary.  
4. The summary will appear below the input box.

---

## ⚡ API Integration  

This project integrates with the [Hugging Face API](https://huggingface.co/) for text summarization. To enable API access:  
1. Sign up at [Hugging Face](https://huggingface.co/) and get your API key.  
2. Create a `.env` file in the root directory:  
   ```plaintext  
   HUGGING_FACE_API_KEY=your_api_key_here  
   ```  

---

## 🖌️ Design Philosophy  

The UI takes inspiration from Apple's design methodology:  
- **Minimalism**: Clean and distraction-free interfaces.  
- **Subtle Interactions**: Smooth transitions and hover effects for a polished experience.  
- **Responsive and Accessible**: Ensuring usability across all devices and for all users.  

---

## 🤝 Contributing  

Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Add feature"`) and push (`git push origin feature-name`).  
4. Open a Pull Request.  

---

## 📜 License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## 💻 Author  

👤 **Mayank Pant**  
- [GitHub](https://github.com/obiwan04kanobi)  
- [LinkedIn](https://www.linkedin.com/in/mayank04pant/)  
- [Portfolio](https://mayankpant.codes/)