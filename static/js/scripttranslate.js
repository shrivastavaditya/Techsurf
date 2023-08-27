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
    langf = document.getElementById("langf").value;
    langs = document.getElementById("langs").value;

    //Full question for openAi
    question = "Please translate the given content from " + langf + " language to " + langs + " language: " + des;
    //alert(question)


    ansbox.innerHTML = ""

    //Answer to be shown in the textarea ansbox
    let result = await postData('/api', { "question": question })
    ansbox.innerHTML = result.answer
})