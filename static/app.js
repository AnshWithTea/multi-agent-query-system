document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("main-form");
    const queryInput = document.getElementById("query-input");
    const pdfInput = document.getElementById("pdf-input");
    const pdfLabel = document.getElementById("pdf-label");
    const resultsContainer = document.getElementById("results-container");
    const spinner = document.getElementById("loading-spinner");

    // Update the label text when a file is chosen
    pdfInput.addEventListener("change", () => {
        if (pdfInput.files.length > 0) {
            pdfLabel.textContent = `File: ${pdfInput.files[0].name}`;
        } else {
            pdfLabel.textContent = "Click or Drag to Upload PDF";
        }
    });

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const query = queryInput.value;
        const pdfFile = pdfInput.files[0];
        
        spinner.classList.remove("hidden");
        resultsContainer.classList.remove("visible");

        try {
            if (pdfFile) {
                const pdfFormData = new FormData();
                pdfFormData.append("file", pdfFile);
                
                const uploadResponse = await fetch("/api/upload_pdf", {
                    method: "POST",
                    body: pdfFormData,
                });
                if (!uploadResponse.ok) throw new Error("PDF upload failed.");
            }

            const askFormData = new FormData();
            askFormData.append("query", query);

            const askResponse = await fetch("/api/ask", {
                method: "POST",
                body: askFormData,
            });
            if (!askResponse.ok) throw new Error("Failed to get an answer.");

            const data = await askResponse.json();

            resultsContainer.innerHTML = `
                <h3>Answer</h3>
                <p>${data.answer}</p>
                <div class="rationale">
                    <strong>Agent Used:</strong> ${data.agents_used.join(", ")}<br>
                    <strong>Rationale:</strong> ${data.rationale}
                </div>
            `;
            resultsContainer.classList.add("visible");

        } catch (error) {
            resultsContainer.innerHTML = `<p>An error occurred: ${error.message}</p>`;
            resultsContainer.classList.add("visible");

        } finally {
            spinner.classList.add("hidden");
            // Clear inputs for next query
            queryInput.value = "";
            pdfInput.value = "";
            pdfLabel.textContent = "Click or Drag to Upload PDF";
        }
    });
});