document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("summarizationForm");
    const inputText = document.getElementById("inputText");
    const summaryText = document.getElementById("summaryText");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        // Get the input text
        const text = inputText.value.trim();
        if (!text) {
            alert("Please enter text to summarize.");
            return;
        }

        // Make the API request
        try {
            const response = await fetch("/api/summarize/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text })
            });

            if (!response.ok) {
                throw new Error("Failed to summarize text.");
            }

            const data = await response.json();
            summaryText.textContent = data.summary || "No summary available.";
        } catch (error) {
            summaryText.textContent = "Error: " + error.message;
        }
    });
});
