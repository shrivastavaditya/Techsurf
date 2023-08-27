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

    document.querySelector(".btn2").style.display = "block"
    document.querySelector(".writeButton").style.display = "none"
        //Full question for openAi
    question = "Please write an e-commerce content on " + des + " in " + lang + " language in " + ton + " tone in less than 125 words with an impressive quote or dialogue and title.";
    //alert(question)
    ansbox.innerHTML = ""
        //Answer to be shown in the textarea ansbox
    let result = await postData('/api', { "question": question })
    ansbox.innerHTML = result.answer

    document.querySelector(".writeButton").style.display = "block"
    document.querySelector(".btn2").style.display = "none"

})