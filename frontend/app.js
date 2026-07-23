const promptEl = document.getElementById("prompt");
const submitBtn = document.getElementById("submit");
const resultEl = document.getElementById("result");
const modelBadge = document.getElementById("model-badge");
const reasonEl = document.getElementById("reason");
const responseTextEl = document.getElementById("response-text");

submitBtn.addEventListener("click", async () => {
  const prompt = promptEl.value.trim();
  if (!prompt) return;

  submitBtn.disabled = true;
  submitBtn.textContent = "Routing...";

  try {
    const res = await fetch("/api/route", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    const data = await res.json();

    modelBadge.textContent = data.decision.model;
    reasonEl.textContent = data.decision.reason;
    responseTextEl.textContent = data.response;
    resultEl.classList.remove("hidden");
  } catch (err) {
    alert("Something went wrong. Is the backend running?");
    console.error(err);
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Route Task";
  }
});
