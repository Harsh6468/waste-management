const form = document.getElementById('predictForm');
const statusBox = document.getElementById('status');
const resultBox = document.getElementById('result');
const errorBox = document.getElementById('errorBox');
const predValue = document.getElementById('predValue');
const predictBtn = document.getElementById('predictBtn');

function show(el) { el.classList.remove('hidden'); }
function hide(el) { el.classList.add('hidden'); }

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    hide(resultBox);
    hide(errorBox);
    show(statusBox);
    predictBtn.disabled = true;

    const payload = {
        "City/District": document.getElementById('city').value.trim(),
        "Waste Type": document.getElementById('wasteType').value,
        "Waste Generated (Tons/Day)": Number(document.getElementById('wasteGenerated').value),
        "Population Density (People/km²)": Number(document.getElementById('popDensity').value),
        "Municipal Efficiency Score (1-10)": Number(document.getElementById('efficiency').value),
        "Disposal Method": document.getElementById('disposal').value,
        "Cost of Waste Management (₹/Ton)": Number(document.getElementById('cost').value),
        "Awareness Campaigns Count": Number(document.getElementById('awareness').value),
        "Landfill Capacity (Tons)": Number(document.getElementById('capacity').value),
        "Year": Number(document.getElementById('year').value)
    };

    try {
        const res = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        hide(statusBox);
        predictBtn.disabled = false;

        if (!res.ok || data.error) {
            errorBox.textContent = data.error || 'Prediction failed. Please check inputs and try again.';
            show(errorBox);
            return;
        }

        const value = (Array.isArray(data.predictions) ? data.predictions[0] : data["Recycling Rate (%)"] || data.prediction || data.predicted_recycling_rate);
        predValue.textContent = (value !== undefined && value !== null) ? Number(value).toFixed(2) : '--';
        show(resultBox);

    } catch (err) {
        hide(statusBox);
        predictBtn.disabled = false;
        errorBox.textContent = err?.message || 'Network error. Please try again.';
        show(errorBox);
    }
});
