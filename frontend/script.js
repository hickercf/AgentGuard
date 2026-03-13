const API = "http://127.0.0.1:8000"


async function analyzeTask(){

    const task = document.getElementById("taskInput").value

    const response = await fetch(API + "/api/analyze",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            task: task,
            code: ""
        })

    })

    const data = await response.json()

    document.getElementById("result").textContent =
        JSON.stringify(data,null,2)
}


async function loadHistory(){

    const response = await fetch(API + "/api/history")

    const data = await response.json()

    document.getElementById("history").textContent =
        JSON.stringify(data,null,2)
}