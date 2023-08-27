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
    // document.getElementById("description").value = "";
    lang = document.getElementById("language").value;
    // document.getElementById("language").value = "";
    ton = document.getElementById("tone").value;
    // document.getElementById("tone").value = "";

    //Full question for openAi
    question = "Please write a marketing content on " + des + " in " + lang + " language in " + ton + " tone in less than 125 words with an impressive quote or dialogue and title.";
    //alert(question)

    //Answer to be shown in the textarea ansbox
    ansbox.innerHTML = ""


    let result = await postData('/api', { "question": question })
        // setTimeout(() => { alert("loading"); }, 10000);
    ansbox.innerHTML = result.answer


})