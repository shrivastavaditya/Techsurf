//Post Method Implementation
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    return response.json();
}

writeButton.addEventListener("click", async() => {
    med = document.getElementById("socialmedia").value;
    des = document.getElementById("description").value;
    lang = document.getElementById("language").value;

    //Full question for openAi
    question = "Please write " + med + " on " + des + " in " + lang + " language in less than 125 words in its proper format impressive way for academic purpose."

    //Answer to be shown in the textarea ansbox
    let result = await postData('/api', { "question": question })
    ansbox.innerHTML = result.answer
})