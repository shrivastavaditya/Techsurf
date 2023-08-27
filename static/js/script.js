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
    des = document.getElementById("description").value;
    lang = document.getElementById("language").value;
    ton = document.getElementById("tone").value;

    //Full question for openAi
    question = "Please write a news article on " + des + " in " + lang + " language in " + ton + " tone in less than 125 words and impressive title.";
    //alert(question)
    ansbox.innerHTML = ""
        //Answer to be shown in the textarea ansbox
    let result = await postData('/api', { "question": question })
    ansbox.innerHTML = result.answer
})